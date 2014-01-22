__author__ = 'piotrek'
import boto.sdb

class DBMessages():
    def __init__(self, region, domain_name, access_key_id, secret_access_key):
        self.conn = boto.sdb.connect_to_region(region,
                                               aws_access_key_id=access_key_id,
                                               aws_secret_access_key=secret_access_key)
        self.domain_name = domain_name
        self.domain = self.conn.create_domain(domain_name)

    def addMessage(self, message, category, subject):
        index = self.getItemCount() + 1
        item_name = 'message' + str(index)
        item_attrs = {'content': message, 'category': category, 'subject': subject}
        self.domain.put_attributes(item_name, item_attrs)
        print 'added ' + item_name + ': with attributes' + str(item_attrs)
        return item_name

    def getMessage(self, message_id):
        return self.domain.get_item(message_id)

    def printDB(self):
        query = 'select * from `' + self.domain_name + '`'
        rs = self.domain.select(query, None, True)
        for item in rs:
            print item.name + ' ' + str(item)

    def getItemCount(self):
        query = 'select count(*) from `' + self.domain_name + '`'
        rs = self.domain.select(query, None, True)
        return int(rs.next()['Count'])

    def removeAllMessages(self):
        query = 'select * from `' + self.domain_name + '`'

        rs = self.domain.select(query, None, True)
        for item in rs:
            self.domain.delete_item(item)
        print 'Removed all messages'

    def setUpDefaultMessages(self, messages):
        print 'Set up default messages'
        self.removeAllMessages()
        for message in messages:
            self.addMessage(self.readMessageFromFile(message['filename']), message['category'], message['subject'])

    def readMessageFromFile(self, filename):
        f = open(filename, 'r')
        return f.read()