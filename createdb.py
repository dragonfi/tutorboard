#!/usr/bin/python3
from tutorboard import db

db.drop_all()
db.create_all()
