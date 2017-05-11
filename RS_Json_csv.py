#!/usr/bin/python

import json
import csv

with open("abc_RC.txt", "r") as ins:
    with open("RC_all_data_merged_politics.csv", "w", 0) as abc:
        abc = csv.writer(abc)
	abc.writerow(["body","author","subreddit","link_id","subreddit_id","created_utc","id"])
	for line in ins:
            j = json.loads(line)
            try: abc.writerow([j["body"],j["author"],j["subreddit"],j["link_id"],j["subreddit_id"],j["created_utc"],j["id"]])
            except (RuntimeError, TypeError, NameError, KeyError, UnicodeEncodeError):
                pass
