
def create_al_rangloi(no, size, output):
    l = [chr(96+i) for i in range(size, size - (no//2)-1, -1)]
    if len(l) > 1:
        l.extend(reversed(l[:-1]))

    output.append(l)

def print_rangoli(size):
    output = []
    for i in range(size):
        no = (i * 2) + 1
        create_al_rangloi(no, size, output)

    output.extend(reversed(output[:-1]))
    width = ((n - 1) * 2 + 1) + (n - 1) * 2
    for i in output:
        print('-'.join(i).center(width, '-'))

if __name__ == '__main__':

    n = int(input())
    print_rangoli(n)

