import kivy

kivy.require('1.11.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

# init apps for templates
from app.node import NodeWidget
from app.home import HomeWidget


class NodeListButton(ListItemButton):
    pass


class ConfiguratorApp(App):
    """ Точка начала работы приложения """
    def build(self):
        self.root = Builder.load_file('templates/home.kv')

    def next_screen(self, screen):
        filename = screen + '.kv'
        Builder.unload_file('templates/' + filename)
        self.root.container_home.clear_widgets()
        screen = Builder.load_file('templates/' + filename)
        self.root.container_home.add_widget(screen)


if __name__ == '__main__':
    ConfiguratorApp().run()
