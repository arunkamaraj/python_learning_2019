import re
import email.utils
if __name__ == "__main__":
    pattern = "^([A-Za-z])([\w\-\.\_]+)@(\w+)\.(\w{1,3})$"
    for i in range(int(input())):
        name, mail = email.utils.parseaddr(input())
        if re.match(pattern, mail):
            print(email.utils.formataddr((name, mail)))
