def AND(a,b):
    return int(a and b) 

def OR(a,b):
    return int(a or b)

def NOT(a):
    return int(not a)

print("tabla de verdad OR")
print("A B | A OR B")
for A in [0, 1]:
    for B in [0,1]:
        print(A, B, "|", OR(A,B))