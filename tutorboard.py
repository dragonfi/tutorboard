from flask import Flask, render_template, redirect
from models import db, Task, Solution
from forms import NewTaskForm, NewSolutionForm
from breadcrumbs import breadcrumbs

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'this-is-a-secret-key'

db.init_app(app)


@app.route('/')
@app.route('/task')
@app.route('/tasks')
def hello():
    breadcrumbs(['/', 'Tutorboard'], 'Tasks')
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)


@app.route('/task/<int:task_id>')
def task(task_id):
    breadcrumbs(['/', 'Tutorboard'], ['/tasks', 'Tasks'], task_id)
    form = NewSolutionForm()
    if form.validate_on_submit():
        task = Task(description=form.description.data)
        db.session.add(task)
        db.session.commit()
        return redirect('/task/{}'.format(task.id))
    task = Task.query.get(task_id)
    return render_template('task.html', task=task)


@app.route('/task/new', methods=['GET', 'POST'])
def add_task():
    breadcrumbs(['/', 'Tutorboard'], ['/tasks', 'Tasks'], 'New')
    form = NewTaskForm()
    if form.validate_on_submit():
        task = Task(description=form.description.data)
        db.session.add(task)
        db.session.commit()
        return redirect('/task/{}'.format(task.id))
    return render_template('new-task.html', form=form)


if __name__ == '__main__':
    db.create_all(app=app)
    app.run()
