'Chat Room Connection - Client-To-Client'
import threading
import socket
import funktions



"""" 
host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []


def user_input_handler(message, engine, vosk_recognizer, pyttsx_voice_id, current_ask_topic_sentence):
    if message != None:
        user_input = message
    else:
        user_input = funktions.text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, {current_ask_topic_sentence})

    return user_input

import socket

def server_program_old(engine, vosk_recognizer, pyttsx_voice_id, current_ask_topic_sentence):
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        message = conn.recv(1024).decode()
        #if not message:
           # break
        print("from connected user: " + str(message))

        user_input = user_input_handler(message, engine, vosk_recognizer, pyttsx_voice_id, current_ask_topic_sentence)

        Frage = "Was darfs Sein?"
        conn.send(Frage.encode())
        return user_input
    conn.close()




# Function to handle clients'connections


def handle_client(client, engine, vosk_recognizer, pyttsx_voice_id, current_ask_topic_sentence):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            user_input_handler(message, engine, vosk_recognizer, pyttsx_voice_id, current_ask_topic_sentence)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break
# Main function to receive the clients connection


def receive(engine, vosk_recognizer, pyttsx_voice_id, current_ask_topic_sentence):
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client, engine, vosk_recognizer, pyttsx_voice_id, current_ask_topic_sentence, ))
        thread.start()"""


def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    return conn

def get_server_input(conn):   
    data = conn.recv(1024).decode()
    
    print("from connected user: " + str(data))
    return data
    data = input(' -> ')
    conn.send(data.encode())

def conn_close(conn):
    conn.close()

def server_input(conn):        
    server_input = get_server_input(conn)  
    conn_close(conn)
    print(server_input)
    return server_input

def server_output(conn, output):    
    conn.send(output.encode('utf-8'))