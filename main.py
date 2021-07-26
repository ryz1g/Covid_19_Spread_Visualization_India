import kivy
import threading
import time
import pickle

from kivy.core.window import Window
from kivy.app import App
from kivy.graphics import Color,RoundedRectangle
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen


from kivy.config import Config
Config.set('graphics', 'resizable', False)
#Config.set('kivy', 'window_icon', 'Icons/top_icon.png')


Window.size = (1150, 800)
Window.clearcolor = (40/255, 40/255, 40/255, 1)

f = open("data.pkl", "rb")
data = pickle.load(f)
f.close()

f = open("max.pkl", "rb")
max = pickle.load(f)
f.close()

f = open("codes.pkl", "rb")
st_code = pickle.load(f)
f.close()

f = open("pop.pkl", "rb")
pop = pickle.load(f)
f.close()

maxxxx = 68631


def opacity(cases, c):
    pp = ((float(cases)/pop[st_code[c+1]])/0.00061074) * 1.5
    return pp


class Covid_19_Visual(App):
    def initialize(self):
        pass

    def build(self):
        return Builder.load_file("design.kv")

    def slid(self, ss, states):
        global data
        # print(max)
        for c in range(len(states)):
            state = states[c]
            state.color = (1, 1, 1, opacity(data[st_code[c+1]][int(ss.value)], c))


Covid_19_Visual().run()
print("Exitted!")
