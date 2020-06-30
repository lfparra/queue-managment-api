import os
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client
db = SQLAlchemy()

class Queue:

    def __init__(self):
        # CONFIG TWILIO
        self.account_sid = os.environ.get('ACCOUNT_ID')
        self.auth_token = os.environ.get('AUTH_TOKEN')
        self.client = Client(self.account_sid, self.auth_token)

        self._queue = ["Name 1" , "Name 2", "Name 3"]
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = 'FIFO'

    """ def enqueue(self, item):
        message = self.client.messages.create(
            body = 'This is a test message ',
            from_ = os.environ.get('PHONE'),
            to='+56997796298'
        )
        print(message.sid) """
            
    def dequeue(self):
        pass

    def get_queue(self):
        pass
    
    def size(self):
        return len(self._queue)

