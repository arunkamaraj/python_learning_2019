def dynamicArray(n, queries):
    last_answer = 0
    seq_list = [[] for _ in range(n)]

    for q in queries:
        idx = (q[1] ^ last_answer) % n
        if q[0] == 1:
            seq_list[idx].append(q[2])
        elif q[0] == 2:
            tmp_list = seq_list[idx]
            last_answer = tmp_list[q[2] % len(tmp_list)]
            print (last_answer)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    dynamicArray(n, queries)
