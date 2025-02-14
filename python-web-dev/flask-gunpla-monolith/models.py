from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Gunpla(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    series = db.Column(db.String(120), nullable=False)
    grade = db.Column(db.String(50), nullable=False)
    scale = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f"<Gunpla {self.name}>"