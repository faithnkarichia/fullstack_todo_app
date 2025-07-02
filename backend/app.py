from models import db
from flask  import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors  import CORS
from flask_migrate import Migrate 
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


app=Flask(__name__)
CORS(app) 

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-this'



db.init_app(app)

migrate=Migrate(app,db)
bcrypt=Bcrypt(app)
jwt = JWTManager(app)


# @app.before_first_request
# def create_tables():
#     db.create_all()



@app.route('/')
def home():
    return {'message': 'Todo App Backend Running 🎉'}


# get the blue prints
from views import *
app.register_blueprint(user_bp)
app.register_blueprint(todo_bp)




if __name__=='__main__':
    app.run(debug=True)







