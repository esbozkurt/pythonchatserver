import threading
import socket

host = '127.0.0.1' #it must be our local server / kendi yerel makinamizda olacak.
port = 55555 #it should be 5 times 5. It means 255.255.255.255
server = socket.socket(socket.AF_INET,  socket.SOCK_STREAM) #bir onceki dersten bak YT: NeuralNine
server.bind((host, port)) #server will find host and port.
server.listen() #listening for incoming connections


clients = [] #Should be collect clients name in list.
nicknames = [] #It might be more easier to collect created nicks in list as well due to matchin after.

def broadcast(message): #sent a sync to server all the clients connect to server. Such as checking.
    for clinet in clients: 
        clinet.send(message) #Message must be for every clinets. Sending and recieving.

#this part is for clients

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = client.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]   
            broadcast(f'{nickname} left the the chat|' .encode('ascii'))
            nicknames.remove(nickname) 
            break 
#run part

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode(ascii))   
        nickname = client.recv(1024).decode('ascii')
        clients.append(client)

        print(f'Nickname of the client is {nickname}|')
        broadcast(f'{nickname} joined the chat|'.encode('ascii'))
        client.send('Connected to the server|'.encode(ascii))

        thread = threading.Thread(target = handle, args = (client,))
        thread.start

print("Server is listening . . . ")
receive()

