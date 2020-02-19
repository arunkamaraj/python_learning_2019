def decimal_to_other_base(decimal_data, base_info):
    convert_to_string ="0123456789ABCDEFGHIJKLAMNOPQRSTUVWXYZ"

    if decimal_data < base_info:
        return str(decimal_data)
    else:

        return decimal_to_other_base(decimal_data// base_info, base_info) + convert_to_string[decimal_data % base_info]

if __name__ == "__main__":
    print(decimal_to_other_base(769, 10))