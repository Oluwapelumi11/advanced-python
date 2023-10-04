def main():
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    days_yoruba = ['Aiku','Aje','Isegun','Ojoru','Ojobo','Eti','Abameta']
    # print(days)
    # for i in days:
    #     print(i)

    #now let me make an iterator with the days collection

    # day = iter(days)
    # print(next(day))
    # print(next(day))
    # print(next(day))
    # print(next(day))
    # print(next(day))

    # next get and read values from a text file

    # with open('iteration.txt','r') as f:
    #      m = iter(f.readline,"")
    #      print(next(m))
    #      print(next(m))
    #      print(next(m))
    #      print(next(m))
    #      print(next(m))

    # # iterate and make enumerations the old way

    # for i in range(len(days)):
    #     print(i+1, days[i])

    # using modern enumerator technique
    # for i,d in enumerate(days,start=1):
    #     print(i, d)

    #iterate over the two collections simultaneously

    # for day in zip(days,days_yoruba):
    #     print(day[0],day[1])

    # cool now enumerate it

    for i,day in enumerate(zip(days,days_yoruba), start=1):
        print(f"{i} {day[0]} = {day[1]} in Yoruba language")
        
    # Thank you
if __name__=="__main__":
    main()