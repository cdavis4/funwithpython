"""
This program takes input data from txt file that represents addresses of Coronado
"""
import os,sys, re

class DataHolder:
    def __init__(self, name):
       self.name = name
    def set(self,inValue):
        self.name = inValue

def writeLine(inputArray):
    print inputArray
    with open("CoronadoFlowerLocations.csv", "a") as fileOut:
        fileOut.write(' '.join(map(str,inputArray)))
        fileOut.write('\n')

def matchValue(val,checkVal, inputVal):
    return re.search('' + val + '((?!' + checkVal + ').)*$', inputVal)

def main(argv):
    try:
        if os.path.exists('CoronadoFlowerLocations.csv'):
            os.remove('CoronadoFlowerLocations.csv')

        if argv.endswith('.txt'):
            file = open(argv)
            address = DataHolder('')
            address.name = ''
            award = DataHolder('')
            award.name = ''
            for line in file:
                notBlue = matchValue('^', 'BLUE', line)
                notRed = matchValue('^', 'RED', line)
                notYellow = matchValue('^', 'YELLOW', line)
                if (re.search('^[A-Z]', line)) and notBlue and notRed and notYellow:
                    address.set(line)
                if "BLUE" in line or "YELLOW" in line or "RED" in line:
                    award.set(line)
                if re.search('^[0-9]', line):
                    num = re.split(r"[.,]",line)
                    for i in num:
                        if re.search('[0-9]',i):
                            writeLine(i.rstrip() +  ' ' + address.name.rstrip() + ',' + award.name.rstrip())
        else: print("Nothing in file")
        file.close()
    except:
        print "fail"

if __name__ == "__main__":
    if len(sys.argv) >1:
        input = sys.argv[1]
        main(input)
    else:
        main("RAW_Flower_Data.txt")


