import pytest
from app import create_app
from app.models.card import Card
from app.models.board import Board
from app import db



@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def one_card(app):
    new_card = Card(
        message="You got this"
    )
    db.session.add(new_card)
    db.session.commit()

@pytest.fixture
def three_cards(app):
    db.session.add_all([
        Card(
        message="You got this!"),
        Card(
        message="You snooze you lose"),
        Card(
        message="and I oop")
    ])
    db.session.commit()

@pytest.fixture
def one_board(app):
    new_board = Board(title="Encouraging quips")
    db.session.add(new_board)
    db.session.commit()

@pytest.fixture
def one_card_belongs_to_one_board(app, one_board, one_card):
    card = Card.query.first()
    board = Board.query.first()
    board.cards.append(card)
    db.session.commit()
