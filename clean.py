import re
import pandas as pd

class Cleaner:

    def __init__(self):
        pass

    def run(self, df_dirty):
        df_clean = df_dirty.reset_index()
        df_clean.drop('index', axis=1, inplace=True)
        
        
        # The following is very unstable and should be fixed up
               
        df_clean.loc[df_clean['Category']=='MUNICIPALITIES','Category'] = 'Municipalities and Services'
        df_clean.loc[df_clean['Category']==' SCHOOL BOARD','Category'] = 'School Boards'
        df_clean.loc[df_clean['Category']=='ONTARIO PUBLIC SERVICE','Category'] = 'Ontario Public Service'
        df_clean.loc[df_clean['Category']=='CROWN AGENCIES','Category'] = 'Crown Agencies'
        df_clean.loc[df_clean['Category']==' MUNICIPALITIES','Category'] = 'Municipalities and Services'
        df_clean.loc[df_clean['Category']==' SCHOOL BOARDS','Category'] = 'School Boards'
        df_clean.loc[df_clean['Category']==' CROWN AGENCIES','Category'] = 'Crown Agencies'
        df_clean.loc[df_clean['Category']==' ONTARIO PUBLIC SERVICE','Category'] = 'Ontario Public Service'
        df_clean.loc[df_clean['Category']=='Ontario Public Services','Category'] = 'Ontario Public Service'
        
        
        df_clean['Employer'] = df_clean['Employer'].apply(lambda x: re.sub(' +',' ',unicode(x).strip().replace(u'\r',u'').replace(u'\n',u'').replace(u'\t',u'')))
        df_clean['Position'] = df_clean['Position'].apply(lambda x: re.sub(' +',' ',unicode(x).strip().replace(u'\r',u'').replace(u'\n',u'').replace(u'\t',u'')))
        
        # Unbelievably, we have to fix the following two entries
        # $128,059,85
        df_clean.loc[df_clean['Salary'] == 12805985, 'Salary'] = 128059.85
        # $127,455,00
        df_clean.loc[df_clean['Salary'] == 12745500, 'Salary'] = 127455.00
        

        # Malformed HTML, presumably from manual involvement by Ministory of Finance Employees
        bad_row_1 = df_clean.loc[df_clean['Given Name']=='$720.82']
        #       Benefits                     Category  \
        #1590       NaN  Municipalities and Services   
        #
        #                                       Employer Given Name Position  Salary  \
        #1590         Employment Equity and Human Rights    $720.82     None     NaN   
        #
        #          Surname  year  
        #1590  $107,307.79  2007 
        bad_row_2 = df_clean.loc[(df_clean['Given Name']=='EVA') & (df_clean['Surname']=='LANGER') & (df_clean['year']==2007)]
        #      Benefits                     Category         Employer Given Name  \
        #1589       NaN  Municipalities and Services  City of Toronto        EVA   
        #
        #                                               Position  Salary Surname  year  
        #1589  Human Resources Manager Staffing, Workforce Tr...     NaN  LANGER  2007
        #
        better_row = pd.DataFrame({
            'Benefits':['720.82'],
            'Category':['Ministries'],
            'Employer':['City of Toronto'],
            'Given Name':['EVA'],
            'Position':['Transition, Employment Equity and Human Rights'],
            'Salary':['107307.79'],
            'Surname':['LANGER'],
            'year':[2007]})


        df_clean = df_clean.append(better_row)

        df_clean = df_clean.dropna()
        
        return df_clean