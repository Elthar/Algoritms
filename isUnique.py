def is_unique(s):
    l = len(s)
    for i in range(l):
        for j in range(i+1, l):
            if s[i] == s[j]:
                return False 
    return True

print(is_unique([1,2,3,4,2]))
