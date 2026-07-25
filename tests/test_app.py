from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    # Arrange
    email = "student@example.com"
    activity_name = "Chess Club"

    # Act
    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    delete_response = client.delete(f"/activities/{activity_name}/signup?email={email}")
    assert delete_response.status_code == 200

    activities_response = client.get("/activities")
    activities = activities_response.json()

    # Assert
    assert email not in activities[activity_name]["participants"]
