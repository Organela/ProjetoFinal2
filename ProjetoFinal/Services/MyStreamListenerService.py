
import tweepy
from Services.AuthFile import *
global time
wordOfPosts = []

#Escuta a API do Twitter e guarda os posts em um Array chamado "wordOfPosts"

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
    def streamPostsRelatedToSearch(searchedWord): # Stream de posts
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN , ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth)

        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

        global time
        time = 0
        global wordOfPosts
        wordOfPosts.clear()

        postsRelated = myStream.filter(track=[searchedWord], languages=["pt"]) #locations=[5.253824, -69.908963, -32.283039, -33.800944]

   

    @staticmethod
    def openFileAndSaveDictOfWords(): # Da pra ser otimizado    
        fileList = open('LIWC2007_Portugues_win.dic', 'r').readlines(); #Open File and pass all its content to an array
        myDict = [] #Dict with all words
        lineArray = [] 
        i = 0
        for line in fileList:
            if i > 66 :
                myDict.append(dict(name = None, numbers= []))
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

