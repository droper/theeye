"""Client for the project"""

import requests
import argparse
import datetime


parser = argparse.ArgumentParser(description='Send POST requirements.')

parser.add_argument('-url', '--url', type=str,
                    default='http://127.0.0.1:8000/eye/event/2',
                    help='endpoint url')
parser.add_argument('-s', '--session', type=str,
                    help='session id of the event')
parser.add_argument('-cat', '--category', type=str,
                    help='category of the event')
parser.add_argument('-n', '--name', type=str,
                    help='name of the event')
parser.add_argument('-p', '--payload', type=str,
                    help='payload')
args = parser.parse_args()

# Generate Post request
timestamp = datetime.datetime.now()
data = {'session_id': args.session, 'category': args.session, 'name': args.name,
        'data': args.payload,
        'timestamp': timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")}

# Send the post request
print(data)
resp = requests.post(args.url, data=data)

print(resp.text)







