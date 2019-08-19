import os
import base64
import json
import requests
from flask import Flask, make_response, request

app = Flask(__name__)

API_KEY = os.environ['API_KEY']
DOMAIN = os.environ['DOMAIN']

headers = {'Content-Type': 'application/json',
            'Authorization':"Basic "+base64.b64encode((API_KEY+":X").encode("ascii")).decode("utf-8")}
            

@app.route('/ticket/get', methods=['POST'])
def getTicket():
    data = request.json
    res = requests.get(
        "https://"+DOMAIN+".freshdesk.com/api/v2/tickets/"+str(data.get("id")),
        headers=headers
    )
    return end(res.json()),res.status_code

@app.route('/ticket/create', methods=['POST'])
def createTicket():
    data = request.json
    if data.get("ccEmails") is not None or data.get("ccEmails") != "" :
        data["cc_mails"] = data.pop("ccEmails")
    if data.get("priority") is None or data.get("priority") == "" :
        data["priority"] = 1
    if data.get("status") is None or data.get("status") == "" :
        data["status"] = 2
    res = requests.post(
        "https://"+DOMAIN+".freshdesk.com/api/v2/tickets",
        json=data,
        headers=headers
    )
    return end(res.json()),res.status_code

@app.route('/ticket/delete', methods=['POST'])
def deleteTicket():
    data = request.json
    res = requests.delete(
        "https://"+DOMAIN+".freshdesk.com/api/v2/tickets/"+str(data.get("id")),
        headers=headers
    )
    if res.status_code == 405:
        return end({
            'success': False,
            'error': f'Ticket not found for this id.'
        }),404
    if res.status_code == 204:
        return end({
            'success': True,
            'message': f'Ticket deleted successfully.'
        }),200
    return end(res.json()),res.status_code

@app.route('/ticket/list', methods=['POST'])
def listTicket():
    res = requests.get(
        "https://"+DOMAIN+".freshdesk.com/api/v2/tickets",
        headers=headers
    )
    return end(res.json()),res.status_code

def end(res):
    resp = make_response(json.dumps(res))
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp

@app.route('/contact/get', methods=['POST'])
def getContact():
    data = request.json
    res = requests.get(
        "https://"+DOMAIN+".freshdesk.com/api/v2/contacts/"+str(data.get("id")),
        headers=headers
    )
    return end(res.json()),res.status_code

@app.route('/contact/create', methods=['POST'])
def createContact():
    data = request.json
    if data.get("twitterId") is not None or data.get("twitterId") != "" :
        data["twitter_id"] = data.pop("twitterId")
    if data.get("uniqueExternalId") is not None or data.get("uniqueExternalId") != "" :
        data["unique_external_id"] = data.pop("uniqueExternalId")
    res = requests.post(
        "https://"+DOMAIN+".freshdesk.com/api/v2/contacts",
        json=data,
        headers=headers
    )
    return end(res.json()),res.status_code

@app.route('/contact/delete', methods=['POST'])
def deleteContact():
    data = request.json
    res = requests.delete(
        "https://"+DOMAIN+".freshdesk.com/api/v2/contacts/"+str(data.get("id")),
        headers=headers
    )
    if res.status_code == 405:
        return end({
            'success': False,
            'error': f'Contact not found for this id.'
        }),404
    if res.status_code == 204:
        return end({
            'success': True,
            'message': f'Contact deleted successfully.'
        }),200
    return end(res.json()),res.status_code

@app.route('/contact/list', methods=['POST'])
def listContact():
    res = requests.get(
        "https://"+DOMAIN+".freshdesk.com/api/v2/contacts",
        headers=headers
    )
    return end(res.json()),res.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
