from flask import Blueprint, jsonify, request
from app.models.board import Board
from app import db

board_bp = Blueprint('board', __name__, url_prefix='/boards')

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
