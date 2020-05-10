from html.parser import HTMLParser

class myClass(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            print(*["-> " + name + " > " + str(value) for name, value in attrs], sep="\n")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            print(*["-> " + name + " > " + str(value) for name, value in attrs], sep="\n")


if __name__ == "__main__":
    m = myClass()
    html_data = ''.join([input() for i in range(int(input()))])
    m.feed(data=html_data)

