from flask import jsonify, Blueprint, request
from models import User, Todo, db
from app import bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt

todo_bp = Blueprint('todo_bp', __name__)

@todo_bp.route('/todos', methods=['GET'])
@jwt_required()
def get_user_todos():
    current_user = get_jwt_identity()
    user_id = current_user['id']

    todos = Todo.query.filter_by(user_id=user_id).all()

    if not todos:
        return jsonify({'error': 'You don’t have any todos available'}), 404

    return jsonify([todo.to_dict() for todo in todos]), 200


@todo_bp.route('/add_todo', methods=['POST'])
@jwt_required()
def add_todo():
    current_user = get_jwt_identity() 
    print(current_user,"ggggggg")

    data = request.get_json()
    if not data or "title" not in data or "description" not in data:
        return jsonify({"error": "Title and description are required"}), 400

    title = data['title']
    description = data['description']

    
    new_todo = Todo(
        title=title,
        description=description,
        user_id=current_user['id']  
    )

    db.session.add(new_todo)
    db.session.commit()

    return jsonify({
        "id": new_todo.id,
        "title": new_todo.title,
        "description": new_todo.description
    }), 201


@todo_bp.route('/delete/<int:todo_id>', methods=['DELETE'])
@jwt_required()
def delete_todo(todo_id):
    current_user=get_jwt_identity()
    todo=Todo.query.filter_by(id=todo_id, user_id=current_user['id']).first()

    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    

    db.session.delete(todo)
    db.session.commit()

    return jsonify({"message": "Todo deleted successfully"}), 200


        
    
    
