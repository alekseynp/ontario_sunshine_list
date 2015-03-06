configuration = {
    2014:{
            'html_dir':'scrape/pssd/',
            'addenda':['scrape/2014/addenda_14.html'],
            'core_exclude':[],
            },  
    2013:{
            'html_dir':'scrape/pssd/',
            'addenda':['scrape/2013/addenda_13.html'],
            'core_exclude':['scrape/pssd/nosalaries.php&organization=nosalaries&year=2012'],
            },       
    2012:{
            'html_dir':'scrape/2012/',
            'addenda':['scrape/2012/addenda_12.html'],
            'core_exclude':['scrape/2012/addenda_12.html', 'scrape/2012/nosal12.html', 'scrape/2012/pssdguide.html'],
            },
    2011:{
            'html_dir':'scrape/2011/',
            'addenda':['scrape/2012/addenda_11.html'],
            'core_exclude':['scrape/2011/addenda_11.html', 'scrape/2011/nosal11.html', 'scrape/2011/pssdguide.html'],
            },
    2010:{
            'html_dir':'scrape/2010/',
            'addenda':['scrape/2010/addenda_10.html'],
            'core_exclude':['scrape/2010/addenda_10.html', 'scrape/2010/nosal10.html', 'scrape/2010/pssdguide.html'],
            },
    2009:{
            'html_dir':'scrape/2009/',
            'addenda':['scrape/2009/addenda_09.html'],
            'core_exclude':['scrape/2009/addenda_09.html', 'scrape/2009/nosal09.html', 'scrape/2009/pssdguide.html'],
            },
    2008:{
            'html_dir':'scrape/2008/',
            'addenda':['scrape/2008/addenda_08.html'],
            'core_exclude':['scrape/2008/addenda_08.html', 'scrape/2008/nosal08.html', 'scrape/2008/pssdguide.html'],
            },
    2007:{
            'html_dir':'scrape/2007/',
            'addenda':['scrape/2007/addenda_07.html','scrape/2007/addenda_07_2nd.html'],
            'core_exclude':['scrape/2007/addenda_07.html','scrape/2007/addenda_07_2nd.html', 'scrape/2007/nosal07.html', 'scrape/2007/pssdeg.html'],
            },
    2006:{
            'html_dir':'scrape/2006/',
            'addenda':['scrape/2006/addenda1_06.html'],
            'core_exclude':['scrape/2006/addenda1_06.html', 'scrape/2006/nosal06.html', 'scrape/2006/pssdeg.html'],
            },
    2005:{
            'html_dir':'scrape/2005/',
            'addenda':['scrape/2005/addenda1_05.html'],
            'core_exclude':['scrape/2005/addenda1_05.html', 'scrape/2005/nosal05.html', 'scrape/2005/pssdeg.html'],
            },
    2004:{
            'html_dir':'scrape/2004/',
            'addenda':['scrape/2004/addenda1_04.html'],
            'core_exclude':['scrape/2004/addenda1_04.html', 'scrape/2004/nosal04.html'],
            },
    2003:{
            'html_dir':'scrape/2003/',
            'addenda':['scrape/2003/addenda3_03.html'],
            'core_exclude':['scrape/2003/addenda3_03.html', 'scrape/2003/nosal03.html', 'scrape/2003/intro03.html'],
            },
    2002:{
            'html_dir':'scrape/2002/',
            'addenda':['scrape/2002/psadd_02.html'],
            'core_exclude':['scrape/2002/psadd_02.html', 'scrape/2002/nosal02.html', 'scrape/2002/intro02.html'],
            },
    2001:{
            'html_dir':'scrape/2001/',
            'addenda':['scrape/2001/pssdad01.html'],
            'core_exclude':['scrape/2001/pssdad01.html', 'scrape/2001/nosal01.html', 'scrape/2001/intro01.html'],
            },
    2000:{
            'html_dir':'scrape/2000/',
            'addenda':['scrape/2000/adden00.html'],
            'core_exclude':['scrape/2000/adden00.html', 'scrape/2000/nosal00.html', 'scrape/2000/intro00.html'],
            },
    1999:{
            'html_dir':'scrape/1999/',
            'addenda':['scrape/1999/addendum.html'],
            'core_exclude':['scrape/1999/addendum.html', 'scrape/1999/nosalari.html', 'scrape/1999/intro99.html'],
            },
    1998:{
            'html_dir':'scrape/1998/',
            'addenda':['scrape/1998/adden98a.html'],
            'core_exclude':['scrape/1998/adden98a.html', 'scrape/1998/nosal98a.html'],
            },
    1997:{
            'html_dir':'scrape/1997/',
            'addenda':['scrape/1997/addend1.html','scrape/1997/addend2.html','scrape/1997/addend3.html'],
            'core_exclude':['scrape/1997/addend1.html','scrape/1997/addend2.html','scrape/1997/addend3.html'],
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
}

core_columns = [u'Employer', u'Surname', u'Given Name', u'Position', u'Salary', u'Benefits', u'Category']