

for line in f:
    print (line)
with open('C:/Users/maziy/Google Drive/Data Science/Python/Practicecoding/Play-with-Python/Basics/google-basic-python-exercises/basic/small.txt','r') as f:
    for line in f:
        print(line)

with open('C:/Users/maziy/Google Drive/Data Science/Python/Practicecoding/Play-with-Python/Basics/google-basic-python-exercises/basic/small.txt','r') as f:
    for line in f.readlines():
        print(line)

with open('C:/Users/maziy/Google Drive/Data Science/Python/Practicecoding/Play-with-Python/Basics/google-basic-python-exercises/basic/small.txt','r') as f:
    for line in f.read():
        print(line)

with open('C:/Users/maziy/Google Drive/Data Science/Python/Practicecoding/Play-with-Python/Basics/google-basic-python-exercises/basic/small.txt','r') as f:
    for line in f.readline():
        print(line)  ## only return the first line

f=open('C:/Users/maziy/Google Drive/Data Science/Python/Practicecoding/Play-with-Python/Basics/google-basic-python-exercises/basic/small.txt','r')
lines=f.readline()
print(lines)  ## first line
lines=f.readline()
print(lines)  ## second line
f.close()

f=open('C:/Users/maziy/Google Drive/Data Science/Python/Practicecoding/Play-with-Python/Basics/google-basic-python-exercises/basic/small.txt','r')
words=f.read()
f.close()

f1='C:/Users/maziy/Google Drive/Data Science/Python/Practicecoding/Play-with-Python/Basics/google-basic-python-exercises/babynames/baby1990.html'