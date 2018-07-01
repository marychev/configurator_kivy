import kivy
kivy.require('1.11.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from netaddr import IPAddress
import socket
from app.fileconfig import FileConfig
from app.node.input import (IpAddressInput, MaskInput, GatewayInput)


class NodeWidget(BoxLayout):
    """
    Установка сетевых настроек
    """

    def __init__(self):
        super().__init__()
        self.set_active()

    # id = StringProperty('id_node_widget')

    container_home = ObjectProperty()
    node_name_text_input = ObjectProperty()
    node_list = ObjectProperty()

    ip_address_input = IpAddressInput(id='id_ip_address')
    mask_input = MaskInput()
    gateway_input = GatewayInput()

    def set_active(self):
        """установить блокировку на поля. активация DHCP, кнопка далее"""
        self.enabled_text_inputs()
        self.enabled_more()

    def enabled_text_inputs(self):
        if 'id_dhcp' in self.ids.keys():
            self.ids['id_ip_address_input'].disabled = False
            self.ids['id_mask_input'].disabled = False
            self.ids['id_gateway_input'].disabled = False

            if self.ids['id_dhcp'].active:
                self.ids['id_ip_address_input'].disabled = True
                self.ids['id_mask_input'].disabled = True
                self.ids['id_gateway_input'].disabled = True

    def enabled_more(self):
        """Активировать кнопку Далее"""
        if 'id_more_btn' in self.ids.keys():
            ip_address_input = IpAddressInput(id='id_ip_address')
            mask_input = MaskInput(id='id_mask')
            gateway_input = GatewayInput(id='id_gateway')

            if ip_address_input.text is not None and mask_input.text is not None and gateway_input.text is not None:
                self.ids['id_more_btn'].disabled = False

    def save_node(self):
        """сохранить настройки редактируемой ноды"""
        dhcp = self.ids['id_dhcp'].active
        ip_address_text = self.ids['id_ip_address_input'].text
        mask_text = self.ids['id_mask_input'].text
        gateway_text = self.ids['id_gateway_input'].text
        netmask_bits = IPAddress(mask_text).netmask_bits()

        conf = FileConfig(ip_address_text, netmask_bits, gateway_text, dhcp)
        conf_node = conf.not_dhcp() if not dhcp else conf.dhcp()

        sock = socket.socket()
        sock.connect(('localhost', 1507))
        sock.send(bytes(conf_node.encode()))

        sock.close()

