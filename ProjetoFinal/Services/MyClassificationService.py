from Services.MyStreamListenerService import *
import json

class MyClassificationService():
    """description of class """
    global numberOfEmotions
    numberOfEmotions = []
    global filteredNumberOfEmotions
    filteredNumberOfEmotions = []

    def __init__(self):
        pass

    @staticmethod
    def creatingAModel():
        return
            
    #Comparar palavras dos posts com as do liwic e retornar números que demostram as emocoes das palavras/

    def makeArrayEmotionsEmpty(self):
        global numberOfEmotions
        global filteredNumberOfEmotions

        if len(numberOfEmotions) > 0 or len(filteredNumberOfEmotions) > 0:
            numberOfEmotions[:] = []
            filteredNumberOfEmotions[:] = []

    def searchWordinMyDict(self, myDict):
        
        self.makeArrayEmotionsEmpty()

        if len(myDict) <= 0:
            print("Dicionario esta vazio")
        
        global numberOfEmotions
    
        for word in wordOfPosts:
            for element in myDict:
                if word == element["name"]:
                    numberOfEmotions += element["numbers"]              
        
       #print("Numero relacionados as emoções")
       #print(numberOfEmotions)

        return self.filterEmotionNumbers(numberOfEmotions) # vai ser chamado aqui
    

    def filterEmotionNumbers(self, numberOfEmotions):# Implementar filtro de número de emoções
        if len(numberOfEmotions) <= 0:
            print("Nenhuma emoção foi encontrada")
            return
        
        global filteredNumberOfEmotions
        
        for n in numberOfEmotions:
            if n == "22" or n == "128" or n == "129" or n == "130" or n == "134" or n == "360" or n == "121" or n == "122" or n == "123" or n == "125" or n == "148" or n == "355" or n == "356":
               filteredNumberOfEmotions.append(n)
        
        #print("Print de filteredNumberOfEmotions: " + str(filteredNumberOfEmotions))

        return filteredNumberOfEmotions
    
    def countEmotions(self):

        countDict = []

        countSwear = 0
        countAnx = 0
        countAnger = 0
        countSad = 0
        countDiscrep = 0
        countDeath = 0

        countSocial = 0
        countFamily = 0
        countFriend = 0
        countAffect = 0
        countHealth = 0
        countAchieve = 0
        countLeisure = 0

        global filteredNumberOfEmotions

        if len(filteredNumberOfEmotions) <= 0:
            return "Não existe posts relacionados a busca nesse momento ou nao existe emocoes relevantes"

        for n in filteredNumberOfEmotions:
            #print("Print de n: " + str(n))
            if n == "22":
                countSwear+=1
            if n == "128":
                countAnx+=1
            if n == "129":
                countAnger+=1
            if n == "130":
                countSad+=1
            if n == "134":
                countDiscrep+=1
            if n == "360":
                countDeath+=1
            
            if n == "121":
                countSocial+=1
            if n == "122":
                countFamily+=1
            if n == "123":
               countFriend+=1
            if n == "125":
               countAffect+=1
            if n == "148":
               countHealth+=1
            if n == "355":
               countAchieve+=1
            if n == "356":
               countLeisure+=1

        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de xingamentos", count = countSwear))
        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de ansiedade", count = countAnx))
        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de raiva", count = countAnger))
        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de tristreza", count = countSad))
        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de discrepância", count = countDiscrep))
        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de morte", count = countDeath))

        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de social", count = countSocial))
        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de família", count = countFamily))
        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de amizade", count = countFriend))
        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de afeito", count = countAffect))
        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de vida", count = countHealth))
        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de realização", count = countAchieve))
        countDict.append(dict(name="Quantidade de ocorrencia de sentimentos de lazer", count = countLeisure))

        return countDict

           

               
