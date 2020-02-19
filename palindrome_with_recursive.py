def check_palindrome(data):
    if len(data) <= 1:
        return True
    else:
        return (data[0] == data[-1]) and check_palindrome(data[1:-1])

if __name__ == "__main__":
    test = ['kayak',
            'aibohphobia',
            'Live not on evil',
            'Reviled did I live, said I, as evil I did deliver',

            'Go hang a salami; I’m a lasagna hog.',
            'Able was I ere I saw Elba',
            'Kanakanak – a town in Alaska',
            'Wassamassaw – a town in South Dakota'
            ]
    for i in test:
        clean_data = ''.join(e for e in i if e.isalnum())
        print(i + ' : ', check_palindrome(clean_data.lower()))