for n in range(1,101):
    if n % 3 == 0:
        if n % 5 == 0:
            print("FB")
        else:
            print("F")
    elif n % 5 == 0:
        print("B")
    else:
        print(n)

