# Enter your code here. Read input from STDIN. Print output to STDOUT
def draw_line(l, m):
    mat_design = '.|.' * l
    print(mat_design.center(m, '-'))


def draw_mat(n, m):
    j = 0
    for i in range(1, n + 1):
        if i <= n // 2:
            line = (j * 2) + 1
            draw_line(line, m)
            j += 1
        elif i == (n // 2 + 1):
            print('WELCOME'.center(m, '-'))
            j -= 1
        elif i > (n // 2 + 1):
            line = (j * 2) + 1
            draw_line(line, m)
            j -= 1


if __name__ == "__main__":
    n, m = tuple(map(int, input().split()))
    draw_mat(n, m)
