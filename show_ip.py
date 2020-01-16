from App import App
import socket

class ShowIP(App):
    def __init__(self):
        super().__init__(name="Show IP")

    def render(self):
        self.draw.rectangle(((0, 0),(127, 63)), fill=1)
        ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
        self.draw.text((0, 0), text=f"IP:{ip}")
        if self.driver is not None:
            self.driver.refresh()