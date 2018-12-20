# sentiment_analyzer
### Streaming Twitter sentiment analyzer using Tweepy, TextBlob, MySQL, SQLAlchemy, and dataset

------
<b>LICENSE:</b>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see http://www.gnu.org/licenses/.

@author: Jerry Elmore <jerry.r.elmore@silverfox.email>
 
@authors-original: This project is an offline fork of [this Git](https://github.com/dataquestio/twitter-scrape) and based on the 
DataquestIO [tutorial](https://www.dataquest.io/blog/streaming-data-python/). I modified the original source and fixed errors thrown 
by the original Git.
------

Version 0.01:
Date: 19-Dec-2018
------

<i>It is a work in progress and not yet complete - at this point, it is only scraping tweets and
adding the tweets and some relevant metadata to a MySQL database. Updates are forthcoming though.</i>

<b>NOTE: This analyzer uses Python 3 - there is a >97% chance it will not work in Python 2
without modification. Additionally, the instructions below assume you already have a 
Twitter developer account ([apply here](https://developer.twitter.com/en/apply-for-access.html)), as well as the two Twitter keys and two Twitter secrets 
you will need for your app-user authentication ([instructions here](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)).</b>
------

### Installation of dependencies
<b>You must already have MySQL server installed and a user with full GRANTS privileges. If you do not,
follow the official instructions [here](https://dev.mysql.com/doc/mysql-getting-started/en/). I use vanilla MariaDB with no optimization and hundreds of 
thousands of rows with no issues - YMMV.</b>
1. <code>pip3 install -U -r requirements.txt</code>
2. <code>sudo apt install python3-mysqldb</code>
3. <code>python3 -m textblob.download_corpora</code>
------

### Setup your connections
1. Clone this Git to your home directory - <code>git clone https://github.com/jerryrelmore/sentiment_analyzer.git</code>.
2. <code>cd ~/sentiment_analyzer</code>
3. Rename <code>auth_keys_sample.py</code> to <code>auth_keys.py</code>. Add your Twitter keys/secrets and your MySQL info, such as username, host (e.g., 
'localhost'), plain text MySQL password and and database that will be used to store the tweets.
4. Change permissions for <code>auth_keys.py</code> so it is readable only by your system user (and/or <code>root</code>) - <code>chmod 0600 auth_keys.py</code>.
5. Rename <code>settings_sample.py</code> to <code>settings.py</code>. Add the terms you want to search for in the Twitter stream, add a name for a CSV file 
(if you want to export the results to CSV in addition to the database) and add a table name to use for the tweets table in the database. <b>NOTE:</b> If the table
doesn't exist when you run the analyzer, the imported <code>dataset</code> module will create a table with the name in this field.
6. You're now ready to run the analyzer - <code>python3 ./sentiment_analyzer.py</code>.
------

### Operation notes
1. Once you start the analyzer, it will give you a message stating whether or not the database connection was established (and an error message if it was <i>not</i>), 
and then begin automatically printing the results to screen. You can disable this feature by commenting out or removing the appropriate <code>print</code> commands. 
2. If you search for a term like <code>supercalifragilisticexpialidocious</code> you may get one tweet per year, whereas if you search multiple terms, say <code>trump</code>, 
<code>clinton</code>, and <code>obama</code>, you will get dozens upon dozens of tweets per second.
3. This leads us to a point worth noting: the above setup instructions assume you're using Twitter's free, non-premium/not-enterprise API. The free-use API has rate limits
that may come into play if you search for more than several hundred concurrent terms (e.g., the entire NYSE ticker symbol list) or your server's connection can't keep up with
the results. At this point, Twitter will start throwing you <code>420</code> errors. A method is defined in the analyzer to handle these errors, but if you do see them 
popping up, consider narrowing your search terms or increasing your server's allocated bandwidth so that your app isn't banned.
-----

### Analysis notes
<b>TO BE CONTINUED</b> I have to add the methods to the script that perform, y'know, the actual analysis. Then I'll update this README to provide instructions on how to 
setup and/or tweak the results.
------

### DISCLAIMER
I explicitly do not warranty this tool for any use case, organization or operator/user. Your results are your results and you should thoroughly consider the implications of 
collecting, analyzing and/or retaining this publicly-available data.
