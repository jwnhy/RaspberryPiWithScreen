from App import App
import psutil
class ShowInfo(App):
    def __init__(self):
        super().__init__(name="Show Info")

    def render(self):
        self.draw.rectangle(((0, 0),(127, 63)), fill=1)
        text = f'CPU:{psutil.cpu_percent(0)}%\n' +\
               f'Disk:{psutil.disk_usage("/").percent}%\n' +\
               f'RAM:{psutil.virtual_memory()[2]}%'
        self.draw.multiline_text((0, 0), text=text, fill=0, spacing=1)
        if self.driver is not None:
            self.driver.refresh()
    def on_center(self):
        self.render()
    def on_KEY1(self):
        self.render()