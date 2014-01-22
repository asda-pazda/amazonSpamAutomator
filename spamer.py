__author__ = 'piotrek'

import properties
import time
from DBMessages import DBMessages
from DBUsers import DBUsers
from QueueManager import QueueManager
from EmailSender import EmailSender

queue_manager = QueueManager(properties.queue_name,
                             properties.queue_region,
                             properties.access_key_id,
                             properties.secret_access_key)

db_messages = DBMessages(properties.db_messages_region,
                         properties.db_messages_domain,
                         properties.access_key_id,
                         properties.secret_access_key)

db_users = DBUsers(properties.db_users_region,
                   properties.db_users_domain,
                   properties.access_key_id,
                   properties.secret_access_key)

email_sender = EmailSender(properties.email_region,
                           properties.my_email,
                           properties.access_key_id,
                           properties.secret_access_key)



def setUp():
    #email_sender.setUpDefaultEmailAddresses(properties.sample_emails)
    db_users.setUpDefaultUsers(properties.sample_users_list)
    db_messages.removeAllMessages()
    queue_manager.removeAllMessagesFromQueue()
    #db_messages.setUpDefaultMessages(properties.sample_messages)

def tearDown():
    email_sender.deleteAllEmails()
    db_messages.removeAllMessages()
    db_users.removeAllUsers()


#tearDown()

def readMessageFromFile(filename):
        f = open(filename, 'r')
        return f.read()

def addNewMessage(subject, message, category):
    message_id = db_messages.addMessage(message, category, subject)
    queue_manager.sendMessageToQueue(message_id)

def setUpMessages():
    for message in properties.sample_messages:
        addNewMessage(message['subject'], readMessageFromFile(message['filename']), message['category'])

def getMessagesFromQueueAndSendEmails():
    message_id = queue_manager.getMessageFromQueue()
    while message_id:
        print message_id
        message = db_messages.getMessage(message_id)
        category = message['category']
        users_from_category = db_users.getUsersSignedFor(category)

        for user in users_from_category:
            email_sender.sendEmailTo(user['name'], user['surname'], user['email'], message['subject'], message['content'])

        message_id = queue_manager.getMessageFromQueue()

setUp()
setUpMessages()
print 'sleep'
time.sleep(5)
print 'after sleep'
getMessagesFromQueueAndSendEmails()
#db_messages.printDB()
#message = db_messages.getMessage('message4')
#email_sender.sendEmailTo('Sunan', 'Staas', 'sunanstaas@niepodam.pl', message['subject'], message['content'])

