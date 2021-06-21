import socket

#                  ipv4            , UDP type
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# what is my reciver address
recv_addr = ('localhost',9999)

# NOW i want to send message
user_data = input("Enter yout message : ")
newdata=user_data.encode('ascii')
# now you can send data
s.sendto(newdata,recv_addr)
print("your message has been sent.")