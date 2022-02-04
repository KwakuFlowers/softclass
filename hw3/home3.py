from logging import NullHandler
import math
import os


class homework3:
    def Q1():
        word = input("Type a word that you are looking to use for a string:")
        info = []
        vowels = "aeiouAEIOU"
        vowelscount=0
        consoncount=0
        if (word.isalpha()):
            for a in word:
                if a in vowels:
                    vowelscount+=1
                else:
                    consoncount+=1
            if vowelscount > consoncount:
                return True 
            elif vowelscount < consoncount:
                return False
            else:
                return None
    print(Q1())

    def Q2():
        radius = input ("Type the radius:")
        height = input("Type the height:")
        newrad = math.pow(radius,2)
        volume = (math.pi * newrad * height)
        return volume

    def Q3():
        start = input("Type in the strings you want to include, seperated by spaces")
        retstring = start.split()
        return retstring
    
    def Q4():
        fulllist =[]
        numfulllist =4 
        out = open("output.txt", "x")

        l1 = [1,2,3,4]
        l2 = [5,6,7,8]
        l3= [9,10,11,12]
        l4 = [13,14,15,16]
        for b in range(numfulllist):
            fulllist.append("l"(b))

        for i in fulllist:
            retstring = fulllist[i].split()
            out.write(retstring + '\n')
        out.close()

    def Q5(filename):
        listolists = []
        start = open ( filename, "r")
        for line in start:
            orilist = start.split(",")
            listolists.append(orilist)
        return listolists

    def Q6(num1, num2):
        try:
            newnum = num1/num2
        except num2==0:
            print("Denominator is zero, and in math that is not allowed")
        return newnum

    def Q7():
        user = input("Type the list of integers you want to include, seperated by commas")
        oldlist =user.split(",")
        newlist =[]
        for i in oldlist:
            if len(newlist)==0: 
                newlist.append(oldlist[i])
            else:
                for g in newlist:
                    if newlist[g] == oldlist[i]:
                        i+=1
                newlist.append(oldlist[i])
        return newlist

    def Q8():
        path = "/home/softclass/hw3/hw3-folder"
        os.mkdir(path)