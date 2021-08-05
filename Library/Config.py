import os
class Config:
    project_dir = os.getcwd().split('Tests')[0]
    data_file_path = project_dir+'Data/TestData.xlsx'
    objects_file_path = project_dir+'Data/Objects.xlsx'

    URL = r'https://www.makemytrip.com/'
    BROWSER_NAME = "chrome"
    USERNAME = ""
    PASSWORD = ""
    FIREFOX_DRIVER_PATH = r""
    GECKO_DRIVER_PATH = r""
    CHROME_DRIVER_PATH = "../Library/chromedriver"
    IE_DRIVER_PATH = r""
    DATA_FILE_PATH = data_file_path
    OBJECTS_FILE_PATH = objects_file_path