from collections import OrderedDict

if __name__ == "__main__":
    od = OrderedDict()
    for _ in range(int(input())):
        prod, val = input().rsplit(' ', 1)
        if prod in od:
            od[prod] = od[prod] + int(val)
        else:
            od[prod] = int(val)

    for k,v in od.items():
        print("{} {}".format(k, v))
