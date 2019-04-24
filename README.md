Website Crawler  
  
    
      
Introduction:

This is the individual project for EE-551-B.        Author: Yining Wen


Proposal:

This project aims to program a crawler for the Website, which could search the information in the specific website, find and download the information that needed, and store them in mongoDB or other type file.


Notice:

I was planning to program a crawler for website Yelp, download the restaurant information. But after I ran my first program, file "YelpCrawler", I found that crawler was banned by Yelp. I cannot get any more information from it. So I replaced the website by "http://quotes.toscrape.com/". This is a simple website but contains information for crawler rookies to practice.


Features:

•   Crawler searches information from website  
•   Using Scrapy framework  
•   Store data in database mongoDB  
•   Store data in ".json/.csv/.xml" type file  
•   Able to search data page by page automatically  
   (Able to automatically go to the next page by requesting the url connection in current page) 


How To Run This Program:

•   Having python 3.7 operating environment  
•   Having mongoDB environment(you can also run this program without mongoDB, please see the section "How to Run This   Program Without MongoDB")  
•   Install Scrapy package in your environment by using "pip install scrapy"  
•   Install mongoDB package in your environment by using "pip install pymongo"  
•   cd into the first folder "another"  
•   Run this program bu using "scrapy crawl another"   
  
  If everything work functionally, you will see the scrawler data in your mongoDB
    
    
How to Run This Program Without MongoDB:
•   Please comment the code line 67-69 in file "settings.py" like below

        #    ITEM_PIPELINES = {
        #   'another.pipelines.AnotherPipeline': 300,
        #}  
•   Run this program by using "scrapy crawl another -o items.json". This method will import the output to a file named            "items.json"  
•   Run this program by using "scrapy crawl another -o items.csv". This method will import the output to a file named            "items.csv"  
•    Run this program by using "scrapy crawl another -o items.xml". This method will import the output to a file named            "items.xml"
