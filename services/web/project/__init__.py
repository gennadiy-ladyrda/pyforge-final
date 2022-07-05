from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Compound(db.Model):
    __tablename__ = "compounds"

    id = db.Column(db.Integer, primary_key=True)
    compound = db.Column(db.String(4000), nullable=False)
    name = db.Column(db.String(4000), nullable=False)
    formula = db.Column(db.String(4000), nullable=False)
    inchi = db.Column(db.String(4000), nullable=False)
    inchi_key = db.Column(db.String(4000), nullable=False)
    smiles = db.Column(db.String(4000), nullable=False)
    cross_links_count = db.Column(db.String(4000), nullable=False)

    def __init__(self, compound, name, formula, inchi, inchi_key, smiles, cross_links_count):
        self.compound = compound
        self.name = name
        self.formula = formula
        self.inchi = inchi
        self.inchi_key = inchi_key
        self.smiles = smiles
        self.cross_links_count = cross_links_count


if __name__ == '__main__':
    app.run(debug=True)
