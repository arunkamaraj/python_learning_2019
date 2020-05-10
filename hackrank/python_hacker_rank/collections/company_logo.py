import collections

if __name__ == "__main__":
    raw_data = input().strip()
    data = raw_data.lower()
    if 3 < len(data) <= 10000:
        collected_data = collections.Counter(data)
        three_common = collected_data.most_common()
        sorted_data = sorted(three_common, key=lambda x: (-x[1], x[0]))
        for i, j in sorted_data[:3]:
            print(i, j, sep=' ')
