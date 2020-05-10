if __name__ == "__main__":
    n = int(input())
    room_list = list(map(int, input().split()))

    room_set = set(room_list)
    captain = [i for i in room_set if room_list.count(i) == 1 ][0]
    print(captain)
