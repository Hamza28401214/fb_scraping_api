import sqlite3
from pathlib import Path

pat = str(Path(__file__).parent)


def to_db(df, name):
    con = sqlite3.connect('database//scraping_data.db')
    df.to_sql(con=con, name=str(name), if_exists='replace')
    con.close()
    return
# def from_db():
#     con = sqlite3.connect(pat + '\\database//scraping_data.db')
#     res = pd.read_sql_query("SELECT * from about", con)
#     res.drop('index', axis=1, inplace=True)
#     res = res.to_json(orient='records')
#     con.close()
#     return res
