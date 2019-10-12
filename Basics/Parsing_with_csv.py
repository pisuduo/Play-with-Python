import csv

'''
with open ('names.csv','r') as myfile:  #------------- read csv files -----------
    filereader=csv.reader(myfile)
    next(filereader)                    # returns the next item in an iterato
    #for line in filereader:
    #    print(line)                     # print lines in the csv file, each line as a list     why can't write after print

    with open ('newfile.csv','w') as myfile1: #------------- write csv files ------------
        filewriter=csv.writer(myfile1)

        for line in filereader:
            filewriter.writerow(line)
'''           




with open ('names.csv','r') as myfile2:     
    filereaderdict=csv.DictReader(myfile2)            # use dictionary readers
    #for line in filereaderdict:
    #    print(line)
    with open ('newfile2.csv','w',newline='') as myfile3:  # use newline='' to delete the empty line between rows
        field=['first_name','last_name']              # field name need to be sepecified
        filewritedict=csv.DictWriter(myfile3,fieldnames=field,delimiter='\t')

        filewritedict.writeheader()

        for line in filereaderdict:
            del line['email']                          # delete email column
            filewritedict.writerow(line)

