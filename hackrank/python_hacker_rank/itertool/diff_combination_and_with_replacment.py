import itertools
for i in itertools.combinations_with_replacement([1, 2, 3], 2):
    print (i)

print("-----------")

for i in itertools.combinations([1, 2, 3], 2):
    print (i)