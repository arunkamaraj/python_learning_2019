import re
if __name__ == "__main__":
    n = int(input())
    pattern = r"^[789]\d{9}$"

    data = [input() for _ in range(n)]

    print("\n".join(["YES" if re.search(pattern, ph) else "NO" for ph in data]))


