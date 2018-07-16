#! coding: utf-8 -*-
import kivy
kivy.require('1.10.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from client import Client


class HomeWidget(BoxLayout):
    """
    Главное окно. HOME
    """

    container_home = ObjectProperty(None)
    node_name_text_input = ObjectProperty()
    node_list = ObjectProperty()

    def get_node(self):
        node = Client.json_data()
        return node

    def save_node(self):
        print(self)
