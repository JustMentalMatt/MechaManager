# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     def home():
#         return render_template('home.html')

#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_maintenance.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db.init_app(app)

#     with app.app_context():
#         import models
#         db.create_all()

#     return app
