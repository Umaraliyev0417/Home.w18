# https://edabit.com/challenge/4Y5Zk5f9LckvWjFf3

def special_reverse(lst, letter):
    l = lst.split()
    for i in range(len(l)):
        if l[i][0] == letter:
            l[i] = l[i][::-1]
    lst = " ".join(l)
    return lst

print(special_reverse("word searches are super fun", "s"))