#  https://edabit.com/challenge/yXekCk3qRWYR5AHif

def vow_replace(lst, letter):
    vowels = ["a", "e", "i", "o", "u"]
    for x in lst:
        if x in vowels:
            lst = lst.replace(x, letter)

    return lst


print(vow_replace("apples and bananas", "u"))