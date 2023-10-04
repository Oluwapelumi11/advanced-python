def main():
    nums =[1,2,3,4,5,6,7,7,8,4,2,4,5,6]
    chars =['a','F','d','g','T','v','A']
    grades = [56,78,23,90,78,98,78,79,54]


    def filterFunc1(x):
        if x %2 == 0:
            return False
        return True

    def filterFunc2(x):
        if x.isupper():
            return True
        return False

    def squareFunc(x):
        return x**2
        

    def toGrade(x):
        if x >= 90:
            return "A"
        elif x >= 80:
            return "B"
        elif x >= 70:
            return "C"
        elif x >= 60:
            return "D"
        elif x  >= 50:
            return "E"
        return "F"

    # now let me filter out the odd numbers
    # odd  = list(filter(filterFunc1,nums))
    # print(odd)

    # # cool now filter out the uppercase letters

    # upper=list(filter(filterFunc2, chars))
    # print(upper)

    # # great work faith, now find the squares of each number in the collection
    
    # squares = list(map(squareFunc,nums))
    # print(squares)

    # fantastic now finally work up the grades collection to give out its grades in letters
    grades =sorted(grades)
    grade = list(map(toGrade,grades))
    print(grade)

    # great work faith, just do well to assign the scores

    for score in zip(grades,grade):
        print(score[0], "===>",score[1])







if __name__=="__main__":
    main()