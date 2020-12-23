from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"msg": "store not found."}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"msg": "Store with '{}' already exists.".format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"msg": "An error occurred while creating the store."}, 500
        return store.json(), 201
        

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"msg": "Store '{}' was deleted.".format(name)}, 400

class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}