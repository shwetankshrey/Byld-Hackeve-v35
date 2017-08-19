from flask import Flask, render_template
app = Flask(__name__)
lst = ["Aman", "Bhairo", "Chaman"]

@app.route('/')
def template_app1():
   return('<html><body><h1>My name is Shwetank Shrey!</h1></body></html>')

@app.route('/temp')
def template_app2():
   return(render_template('name1.html'))

@app.route('/user')
def template_app3():
   return(render_template('name2.html', name = "Shwetank"))

@app.route('/user/<xname>')
def template_app4(xname):
   return(render_template('name2.html', name = xname, somelist = lst))

if __name__ == '__main__':
   app.run()