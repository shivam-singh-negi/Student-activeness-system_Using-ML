import socket
from csv import DictWriter

while True:
    s = socket.socket()
    port = 12345
    s.bind(('localhost', 12345))
    s.listen(5)
    c, addr = s.accept()
    print("Socket Up and running with a connection from", addr)
    rcvdData = c.recv(4096).decode()
    print("S:",rcvdData)
    sendData = "recieved"
    c.send(sendData.encode())
    x=rcvdData.split(",")
    print(x)
    field_names = ["Roll.No", "Accuracy", "Missed", "Clicks", "Scroll"]
    dict = {"Roll.No": x[0], 'Accuracy': x[1], 'Missed': x[2], 'Clicks': x[3],'Scroll': x[4]}
    with open("C:/Users/SHIVAM SINGH NEGI/Documents/dataset.csv", 'a', newline="") as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)

        # Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(dict)
        print("Written to file")

        # Close the file object
        f_object.close()

c.close()