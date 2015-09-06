# Module containing view functions

import os, datetime

from flask import request, render_template, flash, redirect, url_for, session, g
####TODO: Import app object
#from [[app_name]] import app
from forms import *

from werkzeug import secure_filename

import utils, db_ops	



####TODO: Define operations to be performed before each request; Save temporary values in the 'g' dictionary
# This function is called before every request
@app.before_request
def load_notifs():
	pass


# 404 view function for not-found urls
@app.errorhandler(404)
def _404(error):
	return render_template('404.html'), 404


# Landing page view function
@app.route('/')
@app.route('/index')
def index():
# |go to home page;		|response-status-code:200 by default
	
	####TODO: Remove flash message
	flash('Welcome Home!')	
	return render_template('index.html')



# a custom user-page
@app.route('/user')
@app.route('/user/')
@app.route('/user/<username>')
def profile(username=None):

	####TODO: THIS IS JUST A HACK TO PROCESS USERNAME IN ROUTE'S URL; PROPERLY IMPLEMENT THIS
	if not str(request.url).__contains__('?'):
		test = username

	else:
		test = str(request.url).split('?')[1].split('=')[1] #str(name).lower()
	

	if session.get('in_session'):
		
		if test is None or test == session.get('username'):
			return render_template('user.html', username=session.get('username'))
		
	return redirect(url_for('index'))



# login page
@app.route('/sign_in', methods=['GET', 'POST'])
@app.route('/signin', methods=['GET', 'POST'])
@app.route('/log_in', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login_auth():
	
	form = LoginForm()

	####TODO: ADD CODE TO PROPERLY VALIDATE FORM FIELDS
	if form.validate_on_submit():
		
		####TODO: ADD CODE TO HANDLE INVALID LOGIN

		# code to enable login with username or email
		param_dict={}
		
		if form.username_fld.data.find('@') > -1:	# user entered email not username
			param_dict['email'] = form.username_fld.data		# create email key ins session dictionary
		
		else: 	# user entered username not email
			param_dict['username'] = form.username_fld.data 	# create username key ins session dictionary

		user = db_ops.ret_val(db_ops.User, param_dict)			# retrieve 'user' object with usernam or email, depending on which is provided

		
		if user is not None:	# user with username/email was found

			param_dict.clear()
			
			# retrieve full user details from DB using 'user_id'
			#param_dict['user_id'] = user.user_id
			#user_det = db_ops.ret_val(db_ops.UserDetails, param_dict)
		
			
			####TODO: ADD CODE TO PROPERLY VALIDATE PASSWORD CORRECTNESS; FIND A MORE SECURE APPROACH
			# begin password verification
			if form.password_fld.data == user.password:		# Validate correctness of password; dumb procedure though, but should suffice
				
				session['in_session'] = True	# login was successful; a user is now in session

				# get active user's username and email details
				session['username'] = user.username
				session['email'] = user.email
				
				# get active user's name details if available
				#if user_det is not None:
					#if user_det.f_name is not None:
						#session['f_name'] = user_det.f_name

					#if user_det.l_name is not None:
						#session['l_name'] = user_det.l_name


				####TODO: NEED TO IMPLEMENT BETTER SECURITY HERE
				form.username_fld.data = ''											# clear username field data in form
				form.password_fld.data = ''											# clear password field data in form

				flash("User '%s' has been logged-in;    Remember_me=%s" %(session.get('username'), str(form.remember_me_chkbx.data)))		#DEBUG

				# notify user of login operation
				#notif_msg = 'You logged in at '+ str(datetime.datetime.utcnow())
				#utils.notify(user, notif_msg)

				return redirect(url_for('profile', username = session.get('username')))
				#end: password verification
			
			else:	# incorrect password entry
				flash('You may have entered the wrong password! Try again')			#DEBUG

				# notify user of login operation
				#notif_msg = 'An attempt was made to log into your account at: '+ str(datetime.datetime.utcnow())
				#utils.notify(user, notif_msg)
				
		#end: if: form fields validated

		else:	# incorrect email or username entry
			flash('Username or Email not found in our records!')	#DEBUG

	
	else:	# Login Failed! ..... clear session credentials
		if request.method=='POST':
			flash('Check your Details!')		#DEBUG
		session.pop('username', '')
		session.pop('email', '')
		#session.pop('f_name', '')
		#session.pop('l_name', '')


	session['in_session'] = False	# no user is in session
	return render_template('login.html', form = form)



# Account Registration page
@app.route('/reg', methods=['GET', 'POST'])
@app.route('/sign_up', methods=['GET', 'POST'])
def signup():

	form = RegForm()

	####TODO: ADD CODE TO PROPERLY VALIDATE FORM FIELDS
	if form.validate_on_submit():
		param_dict = {}		# dict to map keywords to values retrieved from registration form

		# retrieve user registration data from form
		param_dict['username'] = form.username_fld.data.lower().decode('utf-8')		# username converted to all-lower case
		param_dict['email'] = form.email_fld.data.decode('utf-8')
		####TODO: IMPLEMENT PASSWORD HASHING
		param_dict['password'] = form.password_fld.data.decode('utf-8') or ''
		
		db_ops.insert_val(db_ops.User, param_dict)	# insert new values into DB
		
		param_dict.pop('email')			# clear dictionary key: email
		param_dict.pop('password')		# clear dictionary key: password
		
		user = db_ops.ret_val(db_ops.User, param_dict)		# retrieve user object from DB using username
		
		param_dict.clear()
		
		#if user is not None:
			# notify user of signup
			#notif_msg = 'Welcome to Afraisr, <span href="%s">%s</span>!' %(url_for('profile', username=user.username), user.username)
			#utils.notify(user, notif_msg)
			
			#param_dict['user_id'] = user.user_id	# get user_id from user object
			#param_dict['profile_img_name'] = app.config['DEFAULT_SILHOUETTE_UNKNOWN']		# set default user profile image for new user
			#param_dict['reg_time'] = datetime.datetime.utcnow()								# set user account creation date and time
			#db_ops.insert_val(db_ops.UserDetails, param_dict)	# save user details


		flash('Successfully Registered!')

		

		return redirect(url_for('login_auth'))
	
	else:
		if request.method=='POST':
			flash('Check your Details!')
	

	session['in_session'] = False
	return render_template('sign_up.html', form = form)




####TODO: Add methods paramater to view function decorator if page will submit a form
# The following is an example of an inbox page view function. The user can send a message
#@app.route('/<username>/messages', methods=['GET', 'POST'])
#def inbox(username=None, buddy_name=None):	
	#form = MessageForm()

	#if form.validate_on_submit():
		#msg = form.msg_fld.data
		#form.msg_fld.data = ''
		#utils.send_msg(g.user, buddy, msg)

		#flash('Message sent; please refresh page.')

	#return render_template('msg_inbox.html', form=form)

