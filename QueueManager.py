__author__ = 'piotrek'

import boto.sqs
import time
from boto.sqs.message import Message

class QueueManager():
    def __init__(self, queue_name, region, access_key_id, secret_access_key):
        self.conn = boto.sqs.connect_to_region(region,
                                               aws_access_key_id=access_key_id,
                                               aws_secret_access_key=secret_access_key)
        self.queue = self.conn.create_queue(queue_name, 30)

    def sendMessageToQueue(self, message):
        print 'Sending message "' + message + '" to queue ' + self.queue.name
        m = Message()
        m.set_body(message)
        self.queue.write(m)

    def removeMessageFromQueue(self, message):
        print 'Removing message from queue' + str(message)
        self.queue.delete_message(message)

    def getMessageFromQueue(self):
        message = self.queue.read()
        if message:
            result = message.get_body()
            self.queue.delete_message(message)
            return result
        return None

    def removeAllMessagesFromQueue(self):
        print 'Removing messages from queue'
        self.queue.clear()
