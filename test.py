    
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
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
