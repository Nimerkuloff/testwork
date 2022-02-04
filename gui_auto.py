import pywinauto,time
import os

from pywinauto.application import Application


class PyWinAuto:
    def __init__(self):
        #TODO: disable error print when no TestCalc in memory before test launch
        os.system("taskkill /f /im  TestCalc.exe")
        self.app = Application(backend='uia').start(os.path.dirname(__file__)+"\TestCalc.exe")
        time.sleep(1)
        self.app = Application().connect(title=u'Калькулятор')

    def get_gui_elements(self):
        #app.window(best_match='Калькулятор') is equal to app.Калькулятор
        #https://pywinauto.readthedocs.io/en/latest/getting_started.html#attribute-resolution-magic
        self.app.window(best_match='Калькулятор').print_control_identifiers()

    def close_app(self):
        self.app.window().close()

