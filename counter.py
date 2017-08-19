from flask import Flask, redirect
app = Flask(__name__)
app.my_vars = {'n' : 0}

@app.route('/')
def counter_app1():
	app.my_vars['n'] += 1
	return("The hit count is : " + str(app.my_vars['n']))

@app.route('/max')
def counter_app2():
	if app.my_vars['n'] > 10:
		return("Max Limit Exceeded")		
	app.my_vars['n'] += 1
	return("The hit count is : " + str(app.my_vars['n']))

@app.route('/finish')
def counter_app3():
	if app.my_vars['n'] > 20:
		return redirect('/end')
	app.my_vars['n'] += 1
	return("The hit count is : " + str(app.my_vars['n']))

@app.route('/end')
def counter_app4():
	return("Please fucking stop! -_-")

if __name__ == '__main__':
	app.run()