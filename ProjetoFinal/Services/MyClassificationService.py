from Services.MyStreamListenerService import *

class MyClassificationService():
    """description of class -> Restrigir buscar na API para posts do Brazil"""
    numberOfEmotions = []

    @staticmethod
    def creatingAModel():
        return
    
    @staticmethod
    def searchWordinMyDict(myDict):
        global numberOfEmotions
        numberOfEmotions = []
    
        for word in wordOfPosts:
            for element in myDict:
                if word == element["name"]:
                    numberOfEmotions += element["numbers"]
                
               
        
        print("Numero relacionados as emoções")
        print(numberOfEmotions)