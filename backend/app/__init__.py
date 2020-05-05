from flask import Flask, jsonify

from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

for i in range(3):
    blockchain.add_block(i)

@app.route('/') # Define end point for the API using the @app decorator
def route_default():
    return 'Welcome to the Blockchain'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

app.run()
