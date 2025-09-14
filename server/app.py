#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Plant  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)


@app.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants])

@app.route('/plants/<int:id>', methods=['GET'])
def get_plant(id):
    plant = Plant.query.get(id)  
    
    if plant:
        return jsonify(plant.to_dict())
    else:
        return jsonify({'error': 'Plant not found'}), 404

@app.route('/plants', methods=['POST'])
def create_plant():
    data = request.get_json()
    # Add plant creation logic here
    pass


@app.route('/plants/<int:id>', methods=['PATCH'])
def update_plant(id):
    plant = Plant.query.get(id)
    
    if not plant:
        return jsonify({'error': 'Plant not found'}), 404
    
    data = request.get_json()
    
   
    if 'is_in_stock' in data:
        plant.is_in_stock = data['is_in_stock']
    if 'name' in data:
        plant.name = data['name']
    if 'image' in data:
        plant.image = data['image']
    if 'price' in data:
        plant.price = data['price']
    
    try:
        db.session.commit()
        return jsonify(plant.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get(id)
    
    if not plant:
        return jsonify({'error': 'Plant not found'}), 404
    
    try:
        db.session.delete(plant)
        db.session.commit()
        return '', 204 
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5555, debug=True)