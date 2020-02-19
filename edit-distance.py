def find_edit_distance(str1, str2):
    str1_length = len(str1)
    str2_length = len(str2)
    dp = [[0 for _ in range(str2_length+1)] for _ in range(str1_length+1)]

    print (dp)

    for i in range(str1_length+1):
        for j in range(str2_length+1):
            # case 1 starting corner
            if i == j == 0:
                dp[i][j] = 0

            # case 2 first row for null
            elif i == 0:
                dp[i][j] = dp[i][j-1] + 1

            # case 3 first column for null
            elif j == 0:
                dp[i][j] = dp[i-1][j] + 1

            # case 4 for equal char
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            #case 5 for not equal char
            else:
                dp[i][j] = 1+ min(dp[i][j-1],
                                  dp[i-1][j],
                                  dp[i-1][j-1])

    print (dp[str1_length][str2_length])

if __name__ == '__main__':
    str1 = "adc"
    str2 = "ab"

    find_edit_distance(str1, str2)