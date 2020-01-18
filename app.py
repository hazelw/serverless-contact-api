import boto3
from flask import Flask, jsonify, request
import os
import uuid

app = Flask(__name__)

client = boto3.client('dynamodb', region_name='eu-west-2')
#CONTACTS_TABLE = os.environ.get('CONTACTS_TABLE', 'contacts')


@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/submissions', methods=['POST'])
def submit_contact():
    data = request.json

    first_name = data.get('first_name', None)
    last_name = data.get('last_name', None)
    email = data.get('email', None)
    message = data.get('message', None)

    submission_id = uuid.uuid4().hex

    """client.put_item(
        TableName=CONTACTS_TABLE,
        # the 'S' here is for String:
        Item={
            'id': {'S': submission_id},
            'first_name': {'S': first_name},
            'last_name': {'S': last_name},
            'email': {'S': email},
            'message': {'S': message}
        }
    )"""

    return jsonify({
        'status': 'success',
        'submission': {
            'id': submission_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'message': message
        }
    }), 201


if __name__ == '__main__':
    app.run()
