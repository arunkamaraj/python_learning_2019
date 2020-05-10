import re
def fun(s):
    # return True if s is a valid email, else return False
    pattern = '^[A-Za-z0-9-_]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
    #here ^ and $ is important
    return bool(re.search(pattern, s))

def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
