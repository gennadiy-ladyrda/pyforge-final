from flask.cli import FlaskGroup
import requests
import logging
from project import app, db, Compound
from project.config import baseurl, column_list, column_width
from time import sleep

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("get_data")
def get_data():
    compounds_list = ['ADP', 'ATP', 'STI', 'ZID', 'DPM', 'XP9', '18W', '29P']
    for compound in compounds_list:
        sleep(1)
        response = requests.get(url=f'{baseurl}{compound}')
        if response.status_code != 200:
            logging.error(f"Request failed. Response code: {response.status_code}")
            raise Exception("Request failed", response.status_code, response.reason)
        else:
            response_dict = response.json()
            compound_value = compound
            name_value = response_dict[compound][0]['name']
            formula_value = response_dict[compound][0]['formula']
            inchi_value = response_dict[compound][0]['inchi']
            inchi_key_value = response_dict[compound][0]['inchi_key']
            smiles_value = response_dict[compound][0]['smiles']
            cross_links_count_value = len(response_dict[compound][0]['cross_links'])

            db.session.add(Compound(compound=compound_value, name=name_value, formula=formula_value,
                                    inchi=inchi_value, inchi_key=inchi_key_value, smiles=smiles_value,
                                    cross_links_count=cross_links_count_value))
        db.session.commit()


@cli.command("print_data")
def print_data():
    sql_text = f"select {', '.join(column_list)} from compounds"
    res = db.session.execute(sql_text)
    query_list = res.fetchall()
    line_str = '-' * ((column_width + 1) * len(column_list))
    print(line_str)
    header = ''
    for name in column_list:
        header += name.ljust(column_width, ' ') + '|'
    print(header)
    print(line_str)
    for item in query_list:
        column_str = ''
        for column_value in item:
            if len(column_value) > column_width:
                column_str += column_value[:column_width - 3:].ljust(column_width, '.') + '|'
            else:
                column_str += column_value.ljust(column_width, ' ') + '|'
        print(column_str)
    print(line_str)


if __name__ == "__main__":
    cli()
