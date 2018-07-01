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
        print(value)

    def on_text(self, instance, value):
        print('The widget',  self, 'instance', instance, 'have:', value)

    def on_enter(self, instance, value):
        """проверить правильность после нажатия ЕНТЕР"""
        print(self, instance, value)