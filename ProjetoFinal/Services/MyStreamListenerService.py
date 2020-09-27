
import tweepy
from Services.AuthFile import *
global time
time = 0
wordOfPosts = []
#from DictionaryFile import *
#Part 2 tutorial está explicando como vou definir o numero de tweets q eu vou ler

class MyStreamListener(tweepy.StreamListener):
       
    def _init_(self):
        pass

    def on_status(self, status):
        global time

        if time <= 0:
            print("********A stream foi inicializada !!!*******")
        print(status.text)
        self.concatenateToWordsOfPosts(status.text)
        
        time = time + 1
        if time > 3 :
            print("***********Stream finalizada!!!***********")
            return False
    
    @staticmethod
    def concatenateToWordsOfPosts(words):
        global wordOfPosts 
        wordOfPosts += words.split()
        #for word in wordOfPosts:
            #print("***WordArray****" + word)
        return
    @staticmethod
    def streamPostsRelatedToSearch(searchedWord):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN , ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth)

        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

        postsRelated = myStream.filter(track=[searchedWord], languages=["pt"])
        #print(myStream.filter(track=['python']))
        #print(postsRelated)
        #return postsRelated

    @staticmethod
    def openFileAndSaveClassificationContent():
        fileList = open('LIWC2007_Portugues_win.dic', 'r').readlines(); #Open File and pass all its content to an array
        mySortDict = [] #Dict with word translation for emotions
        clasificationArray = []

        i = 0
        for line in fileList:
            if i > 64 :
                break
            if i < 69 :
                mySortDict.append(dict(name = None, number = None, classification= None))
                clasificationArray = line.split()

                for text in clasificationArray :
                    if text.isnumeric() == False :
                        mySortDict[i]["name"] = text
                        #print("Classificação: " + text)
            
                    if text.isnumeric() == True :
                        mySortDict[i]["number"] = text
                        #print("Número da classificação: " + text)
            i = i + 1
        
        return mySortDict

    @staticmethod
    def openFileAndSaveDictOfWords():    
        fileList = open('LIWC2007_Portugues_win.dic', 'r').readlines(); #Open File and pass all its content to an array
        myDict = [] #Dict with all words
        lineArray = [] 
        i = 0
        for line in fileList:
            if i > 66 :
                myDict.append(dict(name = None, numbers= [], classification= None))
                lineArray = line.split()

                j = 0
                for text in lineArray :
                    if j == len(lineArray) :
                        #print("Lenght lineArray" + len(lineArray))
                        break

                    if text.isnumeric() == False :
                        myDict[i - 67]["name"] = text
                        #print("Only text: " + text)
            
                    if text.isnumeric() == True :
                        myDict[i - 67]["numbers"].append(text)
                        #print("Only numbers: " + text)
                    j = j + 1
    
            #if i > 100 :
                #break
    
            i = i + 1
        return myDict

# SERCH FOR WORD IN MYDICT

#if __name__ == '__main__':

#    myStreamListener = MyStreamListener()

#    myStreamListener.streamPostsRelatedToSearch()
    
    #for word in wordOfPosts:
        #print("Printando words " + word)

#    mySortDict = myStreamListener.openFileAndSaveClassificationContent()

#    for p in mySortDict:
#        print(p)

#    myDict = myStreamListener.openFileAndSaveDictOfWords()

#    for p in myDict:
#       print(p)
