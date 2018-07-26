#!/usr/bin/env python3

import sys
import pandas as pd

# Get file name
args = sys.argv
if len(args) == 2:
    file_name = args[1]
else:
    print("The script expects exactly one parameter - name of file to be processed.")
    exit(1)

print(file_name)
data = pd.read_csv(file_name)
dementia = data[data.MEASURE == "DEMENTIA_REGISTER_65_PLUS"]
dementia = dementia.loc[:, ["NAME", "ACH_DATE", "MEASURE", "VALUE"]]
print(dementia)
# dementia.to_csv("folder/bla.csv")
