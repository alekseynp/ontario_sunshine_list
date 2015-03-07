import re

class Cleaner:

    def __init__(self):
        pass

    def run(self, df_dirty):
        df_clean = df_dirty.reset_index()
        df_clean.drop('index', axis=1, inplace=True)    
        
        
        # The following is very unstable and should be fixed up
        
        value_counts_category = df_clean['Category'].value_counts()
        
        df_clean.loc[df_clean['Category']==value_counts_category.index[13],'Category'] = 'Ontario Public Service'
        df_clean.loc[df_clean['Category']==value_counts_category.index[14],'Category'] = 'Crown Agencies'
        df_clean.loc[df_clean['Category']==value_counts_category.index[15],'Category'] = 'School Boards'
        df_clean.loc[df_clean['Category']==value_counts_category.index[16],'Category'] = 'Municipalities'
        df_clean.loc[df_clean['Category']==value_counts_category.index[17],'Category'] = 'Crown Agencies'
        df_clean.loc[df_clean['Category']==value_counts_category.index[18],'Category'] = 'Ontario Public Service'
        df_clean.loc[df_clean['Category']==value_counts_category.index[19],'Category'] = 'School Boards'
        df_clean.loc[df_clean['Category']==value_counts_category.index[20],'Category'] = 'Municipalities'
        
        df_clean['Employer'] = df_clean['Employer'].apply(lambda x: re.sub(' +',' ',unicode(x).strip().replace(u'\r',u'').replace(u'\n',u'').replace(u'\t',u'')))
        df_clean['Position'] = df_clean['Position'].apply(lambda x: re.sub(' +',' ',unicode(x).strip().replace(u'\r',u'').replace(u'\n',u'').replace(u'\t',u'')))
        
        # Unbelievably, we have to fix the following two entries
        # $128,059,85
        df_clean.loc[df_clean['Salary'] == 12805985, 'Salary'] = 128059.85
        # $127,455,00
        df_clean.loc[df_clean['Salary'] == 12745500, 'Salary'] = 127455.00
        
        df_clean = df_clean.dropna()
        
        return df_clean