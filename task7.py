# https://edabit.com/challenge/Kh7Bm9X7Q4rYB8uT7

def is_vowel_sandwich(lst):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvxyzw"
    lst = lst.lower()
    res = ''
    for x in vowels:
        if len(lst) > 3:
            res = ("False")
        elif lst[0] in consonants and x == lst[1] and lst[-1] in consonants:
            res = ("True")
        else:
            res = ("False")
    return res


print(is_vowel_sandwich("ear"))