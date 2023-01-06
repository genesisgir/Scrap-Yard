# import selenium with 'from selenium import webdriver' 
from selenium import webdriver

# create url constant for the github webpage
GITHUB_URL = 'https://github.com'


# create an object instance of the Chrome(executable_path="", service_log_path="") class from webdriver()
DRIVER = webdriver.Chrome(executable_path=r'Driver/chromedriver.exe', 
                            service_log_path=r"Log/service_logger.log")

# disable ChromeOptions() logging
def setup_options():
    
    # docstring
    """
    Removes a bunch of errors on Windows, like
    USB: usb_device_win.cc:93 Failed to read descriptors from ...
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    pass
setup_options()

# load url with the get()
DRIVER.get(GITHUB_URL)
DRIVER.maximize_window()
