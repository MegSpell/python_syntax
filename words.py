def print_upper_words(words):
    """Print each word on sep line, uppercased.

        ex: print_upper_words(["Meghan", "is", "a", "GENIUS"])
        MEGHAN
        IS
        A
        GENIUS
    """

    for word in words:
        print(word.upper())

###In [15]: print_upper_words(["elephant", "Exciting", "AMAZING", "meghan"])
###ELEPHANT
###EXCITING
###AMAZING
###MEGHAN


def print_upper_words2(words):
    """Print each word on sep line, uppercased, if starts with E or e.

        ex: print_upper_words2(["elephant", "Meghan", "Exciting"])
        ELEPHANT
        EXCITING
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

###In [16]: print_upper_words2(["elephant", "Meghan", "Exciting"])
###ELEPHANT
###EXCITING


def print_upper_words3(words, must_start_with):
    """Print each word on separate line, uppercased, if starts with one of given

        ex: print_upper_words3(["elephant", "Exciting", "AMAZING", "meghan"],      must_start_with=["A", "E"])
        EXCITING
        AMAZING
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

###In [17]: print_upper_words3(["elephant", "Exciting", "AMAZING", "meghan"],
###    ...: must_start_with=["A", "E"])
###EXCITING
###AMAZING

###In [18]: print_upper_words3(["elephant", "Exciting", "AMAZING", "meghan"],
###    ...: must_start_with=["A", "E", "e"])
###ELEPHANT
###EXCITING
###AMAZING