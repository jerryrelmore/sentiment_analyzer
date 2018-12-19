#!/bin/python3

# File: settings_sample.py
# Note: Rename to settings.py when you've got the fields below filled out.

import auth_keys

TRACK_TERMS = ['','','']
CONNECTION_STRING = "mysql://%s:%s@%s/%s?charset=utf8mb4" % (auth_keys.MYSQL_USER, auth_keys.MYSQL_PASSWORD, auth_keys.MYSQL_HOST, auth_keys.MYSQL_DATABASE)
CSV_NAME = ''
TABLE_NAME = ''
