srt = 3
lenPatTot = 0

for nr in range(2, 10+1):
    number = 1/ nr
    number = str(number)
    print(number)
    if len(number) >= 18:
        while True:
            pattern = number[2:srt]
            lenPat = len(pattern)
            nextPat = number[srt: srt + lenPat]
            if pattern == nextPat:
                if lenPat > lenPatTot:
                    finVal = nr
                    finPattern = pattern
                    lenTotPat = lenPat
                    break
                else:
                    break
            else:
                srt += 1
    else:
        continue
print(lenPat, pattern)



