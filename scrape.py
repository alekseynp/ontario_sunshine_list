from config import *

def scrape(path):
# Takes in the path to an HTML file
# Returns a list of dicts containing a dataframe for each table in that file
# And some meta-data about it
# { file - path scraped, table_number - the nth table in that file, df - pandas DataFrame }

    with open(path, "r") as text_file:
        html = text_file.read()
        
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html)
    
    tables = soup.findAll('table')
    
    # This is the list we will be building of dataframes corresponding to the tables in this file
    table_dfs = []
    
    for t, table in enumerate(tables):    
        theads = table.findAll('thead')
        
        if len(theads) == 0:
            table_data = [[cell.text for cell in row(['td','th'])]
                                 for row in table("tr")]
            headers = table_data[0]
            del table_data[0]
        else:
            # In case there is more than one thead, we want the last one
            thead = theads[-1]
            
            # Sometimes there is more than one row in the thead
            # If there is, we want the last one
            thead_rows = thead('tr')
            if len(thead_rows) > 0:
                thead = thead_rows[-1]
                
            headers = [cell.text for cell in thead('th')]
            
            tbody = table.findAll('tbody')[0]
            table_data = [[cell.text for cell in row("td")]
                                 for row in tbody("tr")]
        
        import pandas as pd
        if len(table_data) > 0:
            
            # Adds dummy headers in case there weren't enough to cover all of the columns in the actual rows
            while len(headers) < max([len(row) for row in table_data]):
                headers.extend([u'dummy'])
                
            # Drops headers off the end in case there were too many headers
            headers = headers[0:max([len(row) for row in table_data])]

            import os
            table_dfs.extend([{"file":os.path.basename(path),"table_number":str(t),"df":pd.DataFrame(table_data, columns=headers)}])
    
    # Ensure we free up memory
    soup.decompose()
    
    return table_dfs

def scrape_directory(path, verbose=True):
# Builds a collection of pandas DataFrames along with meta data
# Corresponding to every table in every HTML file in a directory
    results = []
    
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
    
    for f in onlyfiles:
        if verbose:
            print f
        results.extend(scrape(path + f))
        
    return results

def scrape_directory_2013_onwards(path, year, verbose=True):
# Variant of scrape_directory that aligns with the more recent style of data
# Looks for "year=2012" or equivalent in the filename
    results = []
    
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
    
    for f in onlyfiles:
        if ('year=' + str(year-1)) in f:
            # Ontario Ministry of Finance website has duplicated links
            # SAME DATA from
            # - http://www.fin.gov.on.ca/en/publications/salarydisclosure/pssd/orgs.php?organization=ministries&year=2013
            # - http://www.fin.gov.on.ca/en/publications/salarydisclosure/pssd/orgs.php?pageNum_pssd=0&totalRows_pssd=10483&organization=ministries&year=2013
            # - http://www.fin.gov.on.ca/en/publications/salarydisclosure/pssd/orgs.php?pageNum_pssd=0&organization=ministries&year=2013
            
            # All organizations have links corresponding to the second type, even when there is only one page
            # So we will filter for that
            
            if '&totalRows_pssd=' in f:   
                if verbose:
                    print f
                results.extend(scrape(path + f))
        
    return results

def do_year(year, config, local_save_dir_base):
# Returns a single dataframe of all data from a single year
    
    # Newer years have a new format
    if year >= 2013:
        results = scrape_directory_2013_onwards(local_save_dir_base + config['html_dir'], year, verbose=False)
    else:
        results = scrape_directory(local_save_dir_base + config['html_dir'], verbose=False)
        
    # Addenda not used for now
    # results_addenda = filter(lambda item: item['file'] in config['addenda'], results)
    
    results_core = filter(lambda item: item['file'] not in config['core_exclude'], results)
    
    # Rename columns with the broad translators
    for r in results_core:
        for c in r['df'].columns:
            c_stripped = "".join(c.split())
            for rule in stripped_contains_column_translator.keys():
                if rule in c_stripped:
                    r['df'].rename(columns={c:stripped_contains_column_translator[rule]},inplace=True)
    
    # Rename columns with targeted translators
    for r in results_core:
        for c in r['df'].columns:
            if c not in column_translator.keys():
                print r
            else:
                r['df'].rename(columns={c:column_translator[c]},inplace=True)
    
    # Translate filenames into categories. For instance "munic" is "Municipalities"
    for r in results_core:
        for c in category_translator.keys():
            if c in r['file']:
                r['df']['Category'] = category_translator[c]
                
    # Useless columns are cleared out
    for r in results_core:
        columns_to_drop = []
        for c in r['df'].columns:
            if c not in core_columns:
                columns_to_drop.append(c)
        r['df'].drop(columns_to_drop, axis=1, inplace=True)
    
    
    all_dfs = []
    for r in results_core:
        all_dfs.append(r['df'])
    import pandas as pd
    df_core = pd.concat(all_dfs)
    
    # Cleanup Salary
    df_core['Salary'] = df_core['Salary'].str.replace(',','').str.replace('$','')
    df_core['Salary'] = df_core['Salary'].convert_objects(convert_numeric=True)
    
    # Cleanup Benefits
    df_core['Benefits'] = df_core['Benefits'].str.replace(',','').str.replace('$','')
    df_core['Benefits'] = df_core['Benefits'].convert_objects(convert_numeric=True)
    return df_core

def scrape_one_big_df(local_save_dir_base):
    all_year_dfs=[]

    for year in configuration.keys():
        print "Processing year " + str(year) + "..."
        df_year = do_year(year, configuration[year], local_save_dir_base)
        print "Done."
        
        df_year['year'] = year
        all_year_dfs.append(df_year)
        import pandas as pd
        df_clean = pd.concat(all_year_dfs)
        
    return df_clean