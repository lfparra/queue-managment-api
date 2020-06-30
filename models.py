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

        self._queue = ["Humberto", "Sebastian", "Diego", "Luis", "Jonathan", "Leonardo"]
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = 'FIFO'

    def enqueue(self, nombre):
        message = self.client.messages.create(
            body = f'Hola {nombre}, su requerimiento fu ingresado, faltan {self.size()-1} personas antes que usted',
            from_ = os.environ.get('PHONE'),
            to='+56997796298'
        )
            
    def dequeue(self, nombreTurno):
        message = self.client.messages.create(
            body = f'Hola {nombreTurno}, es su turno',
            from_ = os.environ.get('PHONE'),
            to='+56997796298'
        )
        return self._queue.pop(0)

    def get_queue(self):
        return self._queue

    def size(self):
        return len(self._queue)

