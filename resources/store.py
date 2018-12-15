from flask_restful import Resource,reqparse
from models.item import ItemModel

class Store(Resource):
	
	def get(self,name):
		
		store = StoreModel.find_by_name(name)
		if store:
			return store.json()
		
		return {"message":"This store don't exist"},404
	
		
	def post(self,name):
			
		if StoreModel.find_by_name(name):
			return{"messgae":"An item '{}' alredy exists in the items list".format(name)}
				
		store= StoreModel(name)
		try:
			store.save_to_db()
		except:
			return{"message":"Error occurred while saving to db"},500
		
		return store.json(),201

	
	def delete(self,name):
		store = StoreModel.find_by_name(name)		
		if store: 
			store.delete_from_db()
			return{"message":"store deleted"}	
		return{"message":"'{}' store is not present in the stores list".format(name)}

class StoreList(Resource):
	def get(self):
		return {'stores': [store.json() for store in StoreModel.query.all()]}
		