#-------------------------------------------------------------------------#
movie='$I supposed that coming from MTV Films I should expect no less$'
# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)

# Remove whitespaces and print the result
movie_no_space = movie_lower.strip("$")
print(movie_no_space)

# Split the string into substrings and print the result
movie_split = movie_no_space.split()
print(movie_split)

# Select root word and print the result
word_root = movie_split[1][:-1]
print(word_root)

#------------------------------Joining---------------------------------------------#
movie='the film, however, is all good <\i>'
# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(",")
print(movie_no_comma)

# Join back together and print results
movie_join = ' '.join(movie_no_comma)
print(movie_join)

#-------------------------------Finding and Replacing---------------------------------------------#
# Split string at line boundaries
file1='stringa, a ,stttt sgsgsrhs,erhersgsaher' # should be a variable with multiple lines
print(file1)
file_split = file1.splitlines()

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(',')
    print(substring_split)

#----------------------------Finding and Replacing -----------------------------------------------#
for movie in movies:
  	# Find if actor occurrs between 37 and 41 inclusive
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two by one
    elif movie.count("actor") == 2:  
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences by one
        print(movie.replace("actor actor actor", "actor"))


for movie in movies:
  try:
    # Find the first occurrence of word
  	print(movie.find('money', 12, 51))
  except ValueError:
    print("substring not found")

for movie in movies:
  try:
    # Find the first occurrence of word
  	print(movie.index('money', 12, 51))
  except ValueError:
    print("substring not found")


# Replace negations 
movies_no_negation = movies.replace("isn't", "is")

# Replace important
movies_antonym = movies_no_negation.replace("important", "insignificant")

# Print out
print(movies_antonym)