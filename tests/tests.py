import unittest
import  sqlite3
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pathlib import Path

pat = str(Path(__file__).parent.parent)

class TestReadFromDb(unittest.TestCase):
    def test1(self):
        #at least 10 records are stored in the db
        con = sqlite3.connect(pat + '\\database//scraping_data.db')
        cur = con.cursor()
        querry = "SELECT * from products LIMIT 10"
        v = cur.execute(querry).fetchall()
        self.assertEqual(len(v), 10)
    def test2(self):
        #test the webdriver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.facebook.com/RealMadrid/")
        v =driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/span/h1")[0].text
        driver.close()
        self.assertEqual(v, 'Real Madrid C.F.')

#python -m unittest     tests.tests.TestReadFromDb
if __name__ == '__main__':
    TestReadFromDb