def reverse_str(data):

    if len(data) <= 1:
        return data
    else:
        return data[-1] + reverse_str(data[:-1])


if __name__ == "__main__":
    print(reverse_str('Tanvi'))