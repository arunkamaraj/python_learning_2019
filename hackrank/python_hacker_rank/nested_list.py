if __name__ == '__main__':
    data = []
    s = set()
    second_min_name = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])
        s.add(score)

    second_min_score = list(sorted(s))[1]

    print('\n'.join(sorted([detail[0]for detail in data if detail[1] == second_min_score])))






