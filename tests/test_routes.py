from app.models.board import Board
from app.models.card import Card
import pytest


def test_get_cards_no_saved_cards(client):
    # Act
    response = client.get("/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_tasks_one_saved_card(client, one_card):
    # Act
    response = client.get("/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "id": 1,
            "messsage": "You got this",
            "likes_count": 0
        }
    ]

def test_get_card(client, one_card):
    # Act
    response = client.get("/card/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "card" in response_body
    assert response_body == {
        "card": {
            "id": 1,
            "messsage": "You got this",
            "likes_count": 0
        }
    }



#Tests requirements for 40char limit

def is_message_within_limit(message, max_length):
    return len(message) <= max_length

def test_card_message_length():
    # Arrange
    max_length = 40
    message = "This is a test message within the limit."
    # Act
    result = is_message_within_limit(message, max_length)
    # Assert
    assert result == True
from app.models.board import Board
import pytest

@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_boards_no_saved_boards(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_boards_one_saved_board(client, one_board):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "board_id": 1,
            "title": "Inspo board",
            "owner": "f-a-c-e"
        }
    ]


@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_goal(client, one_board):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "goal" in response_body
    assert response_body == {
        "goal": {
            "board_id": 1,
            "title": "Inspo board",
            "owner": "f-a-c-e"
        }
    }


@pytest.mark.skip(reason="test to be completed by student")
def test_get_board_not_found(client):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "There's no 1, sorry."}


@pytest.mark.skip(reason="No way to test this feature yet")
def test_create_board(client):
    # Act
    response = client.post("/boards", json={
        "title": "My New Board"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "board" in response_body
    assert response_body == {
        "board": {
            "board_id": 1,
            "title": "My New Board"
        }
    }


@pytest.mark.skip(reason="test to be completed by student")
def test_update_board(client, one_board):
    # Act
    response = client.put("/boards/1", json={
        "title": "Updated Board Title"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "board" in response_body
    assert response_body == {
        "board": {
            "board_id": 1,
            "title": "Updated Board Title"
        }
    }

@pytest.mark.skip(reason="test to be completed by student")
def test_update_board_not_found(client):
    # Act
    response = client.put("/boards/1", json={
        "title": "Updated Board Title",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Board 1 not found"}


@pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_board(client, one_board):
    # Act
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "details" in response_body
    assert response_body == {
        "details": 'Board 1 "Inspo board" successfully deleted'
    }

    # Check that the board was deleted
    response = client.get("/boards/1")
    assert response.status_code == 404
    assert response_body ==  {'details': 'Board 1 "Inspo board" successfully deleted'}


@pytest.mark.skip(reason="test to be completed by student")
def test_delete_board_not_found(client):
    # Act
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Board 1 not found"}


def test_card_message_length_exceed_limit():
    # Arrange
    max_length =  40
    message = "This is a test message that exceeds the character limit. It contains more than 40 characters."
    # Act
    result = is_message_within_limit(message, max_length)
    # Assert
    assert result == False 