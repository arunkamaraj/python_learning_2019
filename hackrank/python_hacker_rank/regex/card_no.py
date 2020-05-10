import re
pattren  = '(^[4|5|6])(?!\\1{3,})\\d{3}-?(((\\d)(?!\\4{3,})){4}-?){2}(((\\d)(?!\\7{3,})){4})$'
consective_pattren = '(\d)\\1{3,}'
if __name__ == "__main__":
    n = int(input())
    card_no = [input() for i in range(n)]

    for no in card_no:
        if not re.search(consective_pattren, no.replace('-', '')) and re.match(pattren, no):
            print('Valid')
        else:
            print('Invalid')