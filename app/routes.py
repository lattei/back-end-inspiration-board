from flask import Blueprint, request, jsonify, make_response
from app import db

class Board:
    def __init__(self, id, title, owner):
        self.id = id
        self.title = title
        self.owner = owner

boards = [
    Board(1, "Board 1", "Owner 1"),
    Board(2, "Board 2", "Owner 2"),
    Board(3, "Board 3", "Owner 3"),
    Board(4, "Board 4", "Owner 4"),

]

board_bp = Blueprint("board", __name__, url_prefix="/boards")

@board_bp.route("", methods=["GET"])
def get_all_boards():
    boards = Board.query.all()
    boards_response = []
    for board in boards:
        boards_response.append({
            "id": board.board_id,
            "title": board.title,
            "owner": board.owner
        })
    return jsonify(boards_response)

@board_bp.route("", methods=["GET"])
def get_board(self, board_id):
    board = Board.query.get(board_id)
    return {
        "id": board.board_id,
        "title": board.title,
        "owner": board.owner
    }
@board_bp.route("/", methods=["POST"])
def create_board():
    request_body = request.get_json()
    new_board = Board(title=request_body["title"],
                    owner=request_body["owner"])
    db.session.add(new_board)
    db.session.commit()
    return make_response(f"Board {new_board.title} successfully created", 201)

@board_bp.route("/<board_id>", methods=["PUT"])
def update_board(board_id):
    board = Board.query.get(board_id)
    form_data = request.get_json()
    board.title = form_data["title"]
    board.owner = form_data["owner"]
    db.session.commit()
    return make_response(f"Board #{board.board_id} successfully updated")

@board_bp.route("/<board_id>", methods=["DELETE"])
def delete_board(board_id):
    board = Board.query.get(board_id)
    db.session.delete(board)
    db.session.commit()
    return make_response(f"Board #{board.board_id} successfully deleted")


class Card:
    def __init__(self, id, message, board_id):
        self.id = id
        self.message = message
        self.board_id = board_id

cards = [
    Card(1, "Card 1", 1),
    Card(2, "Card 2", 1),
    Card(3, "Card 3", 1),
    Card(4, "Card 4", 1),

]

card_bp = Blueprint("card", __name__, url_prefix="/cards")
@card_bp.options("", methods=["OPTIONS"])
def handle_options():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


