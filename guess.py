import random
a = int(input("enter the lower bound:"))
b = int(input("enter the upper bound:"))
rastgele = random.randint(a,b)
while True:
    tahmin = int(input("Take a guess:"))
    if tahmin == rastgele:
            print("*****************")
            print("!!GOT IT!!")
            print("*****************")
            break
    elif tahmin < rastgele:
        print("bigger")
        print("*****************")
    elif tahmin > rastgele:
        print("smaller")
        print("*****************")
print("££££££££££££££££££££££££££££££££££££££££££££")
print("new feature added")
