from html.parser import HTMLParser


class Myhtmlparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            print(*["-> " + name + " > " + str(value) for name, value in attrs], sep="\n")


def get_html():
    data = '\n'.join([input() for i in range(int(input()))])
    return data

    
if __name__ == "__main__":
    html_data = get_html()
    m = Myhtmlparser()
    m.feed(data=html_data)
    m.close()
