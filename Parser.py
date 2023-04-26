from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep
from os import rename, getcwd, listdir


class Parser(object):

    def __init__(self):
        self.names_of_supported_files = None
        self.supported_vidio_files = None
        self.PATH = getcwd() + r"\chromedriver.exe"
        self.link = r"https://x2download.com"
        self.headers = {
            "Accept": "* / *",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                          " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }

        self.location = getcwd()
        if __name__ != "__main__":
            self.location += "\\"

        self.new_vidio_location = self.location

    def __call__(self, vidio_link, new_vidio_name, mp3=False):

        options = Options()

        options.add_experimental_option("prefs", {
            "download.default_directory": f"{self.location}",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        self.driver = webdriver.Chrome(executable_path=self.PATH, options=options)
        self.driver.maximize_window()
        self.driver.get(self.link)

        input_link_label = self.driver.find_element(by=By.ID, value="s_input")
        input_link_label.send_keys(vidio_link)

        self.driver.find_element(by=By.ID, value="search-form").find_element(by=By.TAG_NAME, value="button").click()
        sleep(1)
        # next
        opt = self.driver.find_element(by=By.ID, value='formatSelect')
        select = Select(opt)
        t_opt = select.options
        select = Select(self.driver.find_element(by=By.ID, value='formatSelect'))
        if mp3:
            select.select_by_index(len(t_opt) - 1)
        else:
            select.select_by_index(0)

        # download vidio
        self.driver.find_element(by=By.ID, value="btn-action").click()

        while True:
            try:
                self.driver.find_element(by=By.ID, value="asuccess").click()
                break
            except Exception as ex:
                print(ex)
                sleep(1)

        self.driver.minimize_window()
        self.settings_of_file(new_name=new_vidio_name)

        return new_vidio_name

    def settings_of_file(self, new_name="new_vidio.mp4"):
        while True:
            self.supported_vidio_files = listdir(self.new_vidio_location)
            self.names_of_supported_files = [i for i in self.supported_vidio_files if
                                             i[-4:] == ".mp4" and "X2Download.com" in i]
            if len(self.names_of_supported_files) != 0:
                break
            sleep(2)

        rename(
            self.new_vidio_location + "\\" + self.names_of_supported_files[0],
            self.new_vidio_location + "\\" + new_name
        )


if __name__ == "__main__":
    parser = Parser()
    parser('https://www.youtube.com/watch?v=jfgJQ42FN1Q', 'vdfv.mp4')
