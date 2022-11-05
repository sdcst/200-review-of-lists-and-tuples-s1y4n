#!python3


def getIntegers(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the integers to the new list
    integers = [i for i in myList if isinstance(i, (int))]
    return integers

    
def getFactor(myList,factor):
    # myList : expected list or tuple
    # factor : integer
    # iterate through the list and add the number to the list if
    # it is a factor of the number
    factors = [i for i in myList if int(i/factor) == i/factor]
    return factors

def getNegatives(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the negative numbers to the new list
    negatives = [i for i in myList if i < 0]
    return negatives

def getIntersection(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a list of numbers that is in both lists
    # the intersection of the 2 number sets
    common = list(set(list1).intersection(list2))
    return common

def getUnion(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a list of numbers that is in either of the lists
    # the union of the 2 number sets
    union = list(set(list1).union(list2))
    return union   

def getMerge(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # add the elements of list2 into list1
    # if the list2 element is in list1, add it at the position where it occurs in list1
    # if the list2 element is not in list1, add it to the end
    merge = list1.copy()
    
    #add it to the index origin?
    count = 0
    for i in list2:
        if i in list1:
            count += 1
            merge.insert(list1.index(i)+ count, i)
        else:
            merge.append(i)
    return merge

def main():
    easy1 = [5,10,15,2,4,6,8]
    easy2 = [-2,-4,-6,2,4,6,0.1]
    numbers1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
    numbers2 = [3,7,11,15,19,23,27,31,35,39,44,50]
    print(getIntegers(numbers1))
    print(getFactor(easy2,2))
    print(getIntersection(easy1,easy2))
    print(getNegatives(easy2))
    print(getUnion(easy1,easy2))
    print(getMerge(easy1,easy2))

if __name__ == "__main__":
    main()