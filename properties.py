access_key_id = ''
secret_access_key = ''

email_region = 'us-east-1'
my_email = 'spam_provider@niepodam.pl'

queue_region = 'eu-west-1'
queue_name = 'message-queue'

db_messages_region = 'us-west-2'
db_messages_domain = 'messages-domain'

db_users_region = 'us-west-2'
db_users_domain = 'users-domain'

sample_users_list = [ {'name': 'Tane', 'surname': 'Dawson', 'email': 'tanedawson@niepodam.pl', 'category': 'animals'},
                      {'name': 'Tane', 'surname': 'Dawson', 'email': 'tanedawson@niepodam.pl', 'category': 'food'},
                      {'name': 'Jasper', 'surname': 'Juraj', 'email': 'jasperjuraj@niepodam.pl', 'category': 'animals'},
                      {'name': 'Sunan', 'surname': 'Staas', 'email': 'sunanstaas@niepodam.pl', 'category': 'clothes'},
                      {'name': 'Bittor', 'surname': 'Georgiy', 'email': 'bittorgeorgiy@niepodam.pl', 'category': 'animals'},
                      {'name': 'Gilberto', 'surname': 'Ville', 'email': 'gilbertoville@niepodam.pl', 'category': 'animals'},
                      {'name': 'Turlough', 'surname': 'Uther', 'email': 'turloughuther@niepodam.pl', 'category': 'food'},
                      {'name': 'Tzafrir', 'surname': 'Cleon', 'email': 'tzafrircleon@niepodam.pl', 'category': 'animals'} ]

sample_messages = [ {'category': 'animals', 'filename': 'animals2', 'subject': 'Super cats' },
                    {'category': 'food', 'filename': 'food', 'subject': 'Super food' },
                    {'category': 'clothes', 'filename': 'clothes', 'subject': 'Super clothes' },
                    {'category': 'animals', 'filename': 'animals', 'subject': 'Super dogs' }]

sample_emails = [ 'spam_provider@niepodam.pl']
for user in sample_users_list:
    sample_emails.append(user['email'])








