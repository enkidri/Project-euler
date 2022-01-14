for a in range(1,501):
    for b in range(1,251):
        #b=500-bNr
        c=1000-a-b
        if (a**2)+(b**2)==(c**2):
            finalValue=a*b*c
            print('The answer is ',finalValue)

