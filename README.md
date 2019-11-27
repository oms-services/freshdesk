# _Freshdesk_ Open Microservice

> Freshdesk as a microservice

[![Open Microservice Specification Version](https://img.shields.io/badge/Open%20Microservice-1.0-477bf3.svg)](https://openmicroservices.org)
[![Open Microservices Spectrum Chat](https://withspectrum.github.io/badge/badge.svg)](https://spectrum.chat/open-microservices)
[![Open Microservices Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md)
[![Open Microservices Commitzen](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Introduction

This project is an example implementation of the [Open Microservice Specification](https://openmicroservices.org), a standard
originally created at [Storyscript](https://storyscript.io) for building highly-portable "microservices" that expose the
events, actions, and APIs inside containerized software.

## Getting Started

The `oms` command-line interface allows you to interact with Open Microservices. If you're interested in creating an Open
Microservice the CLI also helps validate, test, and debug your `oms.yml` implementation!

See the [oms-cli](https://github.com/microservices/oms) project to learn more!

### Installation

```
npm install -g @microservices/oms
```

## Usage

### Open Microservices CLI Usage

Once you have the [oms-cli](https://github.com/microservices/oms) installed, you can run any of the following commands from
within this project's root directory:

#### Actions

##### getTicket

> Get ticket by id

##### Action Arguments

| Argument Name | Type     | Required | Default | Description                                                      |
| :------------ | :------- | :------- | :------ | :--------------------------------------------------------------- |
| id            | `int`    | `true`   | None    | No description provided.                                         |
| API_KEY       | `string` | `true`   | None    | A Freshdesk `API_KEY`                                            |
| DOMAIN        | `string` | `true`   | None    | A Freshdesk account Domain name: https://{DOMAIN}.freshdesk.com/ |

```shell
oms run getTicket \
    -a id='*****' \
    -e API_KEY=$API_KEY \
    -e DOMAIN=$DOMAIN
```

##### createTicket

> Create new ticket

##### Action Arguments

| Argument Name | Type     | Required | Default | Description                                                      |
| :------------ | :------- | :------- | :------ | :--------------------------------------------------------------- |
| description   | `string` | `true`   | None    | No description provided.                                         |
| subject       | `string` | `true`   | None    | No description provided.                                         |
| email         | `string` | `true`   | None    | No description provided.                                         |
| priority      | `int`    | `false`  | None    | No description provided.                                         |
| status        | `int`    | `false`  | None    | No description provided.                                         |
| ccEmails      | `list`   | `false`  | None    | No description provided.                                         |
| API_KEY       | `string` | `true`   | None    | A Freshdesk `API_KEY`                                            |
| DOMAIN        | `string` | `true`   | None    | A Freshdesk account Domain name: https://{DOMAIN}.freshdesk.com/ |

```shell
oms run createTicket \
    -a description='*****' \
    -a subject='*****' \
    -a email='*****' \
    -a priority='*****' \
    -a status='*****' \
    -a ccEmails='*****' \
    -e API_KEY=$API_KEY \
    -e DOMAIN=$DOMAIN
```

##### deleteTicket

> Delete ticket by id

##### Action Arguments

| Argument Name | Type     | Required | Default | Description                                                      |
| :------------ | :------- | :------- | :------ | :--------------------------------------------------------------- |
| id            | `int`    | `true`   | None    | No description provided.                                         |
| API_KEY       | `string` | `true`   | None    | A Freshdesk `API_KEY`                                            |
| DOMAIN        | `string` | `true`   | None    | A Freshdesk account Domain name: https://{DOMAIN}.freshdesk.com/ |

```shell
oms run deleteTicket \
    -a id='*****' \
    -e API_KEY=$API_KEY \
    -e DOMAIN=$DOMAIN
```

##### listTicket

> Get all tickets

##### Action Arguments

| Argument Name | Type     | Required | Default | Description                                                      |
| :------------ | :------- | :------- | :------ | :--------------------------------------------------------------- |
| API_KEY       | `string` | `true`   | None    | A Freshdesk `API_KEY`                                            |
| DOMAIN        | `string` | `true`   | None    | A Freshdesk account Domain name: https://{DOMAIN}.freshdesk.com/ |

```shell
oms run listTicket \
    -e API_KEY=$API_KEY \
    -e DOMAIN=$DOMAIN
```

##### getContact

> Get contact by id

##### Action Arguments

| Argument Name | Type     | Required | Default | Description                                                      |
| :------------ | :------- | :------- | :------ | :--------------------------------------------------------------- |
| id            | `int`    | `true`   | None    | No description provided.                                         |
| API_KEY       | `string` | `true`   | None    | A Freshdesk `API_KEY`                                            |
| DOMAIN        | `string` | `true`   | None    | A Freshdesk account Domain name: https://{DOMAIN}.freshdesk.com/ |

```shell
oms run getContact \
    -a id='*****' \
    -e API_KEY=$API_KEY \
    -e DOMAIN=$DOMAIN
```

##### createContact

> Create new contact

##### Action Arguments

| Argument Name    | Type     | Required | Default | Description                                                      |
| :--------------- | :------- | :------- | :------ | :--------------------------------------------------------------- |
| name             | `string` | `true`   | None    | No description provided.                                         |
| email            | `string` | `false`  | None    | No description provided.                                         |
| mobile           | `int`    | `false`  | None    | No description provided.                                         |
| phone            | `string` | `false`  | None    | No description provided.                                         |
| twitterId        | `string` | `false`  | None    | No description provided.                                         |
| uniqueExternalId | `list`   | `false`  | None    | No description provided.                                         |
| API_KEY          | `string` | `true`   | None    | A Freshdesk `API_KEY`                                            |
| DOMAIN           | `string` | `true`   | None    | A Freshdesk account Domain name: https://{DOMAIN}.freshdesk.com/ |

```shell
oms run createContact \
    -a name='*****' \
    -a email='*****' \
    -a mobile='*****' \
    -a phone='*****' \
    -a twitterId='*****' \
    -a uniqueExternalId='*****' \
    -e API_KEY=$API_KEY \
    -e DOMAIN=$DOMAIN
```

##### deleteContact

> Delete contact by id

##### Action Arguments

| Argument Name | Type     | Required | Default | Description                                                      |
| :------------ | :------- | :------- | :------ | :--------------------------------------------------------------- |
| id            | `int`    | `true`   | None    | No description provided.                                         |
| API_KEY       | `string` | `true`   | None    | A Freshdesk `API_KEY`                                            |
| DOMAIN        | `string` | `true`   | None    | A Freshdesk account Domain name: https://{DOMAIN}.freshdesk.com/ |

```shell
oms run deleteContact \
    -a id='*****' \
    -e API_KEY=$API_KEY \
    -e DOMAIN=$DOMAIN
```

##### listContact

> Get all contacts

##### Action Arguments

| Argument Name | Type     | Required | Default | Description                                                      |
| :------------ | :------- | :------- | :------ | :--------------------------------------------------------------- |
| API_KEY       | `string` | `true`   | None    | A Freshdesk `API_KEY`                                            |
| DOMAIN        | `string` | `true`   | None    | A Freshdesk account Domain name: https://{DOMAIN}.freshdesk.com/ |

```shell
oms run listContact \
    -e API_KEY=$API_KEY \
    -e DOMAIN=$DOMAIN
```

## Contributing

All suggestions in how to improve the specification and this guide are very welcome. Feel free share your thoughts in the
Issue tracker, or even better, fork the repository to implement your own ideas and submit a pull request.

[![Edit freshdesk on CodeSandbox](https://codesandbox.io/static/img/play-codesandbox.svg)](https://codesandbox.io/s/github/oms-services/freshdesk)

This project is guided by [Contributor Covenant](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md).
Please read out full [Contribution Guidelines](https://github.com/oms-services/.github/blob/master/CONTRIBUTING.md).

## Additional Resources

- [Install the CLI](https://github.com/microservices/oms) - The OMS CLI helps developers create, test, validate, and build
  microservices.
- [Example OMS Services](https://github.com/oms-services) - Examples of OMS-compliant services written in a variety of
  languages.
- [Example Language Implementations](https://github.com/microservices) - Find tooling & language implementations in Node,
  Python, Scala, Java, Clojure.
- [Storyscript Hub](https://hub.storyscript.io) - A public registry of OMS services.
- [Community Chat](https://spectrum.chat/open-microservices) - Have ideas? Questions? Join us on Spectrum.
