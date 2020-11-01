"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from Services.MyStreamListenerService import *
from Services.MyClassificationService import *
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/<searchedWord>', methods=['GET'])
def getResult(searchedWord ):
    """Renders a sample page."""
    if str(searchedWord) == "favicon.ico": # Se requisição for vazia
        return "Requisição vazia"

    myStreamListener = MyStreamListener()
    myClassificationService = MyClassificationService()

    myStreamListener.streamPostsRelatedToSearch(searchedWord)

    myDict = myStreamListener.openFileAndSaveDictOfWords()

    myClassificationService.searchWordinMyDict(myDict) # search and set the numbers of emotions
    
    print("\n******Fim de execucao*******")

    return str(myClassificationService.countEmotions())



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
