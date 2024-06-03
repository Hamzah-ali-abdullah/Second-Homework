import socket
import threading

HOST = '0.0.0.0' 
PORT = 8000        

accounts = {
    "1A": 1000,
    "2A": 500,
    "3A": 1500,
    "1B": 2000,
    "2B": 1500,
    "3B": 2500
    
}

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        account_number, operation, amount = data.split()
        if account_number not in accounts:
            conn.sendall("Invalid account number".encode())
            continue

        try:
            amount = float(amount)
        except ValueError:
            conn.sendall("Invalid amount".encode())
            continue

        if operation == "check_balance":
            balance = accounts[account_number]
            conn.sendall(f"Your balance is: {balance}".encode())
        elif operation == "deposit":
            accounts[account_number] += amount
            conn.sendall(f"Deposit successful. New balance: {accounts[account_number]}".encode())
        elif operation == "withdraw":
            if accounts[account_number] < amount:
                conn.sendall("Insufficient funds".encode())
            else:
                accounts[account_number] -= amount
                conn.sendall(f"Withdrawal successful. New balance: {accounts[account_number]}".encode())
        else:
            conn.sendall("Invalid operation".encode())

    conn.close()
    print(f"Client {addr} disconnected")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
