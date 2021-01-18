I learned list comprehensions today, so that was my new hammer and this exercise provided a nail.

A [popular solution](https://exercism.io/tracks/python/exercises/isogram/solutions/e11643dfde5740e1a078982b6ca2890f) cleans the input by removing spaces and hyphens and lower-casing everything, then uses python sets to compare the length of the set of the string to the length of the string. I like it. Another solution uses `.isalpha` to strip the spaces and hyphens instead of specifying each manually.

```
def is_isogram(string):
    string = string.lower().replace(' ', '').replace('-', '')

    return len(string) == len(set(string))
```
