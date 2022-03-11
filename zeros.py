number = input("n: ")
n = 0
while number.startswith("0"):
    n += 1
    number = number[1:]
        #number = int(number)
print(f"número de zeros = {n}")

#while number == "0":
#while number[0] == "0":
