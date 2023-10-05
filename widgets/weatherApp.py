from PyQt6.QtWidgets import QApplication, QMessageBox, QPushButton, QLineEdit, QWidget, QLabel, QCheckBox
from PyQt6 import QtGui
from requests import get, RequestException
class WeatherMini(QWidget):

    def __init__(self, width=600, height=600) -> None:
        super().__init__()
        self.wd = width
        self.hg = height
        self.city = None
        self.setUI()
        self.input_city.textChanged.connect(self.get_name)
        self.info.clicked.connect(self.weather_info)
        self.ext.clicked.connect(self.close)
        self.line1 = QLabel(self)
        self.line2 = QLabel(self)
        self.line3 = QLabel(self)
        self.line4 = QLabel(self)
        self.logo = QLabel(self)
    def get_name(self, args):
        self.city = args
        print(self.city)
        
    def weather_info(self):
        ob = Weather(self.city)
        wind = ob.get_city_wind_speed()
        if self.kelv.isChecked():
            temp = ob.get_city_temp()
        else:
            temp = ob.get_city_temp() + 273.15

        level = ob.get_city_weather_main()
        answer1 = "----------------------------------RESULT------------------------------"
        answer2 = f"Temperature:                           {temp:.2f}"
        answer3 = f"Weather:                               {level}"
        answer4 = f"Wind speed:                            {wind}"
        self.line1.setText(answer1)
        self.line1.setGeometry(self.width()//2 - 280, 210, 500, 40)
        self.line2.setText(answer2)
        self.line2.setGeometry(self.width()//2 - 280, 260, 500, 50)
        self.line3.setText(answer3)
        self.line3.setGeometry(self.width()//2 - 280, 320, 500, 50)
        self.line4.setText(answer4)
        self.line4.setGeometry(self.width()//2 - 280, 380, 500, 50)
        self.logo.setPixmap(QtGui.QPixmap("icons/sunny.png"))
        self.logo.setGeometry(self.width()//2 + 80, 260, 200, 150)
        self.logo.setScaledContents(True)
        
        
    def setUI(self):
        width = self.wd
        height = self.hg
        ds_width = QApplication.primaryScreen().size().width()
        ds_hght = QApplication.primaryScreen().size().height()
        self.setGeometry(ds_width//2 - width // 2,
                         ds_hght//2 - height // 2,
                         width, height)

        #city
        self.input_city = QLineEdit(self)
        self.input_city.setGeometry(self.width()// 2 - 270, 15, 540, 40)
        self.input_city.setPlaceholderText("INPUT A CITY NAME")

        #kelvin
        self.kelv = QCheckBox("KELVIN", self)
        self.kelv.setGeometry(self.width()//2 - 270, 65, 70, 35)
        self.kelv.setCheckable(True)

        #celcius
        self.celc = QCheckBox("CELCIUS", self)
        self.celc.setGeometry(self.width()//2, 65, 70, 35)

        #info
        self.info = QPushButton(self)
        self.info.setGeometry(self.width()//2 - 280, 110, 270, 55)
        self.info.setText("Get info")

        #exit
        self.ext = QPushButton(self)
        self.ext.setGeometry(self.width()//2 + 10, 110, 270, 55)
        self.ext.setText("Exit")
        btn_css = """
        QPushButton{
        border-radius:5px;
        background-color:blue;
        color:white;
        }
        """
        self.info.setStyleSheet(btn_css)
        self.ext.setStyleSheet(btn_css)

# --------weather --------------

class Weather:

    def __init__(self, city, api_key="0e8c18a7546455248891d5f0fd0641f7") -> None:
        self.city = city
        self.api_key = api_key
        self.url = "https://api.openweathermap.org/data/2.5/weather"
        self.payload = {
            "q": self.city,
        "appid": self.api_key
        }

    def get_weather_data(self):
        try:
            resp = get(self.url, params=self.payload)
            if resp.status_code == 200:
                return resp.json()
            else:
                return None 
        except RequestException as re:
            return re     

    def get_city_temp(self):
        try:
            resp = self.get_weather_data()
            if resp:
                ans = float(resp["main"]["temp"]) - 273.15
                return ans
        except RequestException as re:
            return re        


    def get_city_weather_main(self):
        try:
            resp = self.get_weather_data()
            if resp:
                ans = f"{resp['weather'][0]['main']}, Level: {resp['weather'][0]['description']}"
                return ans 
        except RequestException as re:
            return re    


    def get_city_wind_speed(self):
        try:
            resp = self.get_weather_data()
            if resp:
                ans = f"{resp['wind']['speed']}"
                return ans 
        except RequestException as re:
            return re
        