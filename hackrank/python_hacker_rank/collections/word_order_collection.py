import collections

if __name__ == "__main__":
    n = int(input())
    words = [input().strip() for i in range(n)]
    collection_process = collections.Counter(words)
    print(len(collection_process))
    print(*collection_process.values())