#!/usr/bin/env python3

import os
import pandas as pd
import matplotlib.pyplot as plt

# Showing just how the graph was created, csv files are in directory "folder"
dirname = "folder"
frames = []

for file in os.listdir(dirname):
    if file[-4:] == ".csv":
        data = pd.read_csv(os.path.join(dirname, file),
                           parse_dates=['ACH_DATE'],
                           date_parser=lambda x: pd.to_datetime(x, format='%d%b%Y'))
        # there are mixed levels of administrative units, so I chose first one (CC - ceremonial counties...)
        dementia = data[(data.MEASURE == "DEMENTIA_REGISTER_65_PLUS") & (data.ORG_TYPE == "CC")]
        dementia = dementia.loc[:, ["NAME", "ACH_DATE", "MEASURE", "VALUE"]]
        frames.append(dementia)

merged = frames[0]
merged = merged.append(frames[1:], ignore_index=True).drop_duplicates().reset_index(drop=True)
merged = merged.groupby(["ACH_DATE"])["VALUE"].sum()  # it is also sorted by date then
ax = merged.plot(title="Development of dementia")
ax.set_xlabel("Date")
ax.set_ylabel("Count of people")
plt.show()
