

def comDiv(a, b):
    if (a == b):
        return a
    if (a>b):
        return comDiv(a-b, b)
    else:
        return comDiv(a, b-a)

print(comDiv(100,10))
print(comDiv(21,294))
print(comDiv(16,28))
print(comDiv(31,7))

