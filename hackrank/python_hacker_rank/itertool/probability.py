import itertools

if __name__ == "__main__":
    n = int(input())
    data = input().strip().split()
    k = int(input())

    combination_data = [*itertools.combinations(data, k)]
    possible_choice = [i for i in combination_data if 'a' in i]

    print(round(len(possible_choice)/len(combination_data), 4))