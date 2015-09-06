# Template Filters
# Functions defined in this document
# using the 'app.template_filter()'
# decorator can be called from a Jinja2
# template document


####TODO: Import app object
#from [[app_name]] import app


import datetime

# compute the number of days between today
# and specified date throug 'date' parameter
@app.template_filter()
def get_num_days_left(date):
	return (date.date() - datetime.date.today()).days



# get the current year
@app.template_filter()
def get_current_year(num):
	return datetime.datetime.utcnow().year



# get the current year
@app.template_filter()
def get_date(dt=None):
	try:
		date = dt.date()
		return date
	except Exception, e:
		raise e
	finally:
		return None



# get time from date
@app.template_filter()
def get_time(date=None, micro=False):
	
	if date:
		try:
			date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
			time = date.time()
			if milli:
				return time().strftime("%H.%M.%S.%f")
			return time().strftime("%H.%M.%S")
		except Exception, e:
			raise e
		finally:
			return None

	else:
		return None



# debug-print the passed value
@app.template_filter()
def dbg_print(val=''):
	print 'DEBUG_JINJA_PRINT:\t %r' % val



# mark message as 'Read'
@app.template_filter()
def msg_status_change(msg):
	import db_ops
	param_dict = {}
	####TODO: Update parameters as required
	#param_dict['[[message_id_attrib]]'] = msg.[[message_id_attrib]]
	
	####TODO: Update parameters as required
	# mark all user's notifications as read, i.e change 'notif_status'
	#db_ops.update_row(db_ops.[[db_message_model]], param_dict, dict([[db_message_status_attrib]]='[[status_message]]'))