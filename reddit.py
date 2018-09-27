import praw
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("learnpython")
data = []
for submission in subreddit.hot(limit=50):
    tuple = (submission.title,submission.selftext,submission.score)
    data.append(tuple)
#print("---------------------------------\n")
#print(data)
i = 0
cani = []
#for row in data:
for num, row in enumerate(data, start=0):
	#print(row[0] + '\n')
#	print("---------------------------------\n")
#	print(row[1] + '\n')
#	print("---------------------------------\n")
	message = row[1]
	if ("Can I" in message) or ("the" in row[0]):
#		print('FOUND ----------------------\n\n\n')
		cani.append(row)
	#print(num)
for row in cani:
	print(row[0])
	print('\n')
