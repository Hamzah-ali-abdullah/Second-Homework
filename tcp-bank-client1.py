import socket

HOST = '127.0.0.1'  
PORT = 8000        

while True:
    account_number = input("Enter your account number: ")
    operation = input("Enter operation (check_balance, deposit, withdraw): ")
    if operation in ("deposit", "withdraw"):
        amount = float(input("Enter amount: "))
    data = f"{account_number} {operation} {amount}".encode()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data)
        response = s.recv(1024).decode()
        print(response)
