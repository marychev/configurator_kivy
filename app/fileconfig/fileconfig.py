#! coding: utf-8 -*-
import sys
from ruamel.yaml import YAML


class FileConfig():
    """конфигурационные файлы"""

    def __init__(self, ip_address, netmask_bits, gateway, is_dhcp=False):
        self.is_dhcp = is_dhcp
        self.ip_address = ip_address
        self.netmask_bits = netmask_bits
        self.gateway = gateway

    def create(self):
        pass

    def not_dhcp(self):
        config = '''
network:
    version: 2
    renderer: networkd
    ethernets:
        enp3s0:
        addresses:
            - {ip_address}/{netmask_bits}
        gateway4: {gateway}
        nameservers:
            addresses: [{ip_address}, 8.8.8.8, x.x.x.xxx]
            '''.format(ip_address=self.ip_address, netmask_bits=self.netmask_bits, gateway=self.gateway)

        return config

    def dhcp(self):
        config = '''
network:
    version: 2
    renderer: networkd
    ethernets:
        enp3s0:
            dhcp4: true'''
        return config



'''
{'container_home': <WeakProxy to <kivy.uix.boxlayout.BoxLayout object at 0x7f0e53140458>>, 
'current_node': <WeakProxy to <kivy.uix.label.Label object at 0x7f0e53140528>>, 
'id_dhcp': <WeakProxy to <kivy.uix.checkbox.CheckBox object at 0x7f0e527f91e8>>, 
'id_ip_address_input': <WeakProxy to <kivy.uix.textinput.TextInput object at 0x7f0e527643f0>>, 
'id_mask_input': <WeakProxy to <kivy.uix.textinput.TextInput object at 0x7f0e52764528>>, 
'id_gateway_input': <WeakProxy to <kivy.uix.textinput.TextInput object at 0x7f0e52764660>>
}
'''