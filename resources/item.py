from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price',
			type=float,
			required=True,
			help="The 'price' field cannot be left balnk!"
			)
	parser.add_argument('store_id',
			type=int,
			required=True,
			help="The 'store_id' field cannot be left balnk!"
			)


	@jwt_required()
	def get(self,name):
		
		item = ItemModel.find_by_name(name)
		if item:
			return item.json()
		
		return {"message":"This item don't exist"},404
	
		
	def post(self,name):
			
		if ItemModel.find_by_name(name):
			return{"messgae":"An item '{}' alredy exists in the items list".format(name)}
		
		data = Item.parser.parse_args()
		
		item = ItemModel(name,**data)
		try:
			item.save_to_db()
		except:
			return{"message":"Error occurred while saving to db"},500
		
		return item.json(),201

	
	def put(self,name):

		data = Item.parser.parse_args()
		
		item = ItemModel.find_by_name(name)
		
		if item is None:
			item = ItemModel(name, **data)
					
		else:
			item.price = data['price']
			item.store_id = data['store_id']
		
		item.save_to_db()
		return item.json()

	
	def delete(self,name):
		item = ItemModel.find_by_name(name)		
		if item: 
			item.delete_from_db()
			return{"message":"item deleted"}	
		return{"message":"'{}' item is not present in the items list".format(name)}

class ItemList(Resource):
	def get(self):
		return {'items': [x.json() for x in ItemModel.query.all()]}
		