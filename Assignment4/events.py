#!flask/bin/python
from flask import jsonify, request
import ctx
from db import db

@ctx.app.route('/events', methods=['GET'])
def get_events():
    events = db.get_events()
    return ctx.success({'events': events})

@ctx.app.route('/events', methods=['POST'])
def add_event():
    data = request.json

    result = db.add_event(data)
    if not result[0]:
        return ctx.error(result[1], result[2])

    return ctx.success_created(result[1])