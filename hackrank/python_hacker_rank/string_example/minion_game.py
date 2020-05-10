# def minion_game(string):
#     if string.isalpha() and 0 < len(string) <= 1000000:
#         data = string.upper()
#         stuart_score = 0
#         kevin_score = 0
#         vowels = 'AEIOU'
#         start = 0
#         while start <= len(data) - 1:
#             for i in range(start + 1, len(data) + 1):
#                 sub_str = data[start:i]
#                 if sub_str[0] not in vowels:
#                     stuart_score += 1
#                 elif sub_str[0] in vowels:
#                     kevin_score += 1
#             start += 1
#
#         if stuart_score > kevin_score:
#             print("Stuart " + str(stuart_score))
#         elif stuart_score < kevin_score:
#             print("Kevin " + str(kevin_score))
#         elif stuart_score == kevin_score:
#             print("Draw")


def minion_game(string):
    if string.isalpha() and 0 < len(string) <= 1000000:
        data = string.upper()
        stuart_score = 0
        kevin_score = 0
        vowels = 'AEIOU'

        for i in range(len(data)):
            if data[i] not in vowels:
                stuart_score += len(data) - i
            else:
                kevin_score += len(data) - i

        if stuart_score > kevin_score:
            print("Stuart " + str(stuart_score))
        elif stuart_score < kevin_score:
            print("Kevin " + str(kevin_score))
        elif stuart_score == kevin_score:
            print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
