for i in range(1, 101):
    if i in list(range(0, 101, 15)): # 15飛びでFizzBuzzを表示
        print('FB')
    elif i in list(range(0, 101, 3)): # 3飛びでFizzを表示
        print('F')
    elif i in list(range(0, 101, 5)): # 5飛びでBuzzを表示
        print('B')
    else:
        print(i)