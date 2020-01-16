import psutil

import SH1106
import time
from RPi import GPIO
from Menu import Menu
from screen_off import ScreenOff
from show_info import ShowInfo
from show_ip import ShowIP

RST_PIN        = 25
CS_PIN         = 8
DC_PIN         = 24

KEY_UP_PIN     = 6
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13

KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16
PINS = [6, 19, 5, 26, 13, 21, 20, 16]

class Driver():
    def __init__(self):
        self.disp = SH1106.SH1106()
        self.disp.init()
        self.disp.clear()
        self.target = None
        GPIO.setmode(GPIO.BCM)
        for PIN in PINS:
            GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(PIN, GPIO.FALLING, callback=self.keyboard_handler, bouncetime=300)

    def keyboard_handler(self, PIN):
        if PIN == KEY_UP_PIN:
            self.target.on_up()
        elif PIN == KEY_DOWN_PIN:
            self.target.on_down()
        elif PIN == KEY_LEFT_PIN:
            self.target.on_left()
        elif PIN == KEY_RIGHT_PIN:
            self.target.on_right()
        elif PIN == KEY_PRESS_PIN:
            self.target.on_center()
        elif PIN == KEY1_PIN:
            self.target.on_KEY1()
        elif PIN == KEY2_PIN:
            self.target.on_KEY2()
        else:
            if self.target.parent is not None:
                self.bind_class(self.target.parent)

    def bind_class(self, target, init=False):
        if self.target is not None:
            self.unbind_class()
        self.target = target
        target.on_enter()
        target.disp = self
        target.render()

    def unbind_class(self):
        self.target.disp = None
        self.target = None

    def refresh(self):
        self.disp.show_image(self.disp.get_buffer(self.target.buffer))

    def run(self):
        try:
            while True:
                time.sleep(10000)
        except:
            GPIO.cleanup()

menu = Menu([ShowIP(), ShowInfo(), ScreenOff()])
menu.render()
d = Driver()
d.bind_class(menu, True)
d.run()

