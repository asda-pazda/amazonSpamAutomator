# wysyla email weryfikujacy pod podane adresy
import boto.ses
import properties

conn = boto.ses.connect_to_region(properties.email_region,
                                  aws_access_key_id=properties.access_key_id,
                                  aws_secret_access_key=properties.secret_access_key)

for i in range(1, 10):
    email = properties.head + str(i) + properties.tail
    print 'verifying email address ' + email
    conn.verify_email_address(email)
