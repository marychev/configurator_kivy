#! coding: utf-8 -*-
''' Async TCP server to make first tests of newly received GPS trackers '''

import asyncore
import socket
import logging


class Server(asyncore.dispatcher):
    def __init__(self, address):
        asyncore.dispatcher.__init__(self)
        self.logger = logging.getLogger('Server')
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(address)
        self.address = self.socket.getsockname()
        self.logger.debug('binding to %s', self.address)
        self.listen(5)

    def handle_accept(self):
        # Called when a client connects to our socket
        client_info = self.accept()
        if client_info is not None:
            self.logger.debug('handle_accept() -> %s', client_info[1])
            ClientHandler(client_info[0], client_info[1])


class ClientHandler(asyncore.dispatcher):
    def __init__(self, sock, address):
        asyncore.dispatcher.__init__(self, sock)
        self.logger = logging.getLogger('Client ' + str(address))
        self.data_to_write = []

    def writable(self):
        return bool(self.data_to_write)

    def handle_write(self):
        data = self.data_to_write.pop()
        sent = self.send(data[:1024])
        if sent < len(data):
            remaining = data[sent:]
            self.data.to_write.append(remaining)
        self.logger.debug('handle_write() -> (%d) "%s"', sent, data[:sent].rstrip())

    def handle_read(self):
        data = self.recv(1024)
        self.logger.debug('handle_read() -> (%d) "%s"', len(data), data.rstrip())
        # !!!!! EXAMPLE - ECHO
        self.data_to_write.insert(0, data)

        # сформировать файл (пример названия файла: 01-netcfg.yaml)
        from subprocess import call

        file_name = '01-netcfg.yaml'
        command = 'echo {} > {}'.format(self.data_to_write, file_name)

        call([command], shell=True)

    def handle_close(self):
        self.logger.debug('handle_close()')
        self.close()


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(name)s:[%(levelname)s]: %(message)s')
    HOST = '0.0.0.0'
    PORT = 1507
    s = Server((HOST, PORT))
    asyncore.loop()


if __name__ == '__main__':
    main()



# def current_node_data():
#     """имитация текущей / редактируемой ноды"""
#
#     json_node = open('data/current_node')
#     node_str = json.dumps(json.loads(json_node.read()))
#     json_node.close()
#     return node_str
#
#
# server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# server.settimeout(0.2)
# server.bind(("", 44444))
#
# i = 0
# while True:
#     server.sendto(current_node_data().encode(), ('<broadcast>', 37020))
#     i += 1
#     print("ping: ", i)
#     time.sleep(1)


# import asyncio
#
#
# async def handle_echo(reader, writer):
#     data = await reader.read(100)
#     message = data.decode()
#     addr = writer.get_extra_info('peername')
#     print("Получено %r :: %r" % (message, addr))
#
#     print("Послать: %r" % message + ':: SERVER')
#     writer.write(data)
#     await writer.drain()
#
#     print("---Close the client socket---")
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# coro = asyncio.start_server(handle_echo, '127.0.0.1', 8888, loop=loop)
# server = loop.run_until_complete(coro)
#
#
# # Serve requests until Ctrl+C is pressed
# print('-----------------------------------------------------------')
# print('- Обслуживание {}'.format(server.sockets[0].getsockname()))
# print('- Чтобы завершить обслуживание ``Ctrl+C``')
# print('-----------------------------------------------------------')
#
# try:
#     loop.run_forever()
# except KeyboardInterrupt:
#     pass
#
# # Close the server
# server.close()
# loop.run_until_complete(server.wait_closed())
# loop.close()
#
