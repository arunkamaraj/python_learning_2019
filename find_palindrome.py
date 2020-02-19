# check palindrome
import my_abstract_pack.abstract_pack as abstarct_type

def check_palindrome(data):

    deque = abstarct_type.Deque()

    for ch in data:
        deque.rear_add(ch)

    is_palindrome = True

    while deque.size() > 1 and is_palindrome:
        first_ch = deque.front_remove()
        last_ch = deque.rear_remove()

        if first_ch != last_ch:
            is_palindrome = False

    return is_palindrome

if __name__ == '__main__':
    print(check_palindrome('arun'))
    print (check_palindrome('madam'))
    print (check_palindrome('maddam'))