####TODO: Import database objects
#from database import db, datetime, [[List of Database models or *]]
import database


db.create_all()


# insert given record into specified table(model)
def insert_val(model, param_dict):
	row = model(**param_dict)
	db.session.add(row)
	commit_db()



# insert given list of values into specified
# table (model)
def insert_vals(model, dict_list):
	for param_dict in dict_list:
		insert_val(model, param_dict)


# update database with data
# model: DB table to be updated
# param_dict_ret: dict holding keyword args with which to retrieve previous data, before updation
# param_dict_ins: dict holding keyword args with which to insert new data
def update_row(model, param_dict_ret, param_dict_ins):
	row = model.query.filter_by(**param_dict_ret).update(param_dict_ins)
	commit_db()


# Retreive record from specified table (model) using
# given key (for field) and value (as record)
def ret_val(model, param_dict):
	row = model.query.filter_by(**param_dict).first()
	return row


# Retreive records from specified table (model) using
# given key (for field) and value (as record)
def ret_all_val(model, param_dict):
	row = model.query.filter_by(**param_dict).all()
	return row


# Retreive all records from specified table (model)
def ret_all(model):
	rows = model.query.all()
	return rows

# commit changes to the database
def commit_db():
	db.session.commit()


def get_obj(model, obj):
	ret_val
