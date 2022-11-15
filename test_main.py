from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to Maca api"


def test_upload_csv():
    response = client.post(
        "/upload",
        json={"url": "https://res.cloudinary.com/tracysoft/raw/upload/v1668531896/y46l0zjmqowfwzrhgnfn.csv"},
    )
    assert response.status_code == 200
    assert type(response.json()) is list

def test_upload_xlsx():
    response = client.post(
        "/uploadexcel",
        json={"url": "https://res.cloudinary.com/tracysoft/raw/upload/v1668533276/bgfolb93bntiwagl743l.xlsx"},
    )
    assert response.status_code == 200
    assert type(response.json()) is list


