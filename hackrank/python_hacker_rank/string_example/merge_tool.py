# def merge_the_tools(string, k):
#     if len(string) >= k and len(string) % k == 0:
#         splited_data = []
#         a = 0
#         b = k
#         while b <= len(string):
#             splited_data.append(string[a:b])
#             a = b
#             b += k
#
#         for i in splited_data:
#             no_dup = []
#             for j in [*i]:
#                 if j not in no_dup:
#                     no_dup.append(j)
#             print(''.join([*no_dup]))
#
#
#             # print(i, set([*i]))
#             # print(''.join(set([*i])))

def merge_the_tools(S, N):
    for part in zip(*[iter(S)] * N):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in part if c not in d]))


# [d.append(c) for c in ('A','A', 'C') if c not in d]
# [None, None]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
