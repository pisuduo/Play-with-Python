import csv

with open ('names.csv','r') as myfile:  #------------- read csv files -----------
    filereader=csv.reader(myfile)
    next(filereader)                    # returns the next item in an iterato
    #for line in filereader:
    #    print(line)                     # print lines in the csv file, each line as a list     why can't write after print

    with open ('newfile.csv','w') as myfile1: #------------- write csv files ------------
        filewriter=csv.writer(myfile1)

        for line in filereader:
            filewriter.writerow(line)





