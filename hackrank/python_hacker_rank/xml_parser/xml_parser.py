import xml.etree.ElementTree as etree
import sys


def get_attr_number(root):
    count = 0
    count += len(root.attrib)
    if len(root):
        for child in root:
            count += get_attr_number(child)
        return count
    else:
        return count


if __name__ == "__main__":
    # sys.stdin.readline()
    # xml = sys.stdin.read()

    xml_1 ="""
        <feed xml:lang='en'>
          <title>HackerRank</title>
          <subtitle lang='en'>Programming challenges</subtitle>
          <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
          <updated>2013-12-25T12:00:00</updated>
          <entry>
            <author gender='male'>Harsh</author>
            <question type='hard'>XML 1</question>
            <description type='text'>This is related to XML parsing</description>
          </entry>
        </feed>"""

    xml = """
    <feed xml:lang='en'>
        <title>HackerRank</title>
        <subtitle lang='en'>Programming challenges</subtitle>
        <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
        <updated>2013-12-25T12:00:00</updated>
    </feed>
    """
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
