from app import db
from datetime import datetime

class MyTable(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    item  = db.Column(db.String(32))
    value = db.Column(db.Float)
    stamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
         return '{}: {} = {} at {}'.format(self.id, self.item, self.value, self.stamp)
