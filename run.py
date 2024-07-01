from mecha_manager import create_app, db
from mecha_manager.models import User

app = create_app()

with app.app_context():
    db.create_all()
    if not User.query.filter_by(email='test@example.com').first():
        new_user = User(email='test@example.com', password='password', name='Test User')
        db.session.add(new_user)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
