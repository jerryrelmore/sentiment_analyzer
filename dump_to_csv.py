#!/bin/python3

# File: dump_to_csv.py
# This script will dump MySQL database Tweet scraper results to CSV formatted file

import sys
import auth_keys
import settings
import dataset
from datafreeze import freeze

# Connect to our MariaDB database (tweet_sentiment_analysis)
try:
    # utf8mb4 encoding is necessary because Twitter uses 4 byte characters for things like emojis
    print("\n\nAttempting to connect to database...\n")
    db = dataset.connect(settings.CONNECTION_STRING)
    print("Database connection successful!\n")
except:
    print("Database connection failed...aborting.\n")
    print("Unexpected error:", sys.exc_info()[0])
    raise

# Pull all tweets from the MySQL database
try:
    print("Pulling tweets from database %s...\n" % (auth_keys.MYSQL_DATABASE))
    results = db[settings.TABLE_NAME].all()
    print("Pull successful!\n")

    #Export to CSV
    print("Exporting tweets to %s...\n" % (settings.CSV_NAME))
    freeze(results, format='csv', filename=settings.CSV_NAME)
    print("Export successful!\n")
except:
    print("Database export failed...aborting.\n")
    print("Unexpected error:", sys.exc_info()[0])
    raise
