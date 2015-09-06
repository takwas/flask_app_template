
import datetime

####TODO: Import 'app' and 'db' objects
#from [[app_name]] import app, db



###############################################################################################################################################################
# Database Model(s)



##########################################################################################################################################################
# Basic template for a database ORM model class
#class [[Model_Class_Name]](db.Model):										# This 'model' represents a table named '[[Model_Class_Name]]' in the database
	####TODO: Use lower-case pluralized version of model name to properly represent the table in the actual database.
	#### E.g. if model (class) name is 'User', then the variable '__tablename__' would be equal to 'users'
	#__tablename__ = '[[lower_case_pluralized_model/class_name]]'			# Use proper pluralized table name

	####TODO: Uncomment to create id field for model
	# primary key
	#id = db.Column(db.Integer, primary_key=True)							# id field; unique id for each record

	####TODO: Create more table fields
	# Commonly used examples of Fiel_Data_Type: String, Integer, Text, Enum, Decimal, DateTime
	# If Field_Data_Type is String, specify the maximum number of characters in brackets
	# If Field_Data_Type is Enum, specify possible (allowed) values in brackets
	# If Field_Data_Type is Float, specify value for 'decimal_return_scale' as a named argument in brackets
	# Commonly used field specific options: index=True, unique=True, nullable=False, default=''
	#[[field_name_variable]] = db.Column(db.[[Field_Data_Type]], [[list of field-specific options...]])


	####TODO: Initialize model
	# object initialization method
	#def __init__(self, [[list of field names with optional default values]]):
		#self.u[[field_name_var]] = [[field_value]]
		

	####TODO: Define a string represention for instances of this model
	# string representation for this object
	#def __repr__(self):
		#return '%r' % [[parameter]]


	#####################################################################################################
	# Column relationships demo...

	####TODO: Customise and use these examples as needed
	# foreign key; also primary key in this table
	# relationship-type: 1-to-1
	#user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), \
		#primary_key=True, autoincrement=False)	# foreign key on 'user_id' column of 'users' table
	#user = db.relationship('User', uselist=False, backref=db.backref('user_verif', uselist=False))

	# foreign key
	# relationship-type: 1-to-1
	#user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	#user = db.relationship('User', uselist=False, backref=db.backref('user_details', uselist=False))

	# multiple foreign keys: 'msg_sender_id' and 'msg_recp_id' relate the same column from another table
	# relationship-type: Many-to-1
	#msg_sender_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	#msg_sender = db.relationship('User', uselist=False, backref='outboxes', foreign_keys=[msg_sender_id])
	#msg_recp_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	#msg_recp = db.relationship('User', uselist=False, backref='inboxes', foreign_keys=[msg_recp_id])

	# End Column relationships demo
	#######################################################################################################






# Users table
class User(db.Model):								# This 'model' represents a table named 'User' in the database
	__tablename__ = 'users'							# Use proper pluralized table name

	# primary key
	user_id = db.Column(db.Integer, primary_key=True)	# id field; unique id for each record

	username = db.Column(db.String(24), index=True, unique=True, nullable=False)		# username field/column
	email = db.Column(db.String(64), unique=True, nullable=False)							# email field
	password = db.Column(db.String(128), nullable=False, default='password')


	# object initialization method
	def __init__(self, username, email, password=None):
		self.username = username
		self.email = email
		
		if password is None:
			# provide a default password as 'password'
			password = 'password'
		self.password = password


	# string representation for this object
	def __repr__(self):
		return '<User %r: %r; %r>' % (self.user_id, self.username, self.email)
