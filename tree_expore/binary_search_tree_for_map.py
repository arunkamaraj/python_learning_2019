import my_abstract_pack.abstract_pack as ap

def experiment_put_functionality(bst_obj):
    for i in [15,7,43,13,19,87]:
        bst_obj[i] =''

    bst_obj[17] = ''
    print(bst_obj.length())
    # print(bst_obj)

def experiment_get_functionality(bst_obj):
    result = bst_obj.get(17)
    print (result)

if __name__ == '__main__':
    bst = ap.BinarySearchTree()
    experiment_put_functionality(bst)
    # experiment_get_functionality(bst)
    bst.delete(19)
    print(bst)


