from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'your_secret_key_here'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=True)
    assigned_to = db.Column(db.String(50), nullable=True)
    assigned_by = db.Column(db.String(50), nullable=True)
    is_done = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default='Active')  # New status column

    def __repr__(self):
        return f'<Task {self.id} - {self.title}>'


# Initialize the database
with app.app_context():
    db.create_all()



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You need to log in first.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    sort_by = request.args.get('sort', 'date')
    username = session['username']  # Retrieve the username from session
    if sort_by == 'title':
        tasks_assigned_to = Task.query.filter_by(assigned_to=username).order_by(Task.title).all()
        tasks_assigned_by = Task.query.filter_by(assigned_by=username).order_by(Task.title).all()
    else:
        tasks_assigned_to = Task.query.filter_by(assigned_to=username).order_by(Task.date).all()
        tasks_assigned_by = Task.query.filter_by(assigned_by=username).order_by(Task.date).all()
    completed_tasks = Task.query.filter_by(is_done=True).order_by(Task.date).all()
    return render_template('index.html', tasks_assigned_to=tasks_assigned_to, tasks_assigned_by=tasks_assigned_by)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    date = request.form['date']
    assigned_to = request.form.get('assigned_to', '')  # Now this stores username
    assigned_by = session.get('username')  # Now this stores username
    try:
        task_date = datetime.strptime(date, '%Y-%m-%d').date() if date else None
        new_task = Task(title=title, date=task_date, assigned_to=assigned_to, assigned_by=assigned_by)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
    except ValueError:
        flash('Invalid date format. Please use YYYY-MM-DD.', 'error')
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        assigned_to = request.form.get('assigned_to', '')  # Optional
        assigned_by = request.form.get('assigned_by', '')  # Optional
        try:
            task.date = datetime.strptime(date, '%Y-%m-%d').date() if date else None
            task.title = title
            task.assigned_to = assigned_to
            task.assigned_by = assigned_by
            db.session.commit()
        except ValueError:
            pass  # Handle invalid date format gracefully
        return redirect(url_for('index'))
    return render_template('update.html', task=task)

@app.route('/mark_done/<int:task_id>')
def mark_done(task_id):
    task = Task.query.get_or_404(task_id)
    if task.assigned_to == session['username']:
        task.is_done = True
        task.status = 'Done'
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/mark_in_progress/<int:task_id>')
def mark_in_progress(task_id):
    task = Task.query.get_or_404(task_id)
    if task.assigned_to == session['username']:
        task.is_done = False
        task.status = 'In Progress'
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
