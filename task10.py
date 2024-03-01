# https://edabit.com/challenge/Ddmh9KYg7xA4m9uE7

def convert_binary(lst):
    res = ""
    for x in lst.lower():
        if x in "abcdefghijklm":
            res += "0"
        else:
            res += "1"
    return res


print(convert_binary("house"))