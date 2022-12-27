# Write a Python to find local IP addresses using Python's stdlib
if __name__ == "__main__":
    import socket
    print(socket.gethostbyname(socket.gethostname()))
