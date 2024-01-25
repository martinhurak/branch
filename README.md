# rm-scraper
Realitymap scraper is intended to be universal scraping script able to scrape data from 
simple HTML/CSS based real estate sites on slovak internet. Site must be HTML based, scraper has no 
capability to run or evaluate javascript.

Each site has common structure of landing page with list of advertisments. Script can open
every one of the advertisments by going to link in ad href and extract its content.

In first step, script is searching for hrefs on landing page. In second step, every link 
is opened and the content is searched for ad properties like price, size, type.
When the landing page is paginated the script opens next page of the list by opening the href
of next page.

Your task is to define and test the set of selecors for each website in the website list XLS.
First step is to test it by runing the script using config-test.json when all info are extracted correctly 
and csv is filled with data, paste the final config to config.json

# installation
```pip install -r requirements.txt```
```pip install --upgrade scrapy twisted```
Python 3.10 or above is recommended

# configuration
```config.json``` conatins css selector definitions of pages already tested and extracted, you can get the idea how the selecors works by analysing website and comparing with already defined selectors in this config file  
```config-test.json``` contains css selector definitions of page which is currently being tested by the script

# css selectors
css selector used in the config are specific Scrapy selectors which are identifying the elements on website
these selectors have different syntax than standard ones, for more info have a look on scrapy documentation
https://docs.scrapy.org/en/latest/topics/selectors.html

# config file scrucutre
```
{
    "name": name of real estate agency,
    "start_url": landing page with list of ads,
    "page_selectors": {
        "hrefs": ad link href selector,
        "next_page": next page href selector
    },
    "item_selectors": {
        "title": text of ad title (Predam 2-izb byt v Ruzinove na ul. Kosicka),
        "img_url": url of the image,
        "price": price text selector (150 000 EUR),
        "district": city/district selector (Trencin, Bratislava-Ruzinov),
        "street": location/street selector (Kosicka),
        "category": type of property (byty, domy, pozemky),
        "property_type": category of propety (1 izbovy byt, 2 izbovy byt, rodinny dom)
        "property_size": size in sqm selector (50m2),
        "property_condition": condition of proprerty (novostavba, povodny stav)
    }
},
```
**Important:** If there is no street, or property size, or any other info information available on site, just remove the correspondig selector from the config file

# running the script
```scrapy runspider universal_spider.py```

# output csv files
oputput csv files are generated to data/raw/ folder where you can check if the intended ad parameters are being scraped correctly

# list of websites to be scraped
```Zoznam realitných kancelárií 1-31.xlsx```
