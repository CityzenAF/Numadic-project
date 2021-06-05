from flask import Flask, request, Response
import pymongo
from bson import json_util
import json 


app = Flask(__name__)

MONGO_URI = 'mongodb://admin:admin@cluster0-shard-00-00.hyogg.mongodb.net:27017,cluster0-shard-00-01.hyogg.mongodb.net:27017,cluster0-shard-00-02.hyogg.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-ewpby5-shard-0&authSource=admin&retryWrites=true&w=majority'
connection = pymongo.MongoClient(MONGO_URI)
db = connection['numadic']

@app.route('/api/articles')
def articles():
    
    result = db.articles.find()
    return Response(
    	json_util.dumps({
    		'status':'success',
    		'num_articles_found':result.count(),
    		'results' : result}),
    	mimetype='application/json'
	)

@app.route('/api/search/headline')
def search_headline():
	
	query = request.args.get("query","")
	query = query.replace(" ","|")

	result = db.articles.find({"headline" : {"$regex" : query,"$options":"ig"}})
	return Response(
    	json_util.dumps({
    		'status':'success',
    		'num_articles_found':result.count(), 
    		'results' : result}),
    	mimetype='application/json'
	)

@app.route('/api/search/author')
def search_author():
	
	query = request.args.get("query","")
	query = query.replace(" ","|")
	
	result = db.articles.find({"author" : {"$regex" : query,"$options":"ig"}})
	return Response(
    	json_util.dumps({
    		'status':'success',
    		'num_articles_found':result.count(), 
    		'results' : result}),
    	mimetype='application/json'
	)

if __name__ == "__main__":
    app.run(port=3000)