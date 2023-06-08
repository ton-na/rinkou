import random

input1 = list('268668743807663281359259975924239968838915518781704591221216502144648297573337534154488714432458672010933572906012936272617155562367959865483138529186273117849466634478519408432309577699417')

numbers = [i for i in range(1, 100)]
while 1:
    random.shuffle(numbers)
    result = ''.join(map(str, numbers))
    result_list = list(result)
    count = 0

    for i, j in zip(result_list, input1):
        if i != j:
            break
        else:
            count += 1
            if count == 189:
                print(numbers)
                break
    if count == 189:
        break