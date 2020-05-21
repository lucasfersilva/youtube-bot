from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

class youtube_bot():

    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("--window-position=0,0")
        options.add_argument("--headless")

        PROXY = "216.244.74.138:19006"
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
            "noProxy": None,
            "proxyType": "MANUAL",
            "autodetect": False
        }
        self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=options)

    def open_youtube_video(self):
        time.sleep(3)
        #paste youtube inside of self.driver.get
        self.driver.get("https://www.youtube.com/watch?v=zwvWrHdw7tU&feature=youtu.be")
        time.sleep(2)
        print("ok")


    def close_youtube_video(self):
        self.driver.close()


while True:
    a = youtube_bot()
    a.open_youtube_video()
    time.sleep(130)
    a.close_youtube_video()
    time.sleep(190)
    #second
    a.open_youtube_video()
    time.sleep(200)
    a.close_youtube_video()
    time.sleep(120)
    # third
    a.open_youtube_video()
    time.sleep(150)
    a.close_youtube_video()
    time.sleep(170)
    # third
    a.open_youtube_video()
    time.sleep(150)
    a.close_youtube_video()
    time.sleep(170)
    # fourth
    a.open_youtube_video()
    time.sleep(300)
    a.close_youtube_video()
    time.sleep(20)
    # fifth
    a.open_youtube_video()
    time.sleep(280)
    a.close_youtube_video()
    time.sleep(40)
    # sixth
    a.open_youtube_video()
    time.sleep(260)
    a.close_youtube_video()
    time.sleep(60)
    # seventh
    a.open_youtube_video()
    time.sleep(400)
    a.close_youtube_video()
    time.sleep(40)
    # eigth
    a.open_youtube_video()
    time.sleep(110)
    a.close_youtube_video()
    time.sleep(210)
    # nineth
    a.open_youtube_video()
    time.sleep(120)
    a.close_youtube_video()
    time.sleep(200)
    # tenth
    a.open_youtube_video()
    time.sleep(180)
    a.close_youtube_video()
    time.sleep(200)

