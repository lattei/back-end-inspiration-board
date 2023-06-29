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

def test_card_message_length_exceed_limit():
    # Arrange
    max_length =  40
    message = "This is a test message that exceeds the character limit. It contains more than 40 characters."
    # Act
    result = is_message_within_limit(message, max_length)
    # Assert
    assert result == False 