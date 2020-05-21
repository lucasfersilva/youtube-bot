from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from RC import RC


class youtube_bot():

    def __init__(self):
        
        opttions = Options()
        
        options.add_experimental_option("detach", True)
        options.add_argument("--headless")
        PROXY = "216.244.74.138:19006"
        options.add_argument('--proxy-server=%s' % PROXY)
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
            "noProxy": None,
            "proxyType": "MANUAL",
            "autodetect": False
        }
        self.driver = webdriver.Chrome(executable_path=RC.chromedriver_path,options=options)
        self.driver.get(RC.youtube_link)

    def open_youtube_video(self):
        time.sleep(20)
        #paste youtube inside of self.driver.get
        try:
            self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button').click()
            print('Video running')
        except:
            pass
        time.sleep(2)
        print("ok")


    def close_youtube_video(self):
        self.driver.refresh()


while True:
    a = youtube_bot()
    a.open_youtube_video()
    time.sleep(310)
    a.close_youtube_video()
    time.sleep(310)






