# print('\n'.join(list(map(lambda i : 'Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i), list(range(1, 101))))))
# print('\n'.join(list(map(lambda i : 'Fizz'*not(int(str(i/3).split('.')[1])) + 'Buzz'*not(int(str(i/5).split('.')[1])) or str(i), list(range(1, 101))))))
# print(('' if i % 3 else 'Fizz') + ('' if i % 5 else 'Buzz') or i)
# print('\n'.join(list(map(lambda i : ('' if str(i/3).split('.')[1] else 'Fizz') + ('' if str(i/5).split('.')[1] else 'Buzz') or str(i), list(range(1, 101))))))
print('\n'.join(list(map(lambda i: 'FizzBuzz'[i not in list(range(3, 101, 3)) and 4:i not in list(range(5, 101, 5)) and 4 or 8] or str(i), list(range(1, 101))))))