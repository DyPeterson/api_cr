import logging
import pandas as pd
from flask import Flask, request

logging.basicConfig(format='[%(levelname)-5s][%(asctime)s][%(module)s:%(lineno)04d] : %(message)s',
                    level=logging.INFO,
                    stream=sys.stderr)
logger: logging.Logger = logging

super_data = [
    {"name": 'Friendly Fire' , "superpower": 'Energy Bolts' , "weakness": 'Aim' },
    {"name": 'Batman' , "superpower": 'Money & Training' , "weakness": 'Trauma' },
    {"name": 'The Hulk' , "superpower": 'Radiation' , "weakness": 'Mood' }
]
super_df  = pd.DataFrame(super_data)
super_df.set_index(keys="name", drop=False, inplace=True)

app = Flask(__name__)
app.config["db"] = super_df

@app.route("/")
def index():
    index_str = """
    Welcome to heroes hideout, please orient yourself to '/see_stats' or '/add_stats'
    """
    return '', 200


@app.route('/see_stats', methods=['GET'])
def see_stats():
    """
    Query with either name, superpower and/or weakness
    """
    global super_df
    name = request.args.get('name', default=None)
    superpower = request.args.get('superpower', default=None)
    weakness = request.args.get('weakness', default=None)

    if name is not None:
        logger.info(f'name query for {name}')
        results_df = super_df.loc[super_df['name'] == name]
    else:
        results_df = super_df
    
    if superpower is not None:
        logger.info(f'superpower query for {superpower}')
        results_df = super_df.loc[super_df['superpower'] == superpower]
    else:
        results_df = super_df

    if weakness is not None:
        logger.info(f'weakness query for {weakness}')
        results_df = super_df.loc[super_df['weakness'] == weakness]
    else:
        results_df = super_df

    response_json = {
        'query_name': name,
        'query_superpower': superpower,
        'query_weakness': weakness,
        'result': results_df.to_dict(orient='records'),
    }
    
    response_headers = {
        'content-type': 'application/json'
    }

    return response_json, 200, response_headers

@app.route('/add_stats', methods=['POST'])
def add_stats():
    """
    Function to add a superhero to the database.
    """
    global super_df
    try:
        added_heroes = []
        rejected_heroes = []
        # :(
        data = request.json
        for hero in data:
            if ('name' in hero) and ('superpower' in hero) and ('weakness' in hero):
                logger.info(f'Adding a hero to the hideout, welcome {hero}')
                index = hero['name']
                super_df.loc[hero['name']] = hero
                added_heroes.append(hero)
            else:
                logger.info(f'Rejecting {hero}')
                rejected_heroes.append(hero)
        logger.info(f'Added {len(added_heroes)} heroes & Rejected {len(rejected_heroes)} heroes')
        response_json = {
            'heroes_added': len(added_heroes),
            'result': added_heroes,
            'rejects': rejected_heroes,
        }

        response_header = {
            'content-type': 'application/json'
        }

        return response_json, 200, response_header
    except Exception as error:
        return {'status': 'error', 'error_msg': str(error)}, 400, response_header

if __name__ == '__main__':
    app.run('0.0.0.0', 5050)