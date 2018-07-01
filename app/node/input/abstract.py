import re
from kivy.uix.textinput import TextInput


class AbstractIpAddressInput(TextInput):
    """
    Abstract class: IP Address, Mask, Gateway ...
    """

    multiline = False
    pat = re.compile('[^0-9.:]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(AbstractIpAddressInput, self).insert_text(s, from_undo=from_undo)

    def on_focus(self, instance, value):
        if value:
            print('>> User focused')
        else:
            print('<<  User defocused')
        print(self)
        print(self.get_root_window())
        win = self.get_root_window()
        print(win)
        print('--- end ON FOCUS ---')

    def on_text(self, instance, value):
        print('>> START on text: the widget',  self, 'instance', instance, 'have:', value)
        print('--- end ON TEXT ---')
        print()

    def on_enter(self, instance, value):
        """проверить правильность после нажатия ЕНТЕР"""
        print(self, instance, value)