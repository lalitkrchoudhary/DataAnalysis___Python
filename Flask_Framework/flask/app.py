from flask import Flask, render_template

'''
It create an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
### WSGI application
app=Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to the flask framework"

@app.route("/index")
def indexPage():
    return render_template('index.html') #Render_template will search index page into templates folder


if __name__=="__main__":
    app.run(debug=True) #debug=Ture because when we write the code we don't have to run again and again