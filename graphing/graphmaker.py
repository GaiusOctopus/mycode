#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | Graphing """

import numpy as np
import matplotlib.pyplot as plt



fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

party_affiliation = ["1435 Republican",
                     "1287 Democratic",
                     "1401 Other",
                     "33 Libertarian"]

data = [float(x.split()[0]) for x in party_affiliation ]
demographics = [x.split()[-1] for x in party_affiliation]


def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d} K)".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, demographics,
          title="Party Affiliation",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Arizona Voter Registration Statistics: August 2022 ")

plt.savefig("/home/student/mycode/graphmaker.png")
plt.savefig("/home/student/static/graphmaker.png")
