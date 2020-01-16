from PIL import ImageFont, ImageDraw, Image

class App():
    def __init__(self, parent=None, name='APP'):
        self.height = 64
        self.width = 128
        self.buffer = Image.new('1', (self.width, self.height), "WHITE")
        self.draw = ImageDraw.Draw(self.buffer)
        self.font = ImageFont.truetype('Font.ttf')
        self.parent = parent
        self.name = name
        self.driver = None

    def __str__(self):
        return self.name
    def render(self):
        pass
    def on_down(self):
        pass
    def on_up(self):
        pass
    def on_left(self):
        pass
    def on_right(self):
        pass
    def on_center(self):
        pass
    def on_enter(self):
        pass
    def on_KEY1(self):
        pass
    def on_KEY2(self):
        pass
