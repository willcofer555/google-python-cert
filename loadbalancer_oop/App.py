server = Server()
server.add_connection("192.168.1.1")

print(server.load())

server.close_connection("192.168.1.1")
print(server.load())

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())


l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())
