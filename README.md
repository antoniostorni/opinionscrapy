Opinion scrapper with Scrapy framwork
===================

## DESCRIPTION ##

This program reads a list from opinions from http://www.cadc.uscourts.gov/internet/opinions.nsf and stores the results in a json file.

## USAGE ##

Scrapy project version:

```
scrapy crawl opinions -o results.json
```


Basic spider self-contained in one file version:

```
scrapy runspider basicspider.py -o results.json
```


## Installation

   pip install -r requirements.txt

Package version details are on requirements.txt file.



