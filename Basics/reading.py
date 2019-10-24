with open('/Users/maziyang/Google Drive/Data Science/Python/Practicecoding/Play-with-Python/Basics/hrdata.txt','r') as f:
    total_sal=0
    f.readline()
    for line in f:  
        words=line.replace(',',' ')
        salary=float(re.search(pattern,words).group())
        total_sal +=salary
        turple=re.findall(r'(\d{4,5}\W\d+)\s(\d+)',words)
        (s,day)=turple[0]
        print('{},{}'.format(s,day))
        #print(re.search(pattern,words).group(1))
        print(words)

f.readlines()

import re
pattern=r'\d{4,5}\W\d+'


