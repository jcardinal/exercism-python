def is_isogram(string):
    letters = [x.lower() for x in string if x != " " if x != "-"]
    letters.sort()
    no_repeats_found = True
    for i in range(len(letters) - 1):
        if letters[i] == letters[i + 1]:
            no_repeats_found = False
            break

    return no_repeats_found