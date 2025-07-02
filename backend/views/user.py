from flask import jsonify,Blueprint,request
from models import User,db
from app import bcrypt
from datetime import timedelta
import re 
from extensions import jwt

from flask_jwt_extended import jwt_required,get_jwt_identity,create_access_token,get_jwt

user_bp=Blueprint('user_bp', __name__)

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user=User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({'error':'user not found'}),400
    
    return jsonify(user.to_dict()),200


@user_bp.route('/signup', methods=['POST'])

def signup():
    data=request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'password' not in data or 'phone_number' not in data:
        return jsonify({'error':'name, email,password and phone number required'}),400
    
    name=data['name']
    email=data['email']
    password=data['password']
    phone_number=data['phone_number']

    # validations
    if not re.fullmatch(r'^[^@]+@[^@]+\.[^@]+$', email):
            return jsonify({'error': 'Invalid email format'}), 400
    if User.query.filter_by(email=email).first():
         return jsonify({'error':'user already exists'}),400
    
    hashed_password=bcrypt.generate_password_hash(data['password']).decode('utf-8')

    new_user=User(
         name=name,
         email=email,
         phone_number=phone_number,
         password=hashed_password
    )


    db.session.add(new_user)
    db.session.commit()





    return jsonify({'message':'user created successifully please log in'})





@user_bp.route('/user/login', methods=['POST'])
def login():
    data=request.get_json()

    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'email and password required'}),400
    
    email=data['email'].strip().lower()
    password=data['password']

    user= User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'error':'invalid email or password'}),400
    
    access_token=create_access_token(
        identity={'id':user.id,'name':user.name,'email':user.email},
        expires_delta=timedelta(hours=24)
    )

    return jsonify({'access_token': access_token}), 200







