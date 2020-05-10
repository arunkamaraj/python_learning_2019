if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if 2 <= n <= 10 and max(scores) <= 100 and min(scores) >= 0:
        avg = round(sum(student_marks[query_name]) / 3, 2)
        print(avg)
        print("{:.2f}".format(avg))
