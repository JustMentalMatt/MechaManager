    
# simple login credential save cookies

    # app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    
    # @app.route('/')
    # def index():
    #     if 'username' in session:
    #         return f'Logged in as {session["username"]}'
    #     return 'You are not logged in'

    # @app.route('/login', methods=['GET', 'POST'])
    # def login():
    #     if request.method == 'POST':
    #         session['username'] = request.form['username']
    #         return redirect(url_for('index'))
    #     return '''
    #         <form method="post">
    #             <p><input type=text name=username>
    #             <p><input type=submit value=Login>
    #         </form>
    #     '''

    # @app.route('/logout')
    # def logout():
    #     # remove the username from the session if it's there
    #     session.pop('username', None)
    #     return redirect(url_for('index'))
    
    
# def create_app():
#     app = Flask(__name__)

    # @app.route('/home')
    # def home():
    #     return render_template('home.html', name="World")

    # # mataibhse.net/about/(username) | <path:subpath> <int:post_id>
    # @app.route('/about/<username>')
    # def about(username):
    #     return f'About page: {username}'
    
# Ensure db is initialized only once
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

from werkzeug.security import check_password_hash, generate_password_hash

password = generate_password_hash('testuser', method='scrypt')
print(password)

print(check_password_hash('scrypt:32768:8:1$L32vhtHIIWmnnavq$11855a358893ac38dcc58524cf048ff2d5028ed31fbfd6195f0f0099d62a00c76e8e9545e79a7e401fea9150ec3eae4da72a5e7ad4b9579af2610b5ab9d98cfe', 'testuser'))