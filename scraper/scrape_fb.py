from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from pathlib import Path

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# setup chrome driver and get url

p = str(Path(__file__).parent)


# def get_browser():
#     options = webdriver.ChromeOptions()
#     browser = webdriver.Remote(
#             command_executor=f"http://localhost:4444/wd/hub",
#             desired_capabilities=DesiredCapabilities.CHROME,
#             options=options,
#         )
#     return browser


class _webdirver_:

    def __init__(self):
        self.set_up()
        # self.get_about()
        # self.get_products()

    def set_up(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(ChromeDriverManager(path=p).install(), chrome_options=chrome_options)
        # chrome_path = str(p)+'/chromedriver.exe'
        # self.driver = webdriver.Chrome(executable_path=chrome_path)
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # self.driver = webdriver.Remote(command_executor=f"http://localhost:4444/wd/hub",
        #     desired_capabilities=DesiredCapabilities.CHROME)
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def get_about(self):
        driver = self.driver

        driver.get("https://www.facebook.com/RealMadrid/about")
        # time.sleep(5)
        # driver.find_elements_by_xpath(
        #     "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div/div/div/div/div/span/div/div[2]/div/div[2]/div/div/a/span")[
        #     0].click()
        time.sleep(3)
        try:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)

            if len(driver.find_elements_by_xpath("//*[@class='h28iztb5 s8sjc6am facqkgn9 b0ur3jhr']")) != 0:
                driver.find_elements_by_xpath("//*[@class='h28iztb5 s8sjc6am facqkgn9 b0ur3jhr']")[0].click()
                pass
            likes = driver.find_elements_by_xpath("//*[@class='jcxyg2ei cqf1kptm alzwoclg']")[0].text
            followers = driver.find_elements_by_xpath(
                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div/span/span")[
                0].text
            visitors = driver.find_elements_by_xpath(
                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/div[1]/div/div[4]")[
                0].text
            if len(driver.find_elements_by_xpath(
                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/div[3]/div/div[3]/div[1]/div/div/div/div[2]/div/div/span/div/div[2]/span/div/div/div")) != 0:
                time.sleep(2)
                driver.find_elements_by_xpath(
                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/div[3]/div/div[3]/div[1]/div/div/div/div[2]/div/div/span/div/div[2]/span/div/div/div")[
                    0].click()
            other_infos = driver.find_elements_by_xpath(
                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/div[3]/div/div[3]/div[1]/div/div/div/div[2]/div/div/span/div/div[2]/span/div[1]/div")[
                0].text
            about = {"likes": [likes], "visitors": [visitors], 'followers': [followers], 'other': [other_infos]}
        except Exception as e:
            print(e)
            return about
        print(about)
        return about

    def get_products(self):

        self.driver.get("https://www.facebook.com/RealMadrid/shop/?ref_code=mini_shop_page_card_cta&ref_surface=page")
        time.sleep(2)
        ur = self.driver.find_elements_by_xpath(
            "//*[@class='bdao358l ozxw8sh7 cgu29s5g i15ihif8 srn514ro b0eko5f3 ez8dtbzv fwlpnqze rodvbr0x']")
        len(ur)
        article = {'info': [], 'urls': []}
        for i in range(len(ur)):
            try:
                article['urls'].append(self.driver.find_elements_by_xpath(
                    '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div/div[' + str(
                        i + 1) + "]/div/div/a/div/div[1]/div[1]/div/img")[0].get_attribute("src"))
                article['info'].append(ur[i].text)
                # urllib.request.urlretrieve(url,'tessta.png') to save images
            #         driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #scroll down
            except Exception as e:
                self.driver.close()
                return article

        print(article)
        self.driver.close()
        return article

    # def quit_browser(self):
    #     self.driver.close()
