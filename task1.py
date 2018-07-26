#!/usr/bin/env python3

import sys
import os
import urllib.parse
import urllib.request

# Get directory name
args = sys.argv
if len(args) == 2:
    folder_name = args[1]
else:
    print("The script expects exactly one parameter - target directory name.")
    exit(1)

# Check if directory exists, if not create one
if os.path.exists(folder_name):
    if not os.path.isdir(folder_name):
        print("Name provided as argument refers to a file, not a directory!")
        exit(1)
else:
    os.mkdir(folder_name)
    print("Directory %s was created as it was not present." % folder_name)

# Now download files
links = ["https://files.digital.nhs.uk/publication/8/h/dem-diag-ind-phe-dec-2017.csv",
         "https://files.digital.nhs.uk/30/534FE0/dem-diag-ind-phe-Jun-2018.csv",
         "https://files.digital.nhs.uk/publicationimport/pub24xxx/pub24036/dem-diag-ind-phe-apr-2017.csv"]
for link in links:
    # create name for destination file...
    split_url = urllib.parse.urlsplit(link)
    file_name = split_url.path.split("/")[-1]
    if file_name[-4:] != ".csv":
        file_name += ".csv"
    file_name = os.path.join(folder_name, file_name)
    # there we could check if the file with this name exists and if it does,
    # we could ask user to abort/overwrite/rename, but let it just to overwrite...
    try:
        urllib.request.urlretrieve(link, file_name)
        print("File from %s saved to %s" % (link, file_name))
    except OSError as err:
        print("Download failed for link: %s" % link)
        print("Reason: {0}".format(err))





