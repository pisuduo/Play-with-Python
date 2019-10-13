# DATACAMP exercises
# match string with regular expressions
import re
'''
prog=re.compile('\d{3}-\d{3}-\d{4}')
result=prog.match('123-456-7890')
print(bool(result))

result2=prog.match('0123-456-7890')
print(bool(result2))

# Extracting numerical values from strings

'''
##----------------------------------------- Regular Expressions ------------------------------##
#Write a regex that matches the user mentions that follows the pattern, e.g. @robot3!. \d to match digits, \W to match non-word

sentiment_analysis='@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'

regex = r"@robot\d\W"   # Write the regex

print(re.findall(regex, sentiment_analysis)) # Find all matches of regex

#Write a regex that matches the number of user mentions given as, for example, User_mentions:9 in sentiment_analysis.

sentiment_analysis="Unfortunately one of those moments wasn't a giant squidd monster. \
    User_mentions:2, likes: 9, number of retweet: 7"


print(re.findall(r"User_mentions:\d", sentiment_analysis))   # Write a regex to obtain user mentions

print(re.findall(r"likes:\s\d", sentiment_analysis))         # Write a regex to obtain number of likes

print(re.findall(r"number\sof\sretweet:\s\d", sentiment_analysis)) # Write a regex to obtain number of retweets

#------------- MATCH AND SPLIT -------------------#
sentiment_analysis='He#newHis%newTin love with$newPscrappy. #8break%He is&newYmissing him@newLalready'

regex_sentence = r"\W\dbreak\W" # Write a regex to match pattern separating sentences

sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis) # Replace the regex_sentence with a space

regex_words = r"\Wnew\w" # Write a regex to match pattern separating words


sentiment_final = re.sub(regex_words," ", sentiment_sub) # Replace the regex_words and print the result
print(sentiment_final)

#--------------------------------------- Repetitions ------------------------------------------#

sentiment_analysis=["Boredd. Colddd @blueKnight39 Internet keeps stuffing up. Save me! https://www.tellyourstory.com",
"I had a horrible nightmare last night @anitaLopez98 @MyredHat31 which affected my sleep, now I'm really tired",
"im lonely  keep me company @YourBestCompany! @foxRadio https://radio.foxnews.com 22 female, new york"]
for tweet in sentiment_analysis:
	# Write regex to match http links and print out result  Start with http, and donot contain any whitespace
	print(re.findall(r"http\S+", tweet))

	# Write regex to match user mentions and print out result start from @ and can have letters and numbers only
	print(re.findall(r"@\w+\d*", tweet))

#--------------------------------------------------------------------#

sentiment_analysis=["I would like to apologize for the repeated Video Games Live related tweets. 32 minutes ago",
"@zaydia but i cant figure out how to get there / back / pay for a hotel 1st May 2019",
"FML: So much for seniority, bc of technological ineptness 23rd June 2018 17:54"]

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\s\w+\s\w+", date))

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}", date))

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))

#---------------------------------------------------------------------#

sentiment_analysis='ITS NOT ENOUGH TO SAY THAT IMISS U #MissYou #SoMuch #Friendship #Forever'
# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)

# Get tokens by splitting text
print(re.split(r"\s+", no_hashtag))


