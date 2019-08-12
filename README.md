# _Freshdesk_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)
[![Build Status](https://travis-ci.com/omg-services/freshdesk.svg?branch=master)](https://travis-ci.com/omg-services/freshdesk)
[![codecov](https://codecov.io/gh/omg-services/freshdesk/branch/master/graph/badge.svg)](https://codecov.io/gh/omg-services/freshdesk)

This is omg services for 'Freshdesk'.
An online cloud-based customer service software providing helpdesk support with all smart automations to get things done faster. 

```coffee
microserive.guide exec -e API_KEY=<KEY> -e DOMAIN=<DOMAIN> microservice/freshdesk createTicket \
  description:'Test ticket' \
  subject:'Mock Ticket' \
  email:'mock@email.com'

{
  "cc_emails": [],
  "fwd_emails": [],
  "reply_cc_emails": [],
  "ticket_cc_emails": [],
  "fr_escalated": false,
  "spam": false,
  "email_config_id": null,
  "group_id": null,
  "priority": 1,
  "requester_id": 48008271709,
  "responder_id": null,
  "source": 2,
  "company_id": null,
  "status": 2,
  "subject": "Mock Ticket",
  "to_emails": null,
  "product_id": null,
  "id": 41,
  "type": null,
  "due_by": "2019-08-15T07:37:13Z",
  "fr_due_by": "2019-08-13T07:37:13Z",
  "is_escalated": false,
  "description": "<div>Test ticket</div>",
  "description_text": "Test ticket",
  "custom_fields": {},
  "created_at": "2019-08-12T07:37:13Z",
  "updated_at": "2019-08-12T07:37:13Z",
  "tags": [],
  "attachments": []
}
```

## Direct usage in [Storyscript](https://storyscript.io/):

##### Create Ticket
```coffee
>>> mailgun createTicket description:'<DESCRIPTION>' subject:'<SUBJECT>' email:'<EMAIL>' priority:'<PRIORITY>' status:'<STATUS>' cc_emails='<CC_EMAILS>'
{
  "cc_emails": [],
  "fwd_emails": [],
  "reply_cc_emails": [],
  "ticket_cc_emails": [],
  "fr_escalated": false,
  "spam": false,
  "email_config_id": null,
  "group_id": null,
  "priority": 1,
  "requester_id": 48008271709,
  "responder_id": null,
  "source": 2,
  "company_id": null,
  "status": 2,
  "subject": "Mock Ticket",
  "to_emails": null,
  "product_id": null,
  "id": 41,
  "type": null,
  "due_by": "2019-08-15T07:37:13Z",
  "fr_due_by": "2019-08-13T07:37:13Z",
  "is_escalated": false,
  "description": "<div>Test ticket</div>",
  "description_text": "Test ticket",
  "custom_fields": {},
  "created_at": "2019-08-12T07:37:13Z",
  "updated_at": "2019-08-12T07:37:13Z",
  "tags": [],
  "attachments": []
}
```

##### Get Ticket
```coffee
>>> mailgun getTicket id:<ID>
{
  "cc_emails": [],
  "fwd_emails": [],
  "reply_cc_emails": [],
  "ticket_cc_emails": [],
  "fr_escalated": false,
  "spam": false,
  "email_config_id": null,
  "group_id": null,
  "priority": 1,
  "requester_id": 48008271709,
  "responder_id": null,
  "source": 2,
  "company_id": null,
  "status": 2,
  "subject": "Mock Ticket",
  "association_type": null,
  "to_emails": null,
  "product_id": null,
  "id": 41,
  "type": null,
  "due_by": "2019-08-15T07:37:13Z",
  "fr_due_by": "2019-08-13T07:37:13Z",
  "is_escalated": false,
  "description": "<div>Test ticket</div>",
  "description_text": "Test ticket",
  "custom_fields": {},
  "created_at": "2019-08-12T07:37:13Z",
  "updated_at": "2019-08-12T07:37:13Z",
  "tags": [],
  "attachments": [],
  "source_additional_info": null
}
```

##### Delete Ticket
```coffee
>>> mailgun deleteTicket id:<ID>
{
  "success": true,
  "message": "Ticket deleted successfully."
}
```

##### Get Ticket List
```coffee
>>> mailgun listTicket
["LIST_OF_TICKETS"]
```

##### Create Contact
```coffee
>>> mailgun createContact name:'<NAME>' email:'<EMAIL>' mobile:'<MOBILE>' phone:'<PHONE>' twitter_id:'<TWITTER_ID>' unique_external_id:'<UNIQUE_EXTERNAL_ID>'
{
  "active": false,
  "address": null,
  "company_id": null,
  "view_all_tickets": null,
  "deleted": false,
  "description": null,
  "email": "mock@email.com",
  "id": 48008659871,
  "job_title": null,
  "language": "en",
  "mobile": null,
  "name": "Mock name",
  "phone": null,
  "time_zone": "Chennai",
  "twitter_id": null,
  "custom_fields": {},
  "tags": [],
  "other_emails": [],
  "facebook_id": null,
  "created_at": "2019-08-12T07:41:09Z",
  "updated_at": "2019-08-12T07:41:09Z",
  "other_companies": [],
  "unique_external_id": null,
  "avatar": null
}
```

##### Get Contact
```coffee
>>> mailgun getContact id:<ID>
{
  "active": false,
  "address": null,
  "company_id": null,
  "view_all_tickets": null,
  "description": null,
  "email": "mock@email.com",
  "id": 48008659871,
  "job_title": null,
  "language": "en",
  "mobile": null,
  "name": "Mock name",
  "phone": null,
  "time_zone": "Chennai",
  "twitter_id": null,
  "custom_fields": {},
  "tags": [],
  "other_emails": [],
  "facebook_id": null,
  "created_at": "2019-08-12T07:41:09Z",
  "updated_at": "2019-08-12T07:41:09Z",
  "other_companies": [],
  "unique_external_id": null,
  "avatar": null
}
```

##### Delete Contact
```coffee
>>> mailgun deleteContact id:<ID>
{
  "success": true,
  "message": "Contact deleted successfully."
}
```

##### Get Contact List
```coffee
>>> mailgun listContact
["LIST_OF_CONTACTS"]
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Get Ticket
```shell
$ omg run getTicket -a id=<ID> -e API_KEY=<API_KEY> -e DOMAIN=<DOMAIN>
```

##### Create Ticket
```shell
$ omg run createTicket -a description=<DESCRIPTION> -a subject=<SUBJECT> -a email=<EMAIL> -a priority=<PRIORITY> -a status=<STATUS> -a cc_emails=<CC_EMAILS> -e API_KEY=<API_KEY> -e DOMAIN=<DOMAIN>
```

##### Delete Ticket
```shell
$ omg run deleteTicket -a id=<ID> -e API_KEY=<API_KEY> -e DOMAIN=<DOMAIN>
```

##### Get Ticket List
```shell
$ omg run listTicket -e API_KEY=<API_KEY> -e DOMAIN=<DOMAIN>
```

##### Get Contact
```shell
$ omg run getContact -a id=<ID> -e API_KEY=<API_KEY> -e DOMAIN=<DOMAIN>
```

##### Create Contact
```shell
$ omg run createContact -a name=<NAME> -a email=<EMAIL> -a mobile=<MOBILE> -a phone=<PHONE> -a twitter_id=<TWITTER_ID> -a unique_external_id=<UNIQUE_EXTERNAL_ID> -e API_KEY=<API_KEY> -e DOMAIN=<DOMAIN>
```

##### Delete Contact
```shell
$ omg run deleteContact -a id=<ID> -e API_KEY=<API_KEY> -e DOMAIN=<DOMAIN>
```

##### Get Contact List
```shell
$ omg run listContact -e API_KEY=<API_KEY> -e DOMAIN=<DOMAIN>
```

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/mailgun/blob/master/LICENSE).

