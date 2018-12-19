# sentiment_analyzer
### Twitter sentiment analyzer using Tweepy, TextBlob, MySQL, SQLAlchemy, and dataset

This project is an offline fork of [this Git](https://github.com/dataquestio/twitter-scrape) and based on the DataquestIO [tutorial](https://www.dataquest.io/blog/streaming-data-python/). Updated and 
fixed errors thrown from the original Git.

It is a work in progress and not yet complete - at this point, it is only scraping tweets and
adding the tweets and some relevant metadata to a MySQL database. Updates are forthcoming though.

<b>NOTE: This analyzer uses Python 3 - there is a >97% chance it will not work in Python 2
without modification. Additionally, the instructions below assume you already have a 
Twitter developer account ([apply here](https://developer.twitter.com/en/apply-for-access.html)), as well as the two Twitter keys and two Twitter secrets 
you will need for your app-user authentication ([instructions here](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)).</b>

------

### Installation of dependencies
<b>You must already have MySQL server installed and a user with full GRANTS privileges. If you do not,
follow the official instructions [here](https://dev.mysql.com/doc/mysql-getting-started/en/). Personally, I use MariaDB analyzing millions of rows with no issues - YMMV.</b>
1. <code>pip3 install -U -r requirements.txt</code>
2. <code>sudo apt install python3-mysqldb</code>
3. <code>python3 -m textblob.download_corpora</code>
------

### Setup your connections
1. Clone this Git to your home directory.
2. <code>cd ~/sentiment_analyzer</code>
3. TO BE CONTINUED
