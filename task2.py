# https://edabit.com/challenge/a55ygB8Bwj9tx6Hym

def steps_to_convert(lst):
    upper = 0
    lower = 0
    for x in lst:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1

    return min(upper, lower)


print(steps_to_convert("abCBA"))