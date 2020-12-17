

def find_mod():
    while True:
        number = int(input("Number: "))
        modu = int(input("Modular: "))
        print(f"Result: {number % modu} \n\n")


multiple = 13
mod = 19
remainer = 4
index = 1
while True:
    multiple = index * multiple
    print(f"{multiple}, {index}")
    print(multiple % mod)
    if multiple % mod == 1:
        print(index)
        break
    index += 1
    input("")
