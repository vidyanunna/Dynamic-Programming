#i/p=bbbab o/p =4 explanation:bbbb
s=input()
n=len(s)
rev=s[::-1] #reverse the string
dp=[[0 for _ in range(n+1)] for _ in range(n+1)] #Creating a 2D array 6*6 matrix 
#here there are 5 char in string and we are taking 6 to take empty string
for i in range(1,n+1):
    for j in range(1,n+1): #to understand this ref how dp table works?
        if s[i-1]==rev[j-1]: # if char in s matches with char of rev(s)
            dp[i][j]=1+dp[i-1][j-1] #increment +1 of the top left diagonal value
        else: #if not matches
            dp[i][j]=max(dp[i-1][j],dp[i][j-1]) # take max value from the top or left of the value in dp table 
print(dp[n][n])