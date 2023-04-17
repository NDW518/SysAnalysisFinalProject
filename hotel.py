from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template('welcome.htm')

@app.route('/bookaroom')
def bookaroom():
	return render_template('booking.htm')

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['username']
		pswd = request.form['password']
		if user == 'manager' and pswd == 'hotelManager18':
			return render_template('manager_view.htm', name=user)
		else:
			return render_template('rejected_login.htm', name=user)
	return 'login'


if __name__ == "__main__":
	app.run()
