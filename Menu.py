import App

class Menu(App.App):
    def __init__(self, items, parent=None, name='Menu'):
        super().__init__(parent, name)
        self.selected = 0
        self.page = 0
        self.total_page_num = (len(items)-1) // 5 + 1
        self.items = items
        for item in self.items:
            item.parent = self

    def render(self):
        self.draw.rectangle(((0, 0), (127, 63)), fill=1)
        text = ''
        first_idx = int(self.page * 5)
        end_idx = int((self.page+1) * 5)
        for idx, item in enumerate(self.items[first_idx:end_idx]):
            if idx == self.selected:
                text += '*'
            else:
                text += ' '
            text += str(item) + '\n'
        self.draw.multiline_text((0, 0), text, fill=0, spacing=1)
        if self.disp is not None:
            self.disp.refresh()
            
    def on_down(self):
        if self.page == self.total_page_num - 1:
            self.selected = (self.selected + 1) % (len(self.items) % 5)
        else:
            self.selected = (self.selected + 1) % 5
        self.render()

    def on_up(self):
        if self.page == self.total_page_num - 1:
            self.selected = (self.selected - 1) % (len(self.items) % 5)
        else:
            self.selected = (self.selected - 1) % 5
        self.render()

    def on_right(self):
        self.page = (self.page + 1) % self.total_page_num
        self.selected = 0
        self.render()

    def on_left(self):
        self.page = (self.page - 1) % self.total_page_num
        self.selected = 0
        self.render()


    def on_center(self):
        if self.driver is None:
            return
        self.driver.bind_class(self.items[self.selected])

    def on_enter(self):
        self.selected = self.page = 0
        for item in self.items:
            item.parent = self