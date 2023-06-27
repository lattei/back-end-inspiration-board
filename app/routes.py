from flask import Blueprint, jsonify, request
from app.models import Board, Card
from app import db

board_bp = Blueprint('board', __name__, url_prefix='/boards')
card_bp = Blueprint('card', __name__, url_prefix='/cards')

@board_bp.route('/', methods=['GET'])
def get_boards():
    boards = Board.query.all()
    board_list = [board.to_json() for board in boards]
    return jsonify(board_list)

@board_bp.route('/', methods=['POST'])
def create_board():
    data = request.json
    title = data.get('title')
    owner = data.get('owner')

    board = Board(title=title, owner=owner)
    db.session.add(board)
    db.session.commit()

    return jsonify({'message': 'Board created successfully'}), 201

@board_bp.route('/<int:board_id>', methods=['GET'])
def get_board(board_id):
    board = Board.query.get_or_404(board_id)
    return jsonify(board.to_json())

@board_bp.route('/<int:board_id>', methods=['PUT'])
def update_board(board_id):
    board = Board.query.get_or_404(board_id)
    data = request.json
    title = data.get('title')
    owner = data.get('owner')

    board.title = title
    board.owner = owner
    db.session.commit()

    return jsonify({'message': 'Board updated successfully'})

@board_bp.route('/<int:board_id>', methods=['DELETE'])
def delete_board(board_id):
    board = Board.query.get_or_404(board_id)
    db.session.delete(board)
    db.session.commit()

    return jsonify({'message': 'Board deleted successfully'})

@board_bp.route('/<int:board_id>/cards', methods=['GET'])
def get_board_cards(board_id):
    board = Board.query.get_or_404(board_id)
    cards = board.cards
    card_list = [card.to_json() for card in cards]
    return jsonify(card_list)

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

