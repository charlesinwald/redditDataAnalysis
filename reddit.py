#Reddit scraper
import praw
#Natural Language Processing
import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("Jokes")
data = []
#Gather Reddit posts
for submission in subreddit.hot(limit=200):
    tuple = (submission.title,submission.selftext,submission.score)
    data.append(tuple)
i = 0
cani = []
correct = []
#For each post, perform NLP
for num, row in enumerate(data, start=0):
	message = row[1]
	cani.append(row)
	print(row[i])
	doc = nlp(row[i])
	for entity in doc.ents:
		print(entity.text, entity.label_,'\n')
		correct.append(entity.text)
counts = Counter(correct)
counts2 = []
for element in correct:
	print(element, counts[element],  '\n')
	counts2.append((counts[element],element))
counts2 = set(sorted(counts2, reverse=True))
counts3 = sorted(counts2, reverse=True)
for element in counts3:
	print(element)
	for i in range(0, element[0]):
		print('[-]', end='')
	print('\n---------------------------------------------------');
print('---------------------------------------------------');
