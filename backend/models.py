from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique = False, nullable=False) # max length of 80; can't pass null
    last_name = db.Column(db.String(80), unique = False, nullable=False)
    email = db.Column(db.String(120), unique = True, nullable=False)

    def to_json(self): #take fields above -> dictionary -> json
        return {
            'id': self.id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
        }
