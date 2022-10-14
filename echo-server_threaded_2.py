#!/usr/bin/env python3

import socket
from gpiozero import Motor, OutputDevice
from time import sleep
from time import time
import logging
import threading



# Define and setup GPIO pins
# Left foot
motor1 = Motor(24, 27)
motor1_enable = OutputDevice(5, initial_value=1)
# Right foot
motor2 = Motor(6, 22)
motor2_enable = OutputDevice(17, initial_value=1)
# Right tentacle
motor3 = Motor(23, 16)
motor3_enable = OutputDevice(12, initial_value=1)
# Left tentacle
motor4 = Motor(13, 18)
motor4_enable = OutputDevice(25, initial_value=1) 

# HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 65442  # Port to listen on (non-privileged ports are > 1023)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# time_old = time()
# flag_wings = True


def thread_function(name):
    logging.info("Thread %s: starting", name)
    sleep(2)
    logging.info("Thread %s: finishing", name)





if __name__ == "__main__":
    while True:
        print('looping')
        x = threading.Thread(target=thread_function, args=(1,))
        x.start()


# # Define and setup GPIO pins
# # Left foot
# motor1 = Motor(24, 27)
# motor1_enable = OutputDevice(5, initial_value=1)
# # Right foot
# motor2 = Motor(6, 22)
# motor2_enable = OutputDevice(17, initial_value=1)
# # Right tentacle
# motor3 = Motor(23, 16)
# motor3_enable = OutputDevice(12, initial_value=1)
# # Left tentacle
# motor4 = Motor(13, 18)
# motor4_enable = OutputDevice(25, initial_value=1) 

# # HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
# HOST = "0.0.0.0"  # Listen on all interfaces
# PORT = 65442  # Port to listen on (non-privileged ports are > 1023)

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((HOST, PORT))
# server_socket.listen()

# time_old = time()
# flag_wings = True






# from threading import Thread

# class myClassA(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#         self.daemon = True
#         self.start()
#     def run(self):
#         while True:
#             #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allow reuse of address
#         # s.bind((HOST, PORT))
#         # s.listen()
#         #try:

#         # # Switch wing direction every 3s
#         # time_new = time()
#         # if time_new-time_old >= 2:
#         #     flag_wings = not flag_wings
#         #     time_old = time_new
#         #     print('switched wing direction')

#         # # # Switch wings on/off
#         # # if flag_wings:
#         # #     print('wings up')
#         # #     motor3.forward()
#         # #     motor4.forward()
#         # # else:
#         # #     print('wings down')
#         # #     motor3.stop()
#         # #     motor4.stop()

#         # print('looper')



#             conn, addr = server_socket.accept()
#             with conn:
#                 print(f"Connected by {addr}")
#                 while True:
#                     data = conn.recv(1024)
#                     if not data:
#                         break
#                     msg = data.decode()
#                     print(msg)

#                     if msg == 'stop':
#                         motor1.stop()
#                         motor2.stop()

#                     elif msg == 'left':
#                         motor1.forward(0.5)
#                         motor2.stop()

#                     elif msg == 'right':
#                         motor1.stop()
#                         motor2.forward(0.5)

#                     elif msg == 'forward':
#                         motor1.forward(0.5)
#                         motor2.forward(0.5)

#                     #conn.sendall(data)

# class myClassB(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#         self.flag_wings = True
#         self.time_old = time()
#         self.daemon = True
#         self.start()
#     def run(self):
#         while True:
#             # Switch wing direction every 3s
#             time_new = time()
#             if time_new-time_old >= 2:
#                 self.flag_wings = not self.flag_wings
#                 self.time_old = time_new
#                 print('switched wing direction')

#             # # Switch wings on/off
#             # if flag_wings:
#             #     print('wings up')
#             #     motor3.forward()
#             #     motor4.forward()
#             # else:
#             #     print('wings down')
#             #     motor3.stop()
#             #     motor4.stop()

#             print('looper')


# myClassA()
# myClassB()
# while True:
#     pass





# # while(1):
# #     #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# #         #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allow reuse of address
# #         # s.bind((HOST, PORT))
# #         # s.listen()
# #     #try:

# #     # Switch wing direction every 3s
# #     time_new = time()
# #     if time_new-time_old >= 2:
# #         flag_wings = not flag_wings
# #         time_old = time_new
# #         print('switched wing direction')

# #     # # Switch wings on/off
# #     # if flag_wings:
# #     #     print('wings up')
# #     #     motor3.forward()
# #     #     motor4.forward()
# #     # else:
# #     #     print('wings down')
# #     #     motor3.stop()
# #     #     motor4.stop()

# #     print('looper')



# #     conn, addr = server_socket.accept()
# #     with conn:
# #         print(f"Connected by {addr}")
# #         while True:
# #             data = conn.recv(1024)
# #             if not data:
# #                 break
# #             msg = data.decode()
# #             print(msg)

# #             if msg == 'stop':
# #                 motor1.stop()
# #                 motor2.stop()

# #             elif msg == 'left':
# #                 motor1.forward(0.5)
# #                 motor2.stop()

# #             elif msg == 'right':
# #                 motor1.stop()
# #                 motor2.forward(0.5)

# #             elif msg == 'forward':
# #                 motor1.forward(0.5)
# #                 motor2.forward(0.5)

# #             #conn.sendall(data)
    
# #     # except:
# #     #     print('no comms')


# # # except KeyboardInterrupt:
# # #         pass
