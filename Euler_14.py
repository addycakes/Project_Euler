def collatz(num):
    global terms
    terms.append(num)

    if num == 1:
        return len(terms)
    elif num%2==0:
        return collatz(num/2)
    else:
        return collatz(3*num + 1)


def largest_termslist(x):
    sizes = {}
    for i in range(50, x):
        global terms
        terms = []
        sizes[collatz(i)] = i
    
    return sizes[max(sizes)]

print(largest_termslist(1000000))
