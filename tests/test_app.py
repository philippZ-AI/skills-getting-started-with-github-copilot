from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    email = "student@example.com"

    post_response = client.post(f"/activities/Chess Club/signup?email={email}")
    assert post_response.status_code == 200

    delete_response = client.delete(f"/activities/Chess Club/signup?email={email}")
    assert delete_response.status_code == 200

    response = client.get("/activities")
    assert email not in response.json()["Chess Club"]["participants"]
