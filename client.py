import socket
import threading

nickname = input("Chose a nickname")

client = socket.scoket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
        while True:
            try:
                massege = client.recv(1024).decode('ascii')
                if message == 'NICK':
                    client.send(nickname.encode('ascii'))
                    pass
                else:
                    print(message)
            except:
                print("An error occured!")
                client.close()
                break
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start


            