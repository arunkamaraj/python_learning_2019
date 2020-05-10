
if __name__ == "__main__":
    student, subject = list(map(int, input().split()))
    sub_marks = [list(map(float, input().split())) for i in range(subject)]
    for i in zip(*sub_marks):
        print(sum(i)/subject, end='\n')
