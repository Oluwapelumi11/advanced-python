import itertools

def testFunction(x):
    pass


def main():
    """main() --> None

        does nothing just checking
    """
    names= ['Faith','Solomon','Esther']

    # use the itertools cycle to iterate indefinitely on the collection
    # name = itertools.cycle(names)
    # print(next(name))
    # print(next(name))
    # print(next(name))
    # print(next(name))
    # print(next(name))
    # print(next(name))
    # print(next(name))
    # print(next(name))

    ## Nice work next use the count property to count numbers
    # number = itertools.count(100)
    # print(next(number))
    # print(next(number))
    # print(next(number))
    # print(next(number))

    #nice give it a step

    # stepnum = itertools.count(1,10)
    # print(next(stepnum))
    # print(next(stepnum))
    # print(next(stepnum))
    # print(next(stepnum))
    # print(next(stepnum))

    # now make use of the accumulator

    nums = [1,5,6,8,4,34,7,5,3,5,7,3,2]
    # acc = list(itertools.accumulate(nums))
    # print(acc)

    # change the behaviour of the accumulator to get the max value in the list
    # acc = list(itertools.accumulate(nums, max))
    # print(acc)

    # nice work faith!!

    # now use itertools chain to connect sequences together

    connected = list(itertools.chain("ASDFFGG"))
    print(connected)

    # now from my findings, i got that i can use the chain method
    # to turn strings into list in a smooth way... i think this is 
    # my new great syntax for string to list casting






if __name__=="__main__":
    print(main.__doc__)