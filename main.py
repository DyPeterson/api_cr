import pandas as pd
from flask import Flask, request

super_data = [
    {"name": '' , "superpower": '' , "weakness": '' },
    {"name": '' , "superpower": '' , "weakness": '' },
    {"name": '' , "superpower": '' , "weakness": '' }
]
super_df  = pd.DataFrame(super_data)
super_df.set_index(keys="name", drop=False, inplace=True)

app = Flask(__name__)
app.config["db"] = super_df

@app.route('/see_stats', methods=['GET'])
def see_stats():
    pass

@app.route('/add_stats', methods=['POST'])
def add_stats():
    pass

if __name__ == '__main__':
    app.run('0.0.0.0', 5050)