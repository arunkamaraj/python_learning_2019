class sample:
    arun= 10

class myclass(sample):
    sample.arun=50

print(myclass.arun)
print(sample.arun)
