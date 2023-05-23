import urllib.request
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class MyApp(App):
    def build(self):
        self.label = Label(text="Температура: ")
        Clock.schedule_interval(self.update_temperature, 2)
        return self.label

    def update_temperature(self, dt):
        with urllib.request.urlopen('http://192.168.0.101/temperature') as response:
            temperature = response.read().decode('utf-8')
            self.label.text = f"Температура: {temperature} °C"

MyApp().run()
