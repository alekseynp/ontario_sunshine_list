# Ontario Sunshine List

This is a set of scripts and useful functions for anyone wanting to work with the Public Salary Disclosure data as published by the Ontario Ministry of Finance, also known as the Sunshine List.

# How to Use

**Download the Data**

The basic output from this toolchain is available for download in CSV format here: (link missing)

**Process Your Own**

1. Collect the raw HTML from http://www.fin.gov.on.ca/en/publications/salarydisclosure/
```python
from ontario_sunshine_list import collect  
collect.collect('/home/aleksey/data/sunshine/')
```
2. Scrape the data
```python
from ontario_sunshine_list import scrape
df = scrape.scrape_one_big_df('/home/aleksey/data/sunshine/')
```
3. Clean the data
```python
from ontario_sunshine_list import clean
df_clean = clean.clean(df)
```
4. Save
```python
df_clean.to_csv('/home/aleksey/data.csv', encoding='utf-8')
```
