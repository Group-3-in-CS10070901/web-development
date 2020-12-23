
import os
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.before_first_request
def create_db():
    db.create_all()

if __name__ == '__main__':
    app.run()
