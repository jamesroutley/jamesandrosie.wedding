import json
import sys
import os

guests = [
    "sarah",
    "yesmin",
    "lexi",
    "will-carenza",
    "jamie-julia",
    "tammy",
    "hannibal-imo",
    "hal",
    "ibaad-thea",
    "celia",
    "laurie-jemima",
    "edward",
    "alex",
    "camilla",
    "caspar",
    "laura",
    "kourosh-tom",
    "masha",
    "michael",
    "natalya",
    "tumi",
    "angus",
    "erin",
    "rachel",
    "kevin",
    "raman",
    "olivia",
    "lucy",
    "richard-tori",
    "jez",
    "sophie",
    "harry-yasmine",
    "jonathan-guest",
    "jessica-jake",
]

template = """---
title: "Save the date"
date: 2019-03-05T00:00:00Z
names: "{}"
id: "{}"
---
"""


def get_names(raw):
    ns = raw.split("-")
    names = ""
    if len(ns) == 1:
        return ns[0].capitalize()
    return "{} & {}".format(ns[0].capitalize(), ns[1].capitalize())


if __name__ == "__main__":
    dirname = sys.argv[1]
    os.mkdir(dirname)

    for guest in guests:
        filename = os.path.join(dirname, guest + ".md")
        names = get_names(guest)
        with open(filename, "w") as f:
            f.write(template.format(names, guest))
