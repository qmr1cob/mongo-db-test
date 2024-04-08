import socket

host = 'si0vm03536.de.bosch.com'
port = 30000

try:
    socket.create_connection((host, port), timeout=10)
    print("Connection successful")
except Exception as e:
    print("Connection failed:", e)