import pyrebase
import random
import time
from collections import deque
config = {
    'apiKey': "AIzaSyDmgvnM0dLfnnJr4jpVvHpTWzDlvxHd8nQ",
    'authDomain': "datastore-8679e.firebaseapp.com",
    'databaseURL': "https://datastore-8679e.firebaseio.com",
    'projectId': "datastore-8679e",
    'storageBucket': "datastore-8679e.appspot.com",
    'messagingSenderId': "827174721908"

}
#databse connection
firebase = pyrebase.initialize_app(config)
db = firebase.database()
#mock sensor writer
x=deque(maxlen=20)
x.append(1)
while True:
    timestamp = time.time()
    tval = random.randrange(10,30)
    time.sleep(3)
    db.child("sence1").set({'timestamp': timestamp, 'value': tval})
    print(timestamp,tval)