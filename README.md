# Ontario Sunshine List Open Scraper

This is a set of scripts and useful functions for anyone wanting to work with the Public Salary Disclosure data as published by the Ontario Ministry of Finance, also known as the Sunshine List.

# How to Use

**Download the Data**

The basic output from this toolchain is available for download in CSV format here: https://s3-us-west-1.amazonaws.com/ontariosunshinelist/data_2015_06_17.csv

**Process Your Own**

```python
import ontario_sunshine_list as osl
```
Collect the raw HTML from http://www.fin.gov.on.ca/en/publications/salarydisclosure/  
As of June 17, 2015 this is approx 500 mb of data.  
```python
col = osl.Collector()
col.run('/home/aleksey/data/sunshine/')
```
Scrape the data  
```python
scr = osl.Scraper()
df = scr.run('/home/aleksey/data/sunshine/')
```
Clean the data  
```python
cle = osl.Cleaner()
df = cle.run(df)
```
Save  
```python
df.to_csv('/home/aleksey/data.csv', encoding='utf-8')
```

# Outstanding Issues

* Only the initial disclosure is scraped. Addenda are not scraped or processed.
* A couple of garbled datapoints in the HTML are not captured.
