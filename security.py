from models.user import UserModel
from werkzeug.security import safe_str_cmp   # for people using python2.7 for safe string camparision


def authenticate(username,password):
	user = UserModel.find_by_username(username)
	if user and safe_str_cmp(user.password,password):
		return user


def identity(payload):
	userid = payload['identity']
	return UserModel.find_by_id(userid)