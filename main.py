import kivy
import threading
import time
import math
import pickle

from kivy.config import Config
Config.set('graphics', 'resizable', False)
#Config.set('kivy', 'window_icon', 'Icons/top_icon.png')

from kivy.core.window import Window
from kivy.app import App
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

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

maxx = 0.0
sim = True
wait = 0.2


def opacity(cases, c):
    global maxx
    if cases < 0:
        cases = 0
    pp = ((float(cases)/pop[st_code[c + 1]]) * 520)**0.4
    return pp


class Covid_19_Visual(App):
    def initialize(self):
        pass

    def build(self):
        return Builder.load_file("design.kv")

    def slid(self, ss, states, rev1):
        global data
        # print(max)
        for c in range(len(states)):
            state = states[c]
            state.color = (1, 1, 1, opacity(data[st_code[c+1]][int(ss.value)], c))
        rev1.pos = (900 + 250 * ss.value/497, 0)
        # print(rev1.pos_hint['right'])

    def pl(self, pp):
        global sim
        if pp.text == 'Play':
            pp.text = 'Pause'
            sim = True
        else:
            pp.text = 'Play'
            sim = False

    def sped(self, lab):
        global wait
        if lab == 'x1':
            wait = 0.2
        if lab == 'x2':
            wait = 0.1
        if lab == 'x4':
            wait = 0.05
        if lab == 'x8':
            wait = 0.025
        if lab == 'x16':
            wait = 0.0125

    def simu(self, slid, pp):
        global sim
        global wait
        if sim:
            for i in range(int(slid.value), 498):
                if sim == False:
                    break
                slid.value = i
                time.sleep(wait)
            if pp.text == 'Pause':
                pp.text = 'Play'



Covid_19_Visual().run()
print("Exitted!")
