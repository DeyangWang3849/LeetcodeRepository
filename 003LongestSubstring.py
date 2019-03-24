def lengthOfLongestSubstring(s:str):
    diction = {}
    lenList = []
    if s == '':
        return 0
    diction[s[0]]=0
    lenList.append(1)

    for i in range(1,len(s)):
        if diction.__contains__(s[i]):
            lenList.append(min(i - diction[s[i]],lenList[i-1]+1))
            diction[s[i]]=i
        else:
            diction[s[i]]=i
            lenList.append(lenList[i-1]+1)
    return max(lenList)

if __name__ == '__main__':
    while True:
        string = input('please input string:\n')
        print(lengthOfLongestSubstring(string))
