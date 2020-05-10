import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level = level + 1
    child = list(elem)
    if child:
        for c in child:
            temp_depth = depth(c, level)
            if temp_depth > maxdepth:
                maxdepth = temp_depth
        return maxdepth
    else:
        return level

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)