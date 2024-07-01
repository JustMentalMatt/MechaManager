from mecha_manager import create_app, db
from mecha_manager.models import User

app = create_app()

with app.app_context():
    db.create_all()
    if not User.query.filter_by(email='ma@ma').first():
        new_user = User(email='ma@ma', password='password', name='ma')
        db.session.add(new_user)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
