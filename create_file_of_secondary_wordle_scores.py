#!/usr/bin/env python3


import sys
#import json

words = open('draft12')
word_list = words.readlines()
topscorelist = open('top100wordleswithscores.txt')
topscores = topscorelist.readlines()
topscoreword = topscores[0]
outputfile = 'secondaryscorewordle'
# lastletter = test[0]
column = 0
csv = open(outputfile + '.csv', 'w')
csv.write(outputfile)
wordnum = 0
letternum = 0
imperfectscore = 4
exactbonusscore = 1
strlocation = 0

testword ="aaaaa"
points = 0
testrange = 3
#testrange = len(word_list)

# cycle through each word in the dictionary
# for count in range(len(word_list)):
for count in range(testrange):
    t_topscoreword = topscoreword
    second = word_list[count].strip()
    t_second = second
    print('\n')
    print(topscoreword[0:5], " ", second)

    csv.write('\n')
    csv.write(topscoreword[0:5])
    csv.write(",")
    csv.write(second)
#reset points for each word
    points = 0
# check current word against each other word in the dictionary
#    for count2 in range(len(word_list)):
    for count2 in range(testrange):
        testword = word_list[count2].strip()
        t_testword = testword
        print (testword)
        csv.write(",")
        csv.write(testword)
# check each letter in "testword" for its presence in "second" and "topscoreword"
        for count3 in range(5):
            strlocationtop = t_topscoreword.find(t_testword[count3])
            strlocationsecond = t_second.find(t_testword[count3])
            print ("c",count3," ",strlocationtop, " ", strlocationsecond, " ", count3)
            if (strlocationtop or strlocationsecond) == count3:
                points = points + imperfectscore + exactbonusscore
                if t_testword[count3] == t_second[count3]:
                    t_second = t_second[:count3] + str(imperfectscore + exactbonusscore) + t_second[count3 + 1:]
                if t_testword[count3] == t_topscoreword[count3]:
                    t_topscoreword = t_topscoreword[:count3] + str(imperfectscore + exactbonusscore) + t_topscoreword[count3 + 1:]
                t_testword = t_testword[:count3] + str(imperfectscore + exactbonusscore) + t_testword[count3 + 1:]
                print ("1 ", t_topscoreword[0:5]," ",t_second, " ", t_testword , "pts ", str(points))
            elif (strlocationtop or strlocationsecond) != -1:
                points = points + imperfectscore
                if t_testword[strlocationsecond] == t_second[strlocationsecond]:
                    t_second = t_second[:strlocationsecond] + str(imperfectscore) + t_second[strlocationsecond + 1:]
                if t_testword[strlocationtop] == t_topscoreword[strlocationtop]:
                    t_topscoreword = t_topscoreword[:strlocationtop] + str(imperfectscore) + t_topscoreword[strlocationtop + 1:]
                t_testword = t_testword[:count3] + str(imperfectscore) + t_testword[count3 + 1:]
                print ("2 ", t_topscoreword[0:5]," ",t_second, " ", t_testword , "pts ", str(points))
            else:
                print("3 ", t_topscoreword[0:5]," ",t_second, " ", t_testword , "pts ", str(points))
        csv.write("," + t_second)
        csv.write("," + t_testword)
        csv.write(" " + str(points))
    #    print(t_testword," ",t_second," ",str(points), " ")
    csv.write("," + str(points))
csv.write('\n')
csv.close()
