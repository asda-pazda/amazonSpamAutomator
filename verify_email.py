import boto.ses
import properties

conn = boto.ses.connect_to_region(properties.region,
                                  aws_access_key_id=properties.access_key_id,
                                  aws_secret_access_key=properties.secret_access_key)

print conn.list_verified_email_addresses()

#for i in range(1,10):
#	email = head + str(i) + tail
#	print 'verifying email address ' + email
#	conn.verify_email_address(email)
