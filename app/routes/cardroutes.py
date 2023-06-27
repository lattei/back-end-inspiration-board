from flask import Blueprint, jsonify, request
from app.models.card import Card
from app import db

card_bp = Blueprint('card', __name__, url_prefix='/cards')

@card_bp.route('/', methods=['GET'])
def get_cards():
    cards = Card.query.all()
    card_list = [card.to_json() for card in cards]
    return jsonify(card_list)

@card_bp.route('/', methods=['POST'])
def create_card():
    data = request.json
    message = data.get('message')
    likes_count = data.get('likes_count')

    card = Card(message=message, likes_count=likes_count)
    db.session.add(card)
    db.session.commit()

    return jsonify({'message': 'Card created successfully'}), 201

@card_bp.route('/<int:card_id>', methods=['GET'])
def get_card(card_id):
    card = Card.query.get_or_404(card_id)
    return jsonify(card.to_json())

@card_bp.route('/<int:card_id>', methods=['PUT'])
def update_card(card_id):
    card = Card.query.get_or_404(card_id)
    data = request.json
    message = data.get('message')
    likes_count = data.get('likes_count')

    card.message = message
    card.likes_count = likes_count
    db.session.commit()

    return jsonify({'message': 'Card updated successfully'})

@card_bp.route('/<int:card_id>', methods=['DELETE'])
def delete_card(card_id):
    card = Card.query.get_or_404(card_id)
    db.session.delete(card)
    db.session.commit()

    return jsonify({'message': 'Card deleted successfully'})
