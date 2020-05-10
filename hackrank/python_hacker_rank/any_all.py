if __name__ == "__main__":

    n_list = input().split()
    print(

        all([int(i) >= 0 for i in n_list]) and any([i == i[::-1] for i in n_list])

    )
