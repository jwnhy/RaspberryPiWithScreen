from App import App

class ScreenOff(App):
    def __init__(self):
        super().__init__(name="Screen Off")

    def render(self):
        self.draw.rectangle(((0, 0),(127, 63)), fill=1)
        if self.driver is not None:
            self.driver.refresh()