from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    solutions = db.relationship('Solution', backref='task', lazy=True)

    def __repr__(self):
        return 'Task({},"{}...")'.format(self.id, self.description[:10])


class Solution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    solution = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return 'Solution({}, {}, "{}...")'.format(
            self.id, task_id, self.solution[:10])
