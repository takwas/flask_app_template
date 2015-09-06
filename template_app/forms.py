

# Extension imports
from flask.ext.wtf import Form, RecaptchaField
from flask_wtf.html5 import TelField, IntegerField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, DecimalField
from wtforms.validators import Email, DataRequired, EqualTo
#from flask_wtf.file import FileField	
from flask_wtf.file import FileField, FileRequired, FileAllowed # for file upload(s)


####TODO: Import app object
#from [[app_name]] import app

import db_ops




#######################################################################################################################
# Basic template for a form class
#class [[Form_Class_Name]](Form):
	# Create form fields
	####TODO: ...
	## Use fields and validators imported above
	## Submitfield does not need a validator
	## An example is shown for SelectField which loads the fields options from a database. Sample case uses 'categories'
	## An example for FileField is shown below; useful for image uploads

	#[[form_field_name_variable]] = [[FieldType]]('[[Field label]]', validators=[[[List_of_Field_Validators,...]]])
	
	# SelectField Example
	# load categories from DB
	#catgs = [(category.name, category.name) for category in db_ops.ret_all(db_ops.Category)]
	#category_fld = SelectField('Category', choices=catgs, validators=[DataRequired()])

	# FileField example
	#img_fld = FileField('Upload a Profile Photo', \
	#	validators=[FileAllowed(app.config['IMG_ALLOWED_EXTENSIONS'], 'Images only!')])
	#contact_no_fld = TelField('Telephone: ')



# User login form
class LoginForm(Form):
    # openid = StringField('openid', validators=[DataRequired()])
    username_fld = StringField('Username or Email:  ', validators=[DataRequired()])
    password_fld = PasswordField('Password:  ', validators=[DataRequired()])
    remember_me_chkbx = BooleanField('Remember me', default=False)
    login_btn = SubmitField('Sign in!')




# New user signup form
class RegForm(Form):
    
    username_fld = StringField('Username:   ', validators=[DataRequired()])												# Text-Field: First name
    
    email_fld = StringField('Email:   ', validators = [DataRequired()])										# Text-Field: Email
    conf_email_fld = StringField('Confirm Email:   ', validators = [DataRequired()])				# Text-Field: Retype/Confirm Email
    
    password_fld = PasswordField('Password:  ', validators=[DataRequired()])											# Text(Password)-Field: Password
    conf_password_fld = PasswordField('Confirm Password:  ', validators=[DataRequired()])		# Text(Password)-Field: Retype/Confirm Password

    #recap_fld = RecaptchaField()																						# Recaptcha code verification

    #subscrb_chkbx = BooleanField('Subcscribe for our newsletters!', default=False)										# Check-box: Subscribe
    submit_btn = SubmitField('Sign me up!')																				# Button: Submit Form
