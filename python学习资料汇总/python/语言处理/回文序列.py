def longestPalindrome(s):
    i=1
    a=[0,0]
    longestPalindrome=""
    while i<len(s):
        j=0
        while j<=i and i+j<=len(s)-1:
            if s[i-j]==s[i+j]:
                j+=1
                print('out',i,j)
                if i-j<0 or i+j>len(s)-1:
                    print('in',i,j)
                    j-=1
                    break
            else:
                j-=1
                break

        if j>a[1]:
            a[0]=i
            a[1]=j

        i+=1
    return a


s='acdefefbahabchghu'
a=longestPalindrome(s)
i,j=a[0],a[1]
print(a)
print(s[i-j:i+j+1])

