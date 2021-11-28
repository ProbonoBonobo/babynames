# manage.py

from flask_script import Manager

from babynames.app import app
from babynames.database import db
import pdb
import pandas as pd

manager = Manager(app)

@manager.command
def hello():
    print("hello")
    result = db.engine.execute("select * from NationalNames LIMIT 5;")
    print(result.fetchall())

@manager.command
def db_shell():
    while True:
        try:
            cmd = input("sql> ")
            if cmd == "exit":
                break
            result = db.engine.execute(cmd)
            print(result.fetchall())
        except Exception as e:
            print(f"{e.__class__.__name__} while executing {cmd} ::  {e}. Check your syntax and make sure your identifiers correctly refer to the columns defined in the table schema.")

@manager.command
def plot():
    result = db.engine.execute("select year, name, sum(count) from NationalNames where name = 'Tequila' group by year, name;")
    by_year = {'Tequila': defaultdict(int)}
    for year, name, births in result:
        by_year['Tequila'][year] += births
    xs = []
    ys = []

    for name, year in by_year.items():
        for year, births in year.items():
            xs.append(year)
            ys.append(births)


    fig = go.Figure()
    for i, name in enumerate(dims):
        fig.add_trace(go.Scatter(x=xs, y=ys, name=name, fill='tozeroy', groupnorm='percent'))  # fill down to xaxis
    fig.update_layout(hovermode='x unified')
    # fig.update_traces(hovertemplate)

    fig = px.area(df, x='year', y=dims)
    fig.update_xaxes(
            dtick='Y5',
            tickformat='%Y',
    )
    return decapitate(fig)

if __name__ == "__main__":
    manager.run()
