Saw [this solution](https://exercism.io/tracks/python/exercises/luhn/solutions/3994d3717e134d3bab18565c0bd1ca46), which did a couple things I found clever.

1. In the step for converting the raw string into a list of digits, they reversed the list to avoid awkwardly processing digits backward from the right, and they wrapped this step in a `try` block where they also try casting each character to an `int` (including logic to skip spaces). If this fails, they know they've received invalid characters and thus the card number is invalid.

2. Used some list-creation logic I've seen before but still don't know the name of the approach or the intricacies of how it works:
   `digits = [int(x) for x in card_num[::-1] if x != ' ']`
   It appears to be something along the lines of
   `[function(x) for x in iterable if x satisfies conditional]`

   Found them! They're called [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
