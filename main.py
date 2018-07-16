import getData
import detect
import os, os.path

numbers = []

def main():
    index = 1
    path = ("Clips_Desired")
    file_count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

    while index <= file_count:
        filePath = "Clips_Desired/0%d.avi" % (index)
        print filePath
        getData.callDetect(filePath)

        index += 1

        getData.find_Squares_Files()
        sum = getData.count_Shapes()

        numbers.append(sum)

#main()
#print "<--------------------------------------------->", numbers

def runner():
    list = [168432, 313776, 287440, 364888, 347124, 575468, 481129, 398128, 528472, 401308, 517348, 521516, 521516, 309524, 634836, 602340,
    441856, 492104, 497424, 497424]

    num = sum(list)/len(list)

    print num

runner()
