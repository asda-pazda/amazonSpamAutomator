import boto.sqs
import properties
from boto.sqs.message import Message

conn = boto.sqs.connect_to_region(properties.queue_region,
                                  aws_access_key_id=properties.access_key_id,

                                  aws_secret_access_key=properties.secret_access_key)
q = conn.create_queue(properties.queue_name)

m = Message()
m.set_body(properties.message)
q.write(m)


