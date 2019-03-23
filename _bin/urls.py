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

if __name__ == "__main__":
    print(
        "\n".join(
            ["https://jamesandrosie.wedding/d/{}".format(guest) for guest in guests]
        )
    )
