configuration = {
    2014:{
            'html_dir':'scrape/pssd/',
            'addenda':['addenda_14.html'],
            'core_exclude':[],
            },  
    2013:{
            'html_dir':'scrape/pssd/',
            'addenda':['addenda_13.html'],
            'core_exclude':['nosalaries.php&organization=nosalaries&year=2012'],
            },       
    2012:{
            'html_dir':'scrape/2012/',
            'addenda':['addenda_12.html'],
            'core_exclude':['addenda_12.html', 'nosal12.html', 'pssdguide.html'],
            },
    2011:{
            'html_dir':'scrape/2011/',
            'addenda':['addenda_11.html'],
            'core_exclude':['addenda_11.html', 'nosal11.html', 'pssdguide.html'],
            },
    2010:{
            'html_dir':'scrape/2010/',
            'addenda':['addenda_10.html'],
            'core_exclude':['addenda_10.html', 'nosal10.html', 'pssdguide.html'],
            },
    2009:{
            'html_dir':'scrape/2009/',
            'addenda':['addenda_09.html'],
            'core_exclude':['addenda_09.html', 'nosal09.html', 'pssdguide.html'],
            },
    2008:{
            'html_dir':'scrape/2008/',
            'addenda':['addenda_08.html'],
            'core_exclude':['addenda_08.html', 'nosal08.html', 'pssdguide.html'],
            },
    2007:{
            'html_dir':'scrape/2007/',
            'addenda':['addenda_07.html','addenda_07_2nd.html'],
            'core_exclude':['addenda_07.html','addenda_07_2nd.html', 'nosal07.html', 'pssdeg.html'],
            },
    2006:{
            'html_dir':'scrape/2006/',
            'addenda':['addenda1_06.html'],
            'core_exclude':['addenda1_06.html', 'nosal06.html', 'pssdeg.html'],
            },
    2005:{
            'html_dir':'scrape/2005/',
            'addenda':['addenda1_05.html'],
            'core_exclude':['addenda1_05.html', 'nosal05.html', 'pssdeg.html'],
            },
    2004:{
            'html_dir':'scrape/2004/',
            'addenda':['addenda1_04.html'],
            'core_exclude':['addenda1_04.html', 'nosal04.html'],
            },
    2003:{
            'html_dir':'scrape/2003/',
            'addenda':['addenda3_03.html'],
            'core_exclude':['addenda3_03.html', 'nosal03.html', 'intro03.html'],
            },
    2002:{
            'html_dir':'scrape/2002/',
            'addenda':['psadd_02.html'],
            'core_exclude':['psadd_02.html', 'nosal02.html', 'intro02.html'],
            },
    2001:{
            'html_dir':'scrape/2001/',
            'addenda':['pssdad01.html'],
            'core_exclude':['pssdad01.html', 'nosal01.html', 'intro01.html'],
            },
    2000:{
            'html_dir':'scrape/2000/',
            'addenda':['adden00.html'],
            'core_exclude':['adden00.html', 'nosal00.html', 'intro00.html'],
            },
    1999:{
            'html_dir':'scrape/1999/',
            'addenda':['addendum.html'],
            'core_exclude':['addendum.html', 'nosalari.html', 'intro99.html'],
            },
    1998:{
            'html_dir':'scrape/1998/',
            'addenda':['adden98a.html'],
            'core_exclude':['adden98a.html', 'nosal98a.html'],
            },
    1997:{
            'html_dir':'scrape/1997/',
            'addenda':['addend1.html','saddend2.html','addend3.html'],
            'core_exclude':['addend1.html','addend2.html','addend3.html'],
            }
}

column_translator ={
    u'Taxable Benefits / Avantages imposables':u'Benefits',
    u'Ministry / Minist\xe8re':u'Ministry',
    u'Given Name / Pr\xe9nom':u'Given Name',
    u'Position / Poste':u'Position',
    u'Seconded Position / Poste combl\xe9 par la personne d\xe9tach\xe9e':u'Position',
    u'Taxable Benefits / Avantages imposables Avantages imposables*':u'Benefits',
    u'Surname / Nom de famille':u'Surname',
    u'Salary Paid / Traitement*':u'Salary',
    u'Employer / Employeur':u'Employer',
    u'Salary Paid / Traitement':u'Salary',
    u'Public Sector Organization Employer / Employeur - Organisme du secteur public':u'Employer',
    u'Employer':u'Employer',
    u'Surname':u'Surname',
    u'Given Name':u'Given Name',
    u'Salary':u'Salary',
    u'Benefits':u'Benefits',
    u'Position':u'Position',
    u'Ministry':u'Ministry',
    u'dummy':u'dummy',
    u'Taxable Benefits / Avantages imposables*':u'Benefits',
    u'Given\r\n \t\t\t\t\t\t\t\tName / Pr\xe9nom':u'Given Name',
    u'Salary\r\n \t\t\t\t\t\t\t\tPaid / Traitement':u'Salary',
    u'Sector':u'Category',
                    }

stripped_contains_column_translator = {
    #u'TaxableBenefits':u'Benefits',
    u'Benefits':u'Benefits',
    u'Ministry':u'Ministry',
    u'GivenName':u'Given Name',
    u'FirstName':u'Given Name',
    u'Position':u'Position',
    u'Surname':u'Surname',
    #u'SalaryPaid':u'Salary',
    u'Salary':u'Salary',
    u'Employer':u'Employer',
                                        }

category_translator = {
 'agencies':'Crown Agencies',
 'colleg':'Colleges',
 'crown':'Crown Agencies',
 'electric':'Hydro One and Ontario Power Generation',
 'hospit':'Hospitals and Boards of Public Health',
 'judiciary':'Judiciary',
 'legassembly':'Legislative Assembly and Offices',
 'legislative':'Legislative Assembly and Offices',
 'ministries':'Ministries',
 'munic':'Municipalities and Services',
 'other':'Other Public Sector Employers',
 'schbd':'School Boards',
 'schoolboards':'School Boards',
 'schoolbd':'School Boards',
 'unive':'Universities',
 'ontpub':'Ontario Public Service',
 'ops':'Ontario Public Services',
 'seconded':'Ministries'
}

core_columns = [u'Employer', u'Surname', u'Given Name', u'Position', u'Salary', u'Benefits', u'Category']