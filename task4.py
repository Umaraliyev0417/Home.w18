# https://edabit.com/challenge/vqMFpARj3DvELLDmZ

def letters_only(lst):
    res = ''
    for x in lst:
        if x.isalpha():
            res += x

    return res


print(letters_only("R!=:~0o0./c&}9k`60=y"))