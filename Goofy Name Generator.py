
first = ["stinky","lumpy","buttercup","gidget","crusty","greasy","fluffy","cheeseball","chim-chim","poopsie","flunky","booger","pinky","zippy","goober","doofus","slimy","loopy","snotty","falafel","dorkey","squeezit","oprah","skipper","dinky","zsa-zsa"]

last1 = ["diaper","toilet","giggle","bubble","girdle","barf","lizard","waffle","cootie","monkey","potty","liver","banana","rhino","burger","hamster","toad","gizzard","pizza","gerbil","chicken","pickle","chuckle","tofu","gorilla","stinker"]

last2 = ["head","mouth","face","nose","tush","breath","pants","shorts","lips","honker","butt","brain","tushie","chunks","hiney","biscuits","toes","buns","fanny","sniffer","sprinkles","kisser","squirt","humperdinck","brains","juice"]


name = input('What is your name?')
name = name.strip()
name = name.lower()
name = name.split(' ')
newname = ord(name[0][0])-97
newname1 = ord(name[1][0])-97
newname2 = ord(name[1][-1])-97

print(first[newname]+' '+last1[newname1]+' '+last2[newname2] )


