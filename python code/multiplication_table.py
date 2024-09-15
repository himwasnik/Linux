def table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

num = int(input("enter number: "))
print(f"multiplication table of {num}:")
table(num)
