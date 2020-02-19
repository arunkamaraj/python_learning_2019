import my_abstract_pack.abstract_pack as ap

if __name__ == '__main__':
    hash_table = ap.Map(size=11)
    
    hash_table[54] = "cat"
    hash_table[26] = "dog"
    hash_table[93] = "lion"
    hash_table[17] = "tiger"
    hash_table[77] = "bird"
    hash_table[31] = "cow"
    hash_table[44] = "goat"
    hash_table[55] = "pig"
    hash_table[20] = "chicken"

    print (hash_table.keyInfo)
    print (hash_table.dataInfo)

    print(hash_table[55])

