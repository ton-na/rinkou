x = int(input())
if x == 2:
    print("Yes")
for n in range(2,x):
    if x % n != 0: # 23 % 10 = 3
        if n != x-1:
            continue
        print("Yes")
    elif x % n == 0: # 23 % 23 = 0
        print("No")
        break
