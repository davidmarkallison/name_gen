# Program created by a very sleep-deprived David Allison
import argparse             # For CLI args
from pathlib import Path    # For file detection
import random

#TODO 1. Edit the number argument.
#       2. Add an argument for writing out to file.
#          3.
parser = argparse.ArgumentParser()
parser.add_argument("-n","--number",
                    help="Number of names to be generated", required=False)
parser.add_argument("-o","--output",
                    help="File to be written to (.txt is automatically appended)", required=False)
args = parser.parse_args()

if args.number != None:
    num = int(args.number)
else:
    num = 1

#TODO Take arguments from the command line regarding the amount of names 
#     to be generated.
def main():
    generateFamilyNames()
    generateFirstNames()
    pick(num)
    print("\n>\tComplete!")


def generateFamilyNames():
    
    fam = Path("OUT_familynames.txt")
    if fam.is_file() != True:
        # Opens file with family name data from:
        # https://github.com/fivethirtyeight/data/blob/master/most-common-name/surnames.csv
        try:
            familynames_data = open("IN_familynames.txt", "r")
            # Reads In All Data
            formatted_familynames = familynames_data.readlines()
        except Exception as ex:
            print(ex)
        # Creates new file for output 
        familynames_only = open("OUT_familynames.txt","w+")

        # Trims and writes the names to file, separating them with commas
        try:
            for line in formatted_familynames:
                words = line.split(",")
                try:
                    familynames_only.write(words[0] + ",")
                except Exception as ex:
                    print(ex)
        except Exception as ex:
            print(ex)
    else:
        print("\n>\t\'OUT_familynames.txt\' already generated.")


def generateFirstNames():

    fir = Path("OUT_firstnames.txt")
    if fir.is_file() != True:
        # File of first names from:
        # http://www.quietaffiliate.com/free-first-name-and-last-name-databases-csv-and-sql/
        try:
            firstnames_data = open("IN_firstnames.txt", "r")
            # Reads In All Data
            formatted_firstnames = firstnames_data.readlines()
        except Exception as ex:
            print(ex)
        
        # Creates new file for output
        firstnames_only = open("OUT_firstnames.txt","w+")

        try:
            for line in formatted_firstnames:
                try:
                    line = line.replace("\n", "") 
                    firstnames_only.write(line + ",")
                except Exception as ex:
                    print(ex)
        except Exception as ex:
            print(ex)
    else:
        print("\n>\t\'OUT_firstnames.txt\' already generated.")


def pick(num):

    print("\n")

    familynames_only = open("OUT_familynames.txt", "r")
    tempFam = familynames_only.readlines()
    tempFam = tempFam[0].split(",")

    firstnames_only = open("OUT_firstnames.txt", "r")
    tempFirst = firstnames_only.readlines()
    tempFirst = tempFirst[0].split(",")

    if args.output != None:
        #TODO Complete the pick function.
        generatedNames = open(args.output + ".txt", "w")
        for i in range(0, num):
            generatedNames.write("{}\t{} {}\n".format(
                    (i+1),
                    tempFirst[random.randint(0, len(tempFirst))].capitalize(),
                    tempFam[random.randint(0, len(tempFam))].capitalize()
                )
            )
        print(">\t{}.txt has been written to.".format(args.output))
    else:
        #TODO Complete the pick function.
        for i in range(0, num):
            print((i+1) , "\t" ,
                tempFirst[random.randint(0, len(tempFirst))].capitalize(),
                tempFam[random.randint(0, len(tempFam))].capitalize())

# Invoke main function
if __name__ == "__main__":
    main()
