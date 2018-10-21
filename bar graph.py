N = 5
i=0
while(len(train_depressed)<100):
    get_tweets(query=keywords[i%len(keywords)],count = 20)
    i+=1
depressed = (100*percentTweetsDepressed(users[0]), 100*percentTweetsDepressed(user[1]), 100*percentTweetsDepressed(users[2]), 100*percentTweetsDepressed(users[3]), percentTweetsDepressed(users[4]))
nondepressed = (100-depressed[0], 100-depressed[1], 100-depressed[2], 100-depressed[3], 100-depressed[4])
menStd = (0, 0, 0, 0, 0)
womenStd = (0, 0, 0, 0, 0)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, depressed, width, yerr=menStd)
p2 = plt.bar(ind, nondepressed, width,
             bottom=depressed, yerr=womenStd)

plt.ylabel('Percentage')
plt.title('Tweet Sentiment Make-Up')
plt.xticks(ind, ('User1', 'User2', 'User3', 'User4', 'User5'))
plt.yticks(np.arange(0, 101, 10))
plt.legend((p1[0], p2[0]), ('Depressed', 'Non-Depressed'))

plt.show()