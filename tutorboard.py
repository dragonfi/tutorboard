from flask import Flask, render_template, redirect, request
from models import db, Task, Solution
from breadcrumbs import breadcrumbs

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'this-is-a-secret-key'

db.init_app(app)


@app.route('/')
@app.route('/tasks')
def hello():
    breadcrumbs(['/', 'Tutorboard'], 'Tasks')
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)


@app.route('/tasks/<int:task_id>')
def task(task_id):
    breadcrumbs(['/', 'Tutorboard'], ['/tasks', 'Tasks'], task_id)
    task = Task.query.get(task_id)
    return render_template('task.html', task=task)


@app.route('/tasks/<int:task_id>/solutions/new', methods=['POST'])
def add_solution(task_id):
    description = request.form['description']
    solution = Solution(task_id=task_id, description=description)
    db.session.add(solution)
    db.session.commit()
    return redirect('/tasks/{}'.format(task_id))


@app.route('/tasks/new', methods=['POST'])
def add_task():
    description = request.form['description']
    task = Task(description=description)
    db.session.add(task)
    db.session.commit()
    return redirect('/tasks')


if __name__ == '__main__':
    db.create_all(app=app)
    app.run()
