"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from Services.MyStreamListenerServices import *
from Services.MyClassificationServices import *
from flask import Flask
from flask_cors import CORS
from flask_jsonpify import jsonify

app = Flask(__name__)

CORS(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app


@app.route('/<searchedWord>', methods=['GET'])
def getResult(searchedWord):
    """Renders a sample page."""
    if str(searchedWord) == "favicon.ico": # Se requisição for vazia
        return "Requisição vazia"

    myStreamListener = MyStreamListener()
    myClassificationService = MyClassificationService()

    myStreamListener.streamPostsRelatedToSearch(searchedWord)

    myDict = myStreamListener.openFileAndSaveDictOfWords()

    b = myClassificationService.searchWordinMyDict(myDict) # search and set the numbers of emotions
    
    print("\n******Fim de execucao*******")

    a = myClassificationService.countEmotions()

    #print(a)

    return jsonify(myClassificationService.countEmotions())



if __name__ == '__main__':
   import os
   HOST = os.environ.get('SERVER_HOST', 'localhost')
   try:
       #PORT = int(os.environ.get('SERVER_PORT', '5555'))
       PORT = 5555
   except ValueError:
       PORT = 5555
   app.run(HOST, PORT)

#port = 54703
#app.run(host='0.0.0.0', port=port)
   
