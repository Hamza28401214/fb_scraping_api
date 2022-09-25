from fastapi import FastAPI
import pandas as pd
from scraper.scrape_fb import _webdirver_
import logging
import uvicorn
import time

from utils import *

logging.basicConfig(filename='logs/record.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "welcome to our scraping api"}


@app.get("/scraping")
async def scrape():
    myWebsite = _webdirver_()
    # get page details
    about = myWebsite.get_about()
    time.sleep(1)
    products = myWebsite.get_products()

    # myWebsite.tearDown()
    # prepare data
    df_about = pd.DataFrame(about)
    df_products = pd.DataFrame(products)
    df_products['price'] = df_products['info'].apply(lambda x: x.split('\n')[-1])
    df_products['info'] = df_products['info'].apply(lambda x: x.split('\n')[0])
    logging.info("data successfully extracted from fb")
    # # Save data to SQLite database
    to_db(df_about, 'about')
    to_db(df_products, 'products')
    logging.info("data successfully stored in db")
    return {"message": "Scraping completed"}


@app.get("/get_data")
async def from_db():
    con = sqlite3.connect(pat + '\\database//scraping_data.db')
    res = pd.read_sql_query("SELECT * from about", con)
    res.drop('index', axis=1, inplace=True)
    print(res['likes'])
    # res = res.to_json(orient='records')
    con.close()
    return {'Details': 'Real Madrid FC', 'Number of likes': res['likes'], 'Followers': res['followers'],
            'Other details': res['other']}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
