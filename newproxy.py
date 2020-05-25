from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from RC import RC

class youtube_bot():

    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)

        PROXY = "163.172.221.119:19002"
        self.options.add_argument('--proxy-server=%s' % PROXY)
        self.options.add_arguments("--no-sandbox");
        self.options.add_argument('--disable-dev-shm-usage')
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
            "noProxy": None,
            "proxyType": "MANUAL",
            "autodetect": False
        }
        self.driver = webdriver.Chrome(executable_path=RC.chromedriver_path, options=self.options)
        self.driver.get(RC.youtube_link)


    def open_youtube_video(self):

        time.sleep(30)
        #paste youtube inside of self.driver.get
        try:
            self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button').click()
            print('Video running')
        except:
            pass
        time.sleep(2)
        print("Video is playing")
        self.driver.refresh()

    def close_youtube_video(self):
        self.driver.refresh()


while True:

        a = youtube_bot()
        a.open_youtube_video()
        time.sleep(30)
        print("Ran 1 time")
        a.close_youtube_video()
        time.sleep(30)
        print("It ran 1 more time successfully")






