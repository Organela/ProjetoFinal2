"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from Services.MyStreamListenerService import *
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/<searchedWord>')
def getResult(searchedWord ):
    """Renders a sample page."""

    if searchedWord.isspace():
        return "Retire os espaços em branco de sua busca!"

    myStreamListener = MyStreamListener()

    myStreamListener.streamPostsRelatedToSearch(searchedWord)

    #for word in wordOfPosts:
            #print("***WordArray****" + word)

    mySortDict = myStreamListener.openFileAndSaveClassificationContent()

    #for p in mySortDict:
       #print(p)

    myDict = myStreamListener.openFileAndSaveDictOfWords()

    for p in myDict:
       print(p)

    return "Hello World!" + searchedWord 


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
