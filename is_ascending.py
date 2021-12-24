def is_ascending(items):
    x=0
    while x<len(items)-1:
            if items[x]>=items[x+1]:
                return False
            x+=1
    return True