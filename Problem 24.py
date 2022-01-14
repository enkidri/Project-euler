from itertools import permutations

digits = '0123456789'
permList = permutations(digits)

index = 1000000
answer = ''
permList = list(permList)
for digit in permList[index-1]:
    answer += digit

print(f'The answer is {answer}')
