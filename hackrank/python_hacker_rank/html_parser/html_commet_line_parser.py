from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment", data, sep='\n')
        else:
            print(">>> Single-line Comment", data, sep='\n')

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data ", data, sep='\n')


def get_html():
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    return html


if __name__ == "__main__":
    html_data = get_html()
    parser = MyHTMLParser()
    parser.feed(html_data)
    parser.close()


