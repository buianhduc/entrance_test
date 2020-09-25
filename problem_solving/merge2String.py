def merge2Strings(s1,s2):
    result = ""
    for i in range(min(len(s1),len(s2))):
        result += s1[i] + s2[i]
    if(len(s1) > len(s2)):
        result += s1[len(s2):len(s1)]
    elif(len(s1) < len(s2)):
        result += s2[len(s1):len(s2)]
    return result

print(merge2Strings("abcsda","0123"))