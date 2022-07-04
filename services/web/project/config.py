import os


basedir = os.path.abspath(os.path.dirname(__file__))
baseurl = 'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/'
column_list = ['compound', 'name', 'formula', 'inchi', 'inchi_key', 'smiles', 'cross_links_count']



class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
