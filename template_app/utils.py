# A custom Python file to containing utility (helper)
# [mostly independent] functions that are sometimes
# used within the app



import json

# JSON dump object
def dump(obj):
    return json.dumps(obj.__dict__)



# parses attributes of a query row object to a dict
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d



# verifies if 'filename' has a valid (required) extension
def allowed_file(filename, allw_ext):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in allw_ext



# check if given string is a mix of alphanumeric characters
def contains_alnum(string):
	''' Returns true if string contains both
	alphabets and numbers
	'''

	al, num = 0, 0

	for s in string:
		if s.isalpha():
			al +=1
		if s.isdigit():
			num +=1
	
	if al <=0 or num<=0:
		return False

	return True
		


# generates a random string that defaults to 8 characters
def get_random_string(n=8):
	import string, random
	return ''.join(random.SystemRandom().choice(string.ascii_letters+string.digits) for _ in range(n))





import db_ops

# send given notification message to given user
def notify(user, msg):
	pass
	####TODO: Update parameters as required
	#db_ops.insert_val(db_ops.[[db_notification_model]], dict([[db_notification_owner_id_attrib]]=user.[[notification_owner_id_attrib]], [[db_notification_message_attrib]]=msg))


# given [conversation] message from given 'sender' to given 'recipient'
def send_msg(sender, recp, msg):
	pass
	####TODO: Update parameters as required
	#db_ops.insert_val(db_ops.[[db_message_model]], \ dict([[db_message_sender_id_attrib]]=sender.[[sender_id_attrib]], [[db_message_recipient_id__attrib]] = recp.[[recipient_id_attrib]], \[[db_message_text_attrib]]=msg))
