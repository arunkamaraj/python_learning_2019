import re

if __name__ == "__main__":
    for i in range(int(input())):
        sorted_p = ''.join(sorted(input()))
        l = all([bool(re.search("[A-Z]{2,}", sorted_p)),
             bool(re.search("[0-9]{3,}", sorted_p)),
             bool(re.search("[a-zA-Z0-9]{10}", sorted_p)),
             not bool(re.search(r"(.)\1", sorted_p))])

        print('Valid' if l else 'InValid')
