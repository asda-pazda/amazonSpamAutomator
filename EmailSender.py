__author__ = 'piotrek'
import boto.ses

class EmailSender():
    def __init__(self, region, my_email, access_key_id, secret_access_key):
        self.conn = boto.ses.connect_to_region(region,
                                               aws_access_key_id=access_key_id,
                                               aws_secret_access_key=secret_access_key)
        self.my_email = my_email

    def verifyEmailAddress(self, email):
        self.conn.verify_email_address(email)
        print 'Verification email has been send to ' + str(email)

    def checkIfEmailIsVerified(self, email):
        # lista wszystkich potwierdzonych emaili
        verified_email_addresses = self.conn.list_verified_email_addresses()['ListVerifiedEmailAddressesResponse']['ListVerifiedEmailAddressesResult']['VerifiedEmailAddresses']
        return email in verified_email_addresses

    def checkIfVerificationEmailMessageHasBeenSend(self, email):
        # lista wszystkich potwierdzonych emaili + te do ktorych zostala wyslana weryfikacja
        verified_email_addresses = self.conn.list_identities()['ListIdentitiesResponse']['ListIdentitiesResult']['Identities']
        return email in verified_email_addresses

    def sendEmailTo(self, name, surname, email, subject, body):
        if self.checkIfEmailIsVerified(email):
            print 'Sending email to: ' + name + ' ' + surname + ' at email ' + email + ' with subject ' + subject
            head = 'Dear ' + name + ' ' + surname + ',\n\n'
            tail = '\n\nBest regards, Spam Team'
            final_body = head + body + tail
            self.conn.send_email(self.my_email,
                                 subject,
                                 final_body,
                                 email)
        elif self.checkIfVerificationEmailMessageHasBeenSend(email):
            print 'Verification message has been already send to ' + email
        else:
            self.verifyEmailAddress(email)

    def deleteAllEmails(self):
        verified_email_addresses = self.conn.list_identities()['ListIdentitiesResponse']['ListIdentitiesResult']['Identities']
        for address in verified_email_addresses:
            if not self.checkIfVerificationEmailMessageHasBeenSend(address):
                self.conn.delete_verified_email_address(address)
        print 'All email addresses has been deleted'

    def setUpDefaultEmailAddresses(self, emails):
        print 'Set up default email addresses'
        self.deleteAllEmails()
        for email in emails:
            self.verifyEmailAddress(email)