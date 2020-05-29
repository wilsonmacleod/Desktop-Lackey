import json

from flask import jsonify
from flask_restful import Resource

from .. import logger
from ..models import db, Note

class NOTES(Resource): # '/Notes/<arg> (None if none)
    def get(self, arg):
        data = Note.query.all()
        return jsonify(status=200, text={'data': f'{data}'}) 
    
    def post(self, arg):
        j = json.loads(arg)
        if j['id'] != '':
            note = Note.query.filter_by(id=j['id']).first()
            db.session.delete(note)
            new  = Note(
            id=j['id'],
            text=j['text'],
            color=j['color'] 
                    )
        else:
            new  = Note(
            text=j['text'],
            color=j['color'] 
                    )
        db.session.add(new)
        db.session.commit()
        logger.debug(f'NOTES.POST: {new}')
        return jsonify(status=200)

    def delete(self, arg):
        note = Note.query.filter_by(id=arg).first()
        db.session.delete(note)
        db.session.commit()
        logger.debug(f'Note.DELETE: {note}')
        return jsonify(status=200)