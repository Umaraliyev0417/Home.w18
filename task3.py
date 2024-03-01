# https://edabit.com/challenge/f6LeKowjWQHm5637D

def cap_to_front(lst):
    upper = ""
    lower = ""
    for x in lst:
        if x.isupper():
            upper += x
        elif x.islower():
            lower += x
    res = ''.join(upper + lower)
    return res


print(cap_to_front("shOrtCAKE"))