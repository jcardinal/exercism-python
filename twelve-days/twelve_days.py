def recite(start_verse, end_verse):
    twelve_days = {
        1: ["first", "a Partridge in a Pear Tree"],
        2: ["second", "two Turtle Doves"],
        3: ["third", "three French Hens"],
        4: ["fourth", "four Calling Birds"],
        5: ["fifth", "five Gold Rings"],
        6: ["sixth", "six Geese-a-Laying"],
        7: ["seventh", "seven Swans-a-Swimming"],
        8: ["eighth", "eight Maids-a-Milking"],
        9: ["ninth", "nine Ladies Dancing"],
        10: ["tenth", "ten Lords-a-Leaping"],
        11: ["eleventh", "eleven Pipers Piping"],
        12: ["twelfth", "twelve Drummers Drumming"],
    }
    verses = []
    current_verse = start_verse
    while current_verse <= end_verse:
        if current_verse == 1:
            verse = (
                "On the "
                + twelve_days[current_verse][0]
                + " day of Christmas my true love gave to me: "
                + twelve_days[current_verse][1]
                + "."
            )
        else:
            verse = (
                "On the "
                + twelve_days[current_verse][0]
                + " day of Christmas my true love gave to me: "
            )
            day = current_verse
            while day > 1:
                verse += twelve_days[day][1] + ", "
                day -= 1
            verse += "and " + twelve_days[1][1] + "."
        verses.append(verse)
        current_verse += 1

    return verses
