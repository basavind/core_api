from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core_api.models import Material, Slice, Base
from rest.endpoints import create_api, register_all_apis


engine = create_engine('sqlite:////tmp/test.db')
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()
app = Flask(__name__)


apis, schema = create_api(
    Material, session
)
register_all_apis(app, schema, (apis,))
app.run()
