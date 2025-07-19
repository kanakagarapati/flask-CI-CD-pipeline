from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Hello this is Kanaka Manoj Garapati pushed code to check auto trigger Jenkins- deployment via jenkins pipeline Flask App!--Test" in response.data
