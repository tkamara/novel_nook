from flask import Flask, render_template, redirect, url_for, request, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Create a User class for Flask-Login
class User(UserMixin):
    pass

# User loader function for Flask-Login
@login_manager.user_loader
def load_user(username):
    user_data = db.users.find_one({"username": username})
    if not user_data:
        return None
    user = User()
    user.id = username
    return user

# Establish connection to MongoDB
# client = MongoClient('localhost', 27017)
# client = MongoClient("mongodb://devopshint:devopshint@127.0.0.1:27017/book_catalog")
client = MongoClient("mongodb://devopshint:devopshint@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.1")
db = client['novel_nook']

# Route for login page
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user_data = db.users.find_one({"username": username})
        if user_data and check_password_hash(user_data['password'], password):
            user = User()
            user.id = username
            login_user(user)
            return redirect(url_for('home'))
        else:
            return render_template('register.html')
    return render_template('login.html')

# Route for user registration
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Check if the username is already taken
        existing_user = db.users.find_one({"username": username})

        if existing_user:
            return render_template('register.html', error="Username already taken. Choose another.")

        # If username is not taken, hash the password and add the new user to the database
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        db.users.insert_one({"username": username, "password": hashed_password})

        user = User()
        user.id = username
        login_user(user)

    return render_template('register.html')

# Route for logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# Route page for index
@app.route('/')
def index():
    return render_template('index.html')

# Route for home page
@app.route('/home')
@login_required
def home():
    return render_template('home.html')
    # if 'username' in session:
      #  return render_template('home.html')
    # return redirect(url_for('index'))

# Route to add a book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    success_message = "Successfully added the book!"
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        # Associate the book with the current user
        db.books.insert_one({"title": title, "author": author, "genre": genre, "user": current_user.id})
        return redirect(url_for('book_list', success_message=success_message))
    return render_template('add_book.html')

# Route to display the book list
@app.route('/books')
def book_list():
    # Fetch books associated with the current user
    books = db.books.find({"user": current_user.id})
    success_message = request.args.get('success_message', None)
    return render_template('book_list.html', books=books, success_message=success_message)

# Route to delete a book
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    db.books.delete_one({"_id": ObjectId(book_id)})
    return redirect(url_for('book_list'))

# Route to search for books
@app.route('/search_books', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        search_term = request.form.get('search_term', '').strip()

        # Validate search_term
        if not search_term:
            return render_template('search_results.html', error='Please enter a search term')

        # Use regex for case-insensitive partial matching
        regex_pattern = {"$regex": search_term, "$options": "i"}

        books = db['books'].find({
            "$or": [
                {"title": regex_pattern},
                {"author": regex_pattern},
                {"genre": regex_pattern}
            ]
        })

        return render_template('search_results.html', books=books, search_term=search_term)

    return render_template('search_results.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
