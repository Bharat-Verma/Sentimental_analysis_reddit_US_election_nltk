#!/usr/bin/python

import json
import csv

with open("RC_AllData_merged_wos.csv", "r") as ins:
    with open("RC_id_col.csv", "w", 0) as abc:
        abc = csv.writer(abc)
        abc.writerow(["id"])
        for line in ins:
            j = json.loads(line)
            try: abc.writerow([
		 j["id"]])
            except (RuntimeError, TypeError, NameError, KeyError, UnicodeEncodeError):
                pass
