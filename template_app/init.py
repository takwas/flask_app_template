# Module that initialises and runs the app


from flask import Flask

# Create application object 'app'
app = Flask(__name__)
# Link app to global configurations file
app.config.from_object('config')


# Add extension to manage command line argument/options
from flask.ext.script import Manager					# enable command-line interaction (cmd arg parsing) using extension
app_manager = Manager(app)								# run prog with this object instead



#############################################################################
# Database configuration

import os
basedir = os.path.abspath(os.path.dirname(__file__))

####TODO: Change the database file
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '[[db_file_name]]_data.sqlite')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'afraisr_data_test.sqlite')	#DEBUG: test db_url
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# Add SQLAlchemy ORM extension
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Add extension to manage database versions/changes
from flask.ext.migrate import Migrate, MigrateCommand 					
migrate = Migrate(app, db)								
app_manager.add_command('db', MigrateCommand)

# End Database configuration
#############################################################################



# Add a custom Python file to define extra functions/filters for Jinja2 HTML-templating engine
from template_filters import *


####TODO: Import 'views.py'
#from [[app_name]] import views


# Add extension to support Bootstrap features
from flask.ext.bootstrap import Bootstrap			# enable bootstrap templates using extension
bootstrap = Bootstrap(app)


 

# run the program
if __name__ == '__main__':
	app_manager.run()
