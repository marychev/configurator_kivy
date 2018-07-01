import socket
import json


class Client():

    @staticmethod
    def json_data():
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        client.bind(("", 37020))

        data, addr = client.recvfrom(1024)
        json_data = json.loads(data.decode('utf-8'))
        return json_data

