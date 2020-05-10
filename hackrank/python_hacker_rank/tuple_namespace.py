from collections import namedtuple

if __name__ == "__main__":
    (n, categories) = (int(input()), input().split())
    Grade = namedtuple('Grade', categories)
    marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
    print((sum(marks) / len(marks)))
