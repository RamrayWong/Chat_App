from client import Client
import time


c1 = Client("Ramray")
c2 = Client("Wong")
time.sleep(0.25)
c2.send_message("hello")
time.sleep(0.25)
c1.send_message("howdy")
time.sleep(0.25)
c2.send_message("nothing much")
time.sleep(0.25) 
c1.send_message("howdy again")
time.sleep(0.25)
c1.disconnect()
time.sleep(0.25)
c2.disconnect()
