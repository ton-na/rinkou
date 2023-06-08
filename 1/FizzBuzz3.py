def FizzBuzz(i):
    return 'F'*(not i%3) + 'B'*(not i%5) or str(i)

print('\n'.join(list(map(FizzBuzz, list(range(1, 101))))))