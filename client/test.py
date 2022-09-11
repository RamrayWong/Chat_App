from client import Client
import time
from threading import Thread


c1 = Client("Ramray")
c2 = Client("Wong")



def update_messages():
	msgs = []
	run = True
	while run:
		time.sleep(0.1)
		new_messages = c1.get_messages()
		msgs.extend(new_messages)

		for msg in new_messages:
			print(msg)
			if msg == "{quit}":
				run = False
				print("BREAKED")
				break

Thread(target=update_messages).start()

time.sleep(0.25)
c2.send_message("hello")
time.sleep(0.25)
c1.send_message("howdy")
time.sleep(0.25)
c2.send_message("nothing much")
time.sleep(0.25) 
c1.send_message("GOODBYE")

time.sleep(0.25)
c1.disconnect()
time.sleep(0.25)
c2.disconnect()
	
