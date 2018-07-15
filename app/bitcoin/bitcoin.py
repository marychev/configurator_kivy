import kivy
kivy.require('1.11.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty


class BitcoinWidget(BoxLayout):
    """
    Bitcoin
    """

    container_home = ObjectProperty()
    node_name_text_input = ObjectProperty()
    node_list = ObjectProperty()

