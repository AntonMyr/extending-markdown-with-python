import os
import sys
from datetime import datetime

from lib import tag_checker

latest_week = False
latest_month = False
if len(sys.argv) > 1:
    if sys.argv[1] == "m":
        latest_month = True
    else:
        latest_week = True
else:
    latest_week = True

tags = tag_checker()
tags.add_tag("question", "<q", "q>")
tags.add_tag("remember", "r==", "==r")
tags.add_tag("idea", "<i", "i>")

dirs = ["/Users/antonmyrberg/extending-markdown-with-python/notes"]

for folder in dirs:
    for filename in os.listdir(folder):
        correct_md = filename[-2:] == "md"
        if not correct_md:
            continue

        full_path = folder + "/" + filename
        curr_fp = open(full_path, "r")

        for line in curr_fp:
            tags.run(line)

        curr_fp.close()

tmp_file = "/tmp/" + datetime.now().strftime("%y%m%d%H%M%S") + ".md"

tmp_fp = open(tmp_file, "w")

tmp_fp.write("# Collection from this week\n")

for tag in tags.tags:
    for i, tag_item in enumerate(tags.tags[tag]["tag_list"]):
        tmp_fp.write("## %s %d\n" % (tag, i))
        tmp_fp.write(tag_item + "\n")

tmp_fp.close()
print(tmp_file)
