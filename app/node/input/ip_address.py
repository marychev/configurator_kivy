from app.node.input import AbstractIpAddressInput
from kivy.properties import StringProperty


class IpAddressInput(AbstractIpAddressInput):
    """
    IP Address text input
    """
    id = StringProperty('id_ip_address_input')
