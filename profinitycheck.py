import os;
from urllib import urlopen;
def read_text():
    text=open("/media/raman/New Volume/python_mini_proj/movie_quotes.txt");
    sometext=text.read();
    print(sometext)
    text.close();
    curseword(sometext);
def curseword(sometext):
	connection=urlopen(" http://www.wdylike.appspot.com/?q="+sometext);
	curse=connection.read();
	connection.close();
	if "true" in curse:
	   print ("profanity alert");
	elif "false" in curse:
		print ("ok No curse word");
read_text();