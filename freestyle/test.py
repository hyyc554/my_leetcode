def diff(listA,listB):
    #求交集的两种方式
    retA = [i for i in listA if i in listB]
    retB = list(set(listA).intersection(set(listB)))
    print(retA)
    print(retB)

a = [1,2,4,3,1]
b = [1,1,3]
diff(a,b)