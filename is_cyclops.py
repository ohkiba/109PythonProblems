def is_cyclops(n):
    nStr=str(n)
    count=0
    if len(nStr)%2!=0:
        if int(nStr[len(nStr)//2])==0:
            for x in range (len(nStr)):
                num=int(nStr[x])
                if num==0:
                    count+=1
    return count==1