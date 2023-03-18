import xmlrpc.client
from datetime import datetime

proxy = xmlrpc.client.ServerProxy("http://localhost:5001/")

#nro1 = 15
#nro2 = 20

def start():
    #Start client loop, ask for a note or quit
    print("Hello, welcome to note-machine")
    while True:
        print("******************")
        print("(1) Write a new note")
        print("(2) Look for a note in db")
        print("(3) Quit")
        choice = int(input("Your choice: "))
        if choice == 1:
            topic2 = input("Give note topic: ")
            note = input("Give note name: ")
            txt = input("Give note text: ")
            print("Sending new note")
            time = str(datetime.now())
            print(time)
            print(topic2, note, txt)
            #result = proxy.sendtext(topic, note, txt, time)
            result = proxy.sendtext(topic2, note, txt, time)
            print(f"Result is: {result}")
            #print("This is the note: ",result[0],result[1])
        if choice == 2:
            header = input("Give note topic: ")
            print("Looking for note on given topic")

        if choice == 3:
            print("Thanks for using")
            break
start()

        