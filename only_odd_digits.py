def only_odd_digits(n):
    nStr=str(n)
    count=0
    for x in range (len(nStr)):
        num=int(nStr[x])
        if num%2!=0:
            count+=1

    return count==len(nStr)
