# https://edabit.com/challenge/e8TFAMbTTaEr7JSgd

def left_digit(lst):
    for x in lst:
        if x.isdigit():
            return x


print(left_digit("TrAdE2W1n95!"))