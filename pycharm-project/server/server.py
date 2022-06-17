import os
import sys

from flask import Flask, request, Response
import redis

#starting flask
app = Flask(__name__)
#connecting to the database
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
db = redis.Redis(connection_pool=pool)

#function listens to the db and sends every message uploaded to the db
def event_stream():
    pubsub = db.pubsub()
    pubsub.subscribe('messages')
    for message in pubsub.listen():
        #for some reason i get the number 1 when i start listening so i decided to skip it
        if(message['data'] == 1):
            continue
        parsed_message = str(message['data']).split('\'')[1]
        yield f'{parsed_message}\n'
#post function, puts the message that the user sent in to the db
@app.route('/post', methods=['POST'])
def post():
    request_data = request.get_json()

    message = None

    if request_data:
        if 'message' in request_data:
            message = request_data['message']
            #print(message, file = sys.stderr)
    db.publish('messages', message)
    db.rpush('message_list', message)
    return ""
#get all function, gets all messages that were uploaded to the server
@app.route('/getall',methods = ['GET'])
def getall():
    message_list = db.lrange('message_list',0,db.llen('message_list'))
    string_message_list=[x.decode('utf-8') for x in message_list]
    return "\n".join(string_message_list)+"\n"
#stream function, returns any given message that is posted to the server
@app.route('/stream', methods = ['GET'])
def stream():
    return Response(event_stream(),mimetype="text/event-stream")


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
