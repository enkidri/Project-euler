
fibList = [1, 1]

while True:
    nextFib = fibList[-1] + fibList[-2]
    if len(str(nextFib)) >= 1000:
        break
    else:
        fibList.append(nextFib)

finalAnswer = len(fibList) + 1
print(f'Final answer is {finalAnswer}')
