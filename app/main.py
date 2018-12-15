# pylint: skip-file
from app import app
from views import views

app.run(port=5000, host='0.0.0.0')
