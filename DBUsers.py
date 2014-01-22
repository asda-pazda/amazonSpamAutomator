__author__ = 'piotrek'
import boto.sdb

class DBUsers():
    def __init__(self, region, domain_name, access_key_id, secret_access_key):
        self.conn = boto.sdb.connect_to_region(region,
                                               aws_access_key_id=access_key_id,
                                               aws_secret_access_key=secret_access_key)
        self.domain_name = domain_name
        self.domain = self.conn.create_domain(domain_name)

    def addUser(self, name, surname, email, category):
        index = self.getItemCount() + 1
        item_name = 'user' + str(index)
        item_attrs = {'name': name, 'surname': surname, 'email': email, 'category': category}
        self.domain.put_attributes(item_name, item_attrs)
        print 'added ' + item_name + ': with attributes' + str(item_attrs)
        return item_name

    def getUsersSignedFor(self, category):
        query = 'select * from `' + self.domain_name + '` where category="' + category + '"'
        users_list = []
        for user in self.domain.select(query, None, True):
            users_list.append(user)
        return users_list

    def printDB(self):
        query = 'select * from `' + self.domain_name + '`'
        rs = self.domain.select(query, None, True)
        for item in rs:
            print item.name + ' ' + str(item)

    def getItemCount(self):
        query = 'select count(*) from `' + self.domain_name + '`'
        rs = self.domain.select(query, None, True)
        return int(rs.next()['Count'])

    def removeAllUsers(self):
        query = 'select * from `' + self.domain_name + '`'

        rs = self.domain.select(query, None, True)
        for item in rs:
            self.domain.delete_item(item)
        print 'Removed all users'

    def setUpDefaultUsers(self, users):
        print 'Set up default users'
        self.removeAllUsers()
        for user in users:
            self.addUser(user['name'], user['surname'], user['email'], user['category'])

