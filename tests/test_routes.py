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
            "title": "Encouraging quips"
        }
    ]


@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_goal(client, one_goal):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "goal" in response_body
    assert response_body == {
        "goal": {
            "board_id": 1,
            "title": "Encouraging quips"
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
        "details": 'Board 1 "Encouraging quips" successfully deleted'
    }

    # Check that the board was deleted
    response = client.get("/boards/1")
    assert response.status_code == 404
    assert response_body ==  {'details': 'Board 1 "Encouraging quips" successfully deleted'}


@pytest.mark.skip(reason="test to be completed by student")
def test_delete_board_not_found(client):
    # Act
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Board 1 not found"}


@pytest.mark.skip(reason="No way to test this feature yet")
def test_create_board_missing_title(client):
    # Act
    response = client.post("/boards", json={})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        "details": "Invalid data"
    }