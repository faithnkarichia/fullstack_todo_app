from app import app
from models import db, User, Todo

# Run this inside app context to access Flask app + db
with app.app_context():
    print("Seeding data...")

    # Clear existing data
    Todo.query.delete()
    User.query.delete()

    # Create sample users
    user1 = User(name="Faith", email="faith@example.com", phone_number=712345678, password="secret123")
    user2 = User(name="Vincent", email="vincent@example.com", phone_number=798765432, password="openai2025")

    # Create sample todos
    todo1 = Todo(title="Buy groceries", description="Milk, Bread, Eggs", user_id=1)
    todo2 = Todo(title="Finish project", description="Finish the full-stack todo app", user_id=1)
    todo3 = Todo(title="Walk the dog", description="Evening walk", user_id=2)

    # Add to session
    db.session.add_all([user1, user2, todo1, todo2, todo3])

    # Commit to database
    db.session.commit()

    print("🌱 Seed complete!")
