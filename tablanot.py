def NOT(a):
    return int(not a)

print("tabla de verdad NOT")
print("A | NOT A")

for A in [0,1]:
    print(A, "|", NOT(A))