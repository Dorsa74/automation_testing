from hello import app
with ap.test_client() as c:
  response = c.get('/')
  assert response.data == b'Hello World!'
  assert response.status_code == 200


