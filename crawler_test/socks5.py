import socks
import socket
def openproxy():
    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 10808)
    socket.socket = socks.socksocket