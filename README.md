# Clean Architecture

This project is described a clean architecture written by Robert C. Martine.
Architecture is fellow a [clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)



## Table of contents

- [Features](#features)
- [Directory Structure](#diretory-structure)
- [Installation](#installation)
- [Example](#example)
- [Testing](#testing)
- [Contribution](#contribution)

## Features

 Some features I've included in this application are:

- Tests are gonna be written by for [pytest](http://pytest.org/)

## Directory Structure

```bash
|-- clean_architecture
|    |-- domain
|    |	|-request_object.py
|    |	|-response_object.py
|    |	`-use_case.py
|    |-- entity
|    |	`-entity.py
|    |-- exception
|    |	|-exception.py
|    |	`- *_exception.py
|    |-- serializer
|    	`-serializer.py
```



## Design Choices

### Clean Architecture

The clean architecture has three area **Rest**, **Domain** and **Serializer**.

#### Rest

It's handling with api request and response. It transfers a request data to a request object and calls a domain mapped each rest api. If a domain logic finished, It should be response result of domain logic whether success or fail.

#### Domain 

It has a **Repository** and **Entity**. It controls response data with **Repository ** and **Entity**. 

##### Repository

This is to control storing data on any store(ex. database, file storage, aws s3, ...)

##### Entity

This is to transfer data scheme for each repository.

#### Serializer

It's frame about response data.

### RBAC(Role Base Access Control)

Blah~~

## Installation

### Requirements

- Python^=3.7
- Postegresql^=10.5
- Celery^=4.2.1



### Commands

- First, download source code

    ```bash
    $ git clone https://{remote-account}@bitbucket.org/thepaycheckservice/paycheck_app_service.git
    ```

    and download submodule source code

    ```bash
    $ git submodule init
    $ git submodule update
    ```

- Second, set up virtualenv

    ```bash
    $ cd paycheck_app_service
    $ virtualenv -p python3 venv
    ```

- Third, create .env file on **/**

    ```bash
    $ touch .env
    ```
    and write following environment variable on a .env file

    ```.env
    SQLALCHEMY_DATABASE_URI=${{SQLALCHEMY_DATABASE_URI}}
    SECRET_KEY=${{SECRET_KEY}}
    CELERY_BROKER_URL=${{CELERY_BROKER_URL}}
    CELERY_RESULT_BACKEND=${{CELERY_RESULT_BACKEND}}
    UPLOAD_TEMP_PATH=${{UPLOAD_TEMP_PATH}}
    S3_BUCKET=${{S3_BUCKET}}
    S3_ACCESS_KEY=${{S3_ACCESS_KEY}}
    S3_SECRET_KEY=${{S3_SECRET_KEY}}
    S3_REGION_NAME=${{S3_REGION_NAME}}
    ```

- Forth, install pip on venv

    ```bash
    $ source venv/bin/activate
    (venv) $ pip install -e .
    ```



**!!** *If database don't set up schema, you have to migrate set up*

    ```bash
    (venv) $ paycheck db init
    (venv) $ paycheck db migrate
    (venv) $ paycheck db upgrade
    ```



## Running

If you complete an installation this application, move the root directory on project. 

    ```bash
    $ cd ~/project-root-directory 
    ```

and activate virturalenv.

    ```bash 
    $ source /venv/bin/activate
    ```

and just run this application

    ```bash
    (venv) $ paycheck run 
    ```

If you use a gunicorn, put on terminal this command

    ```bash
    # Develop mode
    (venv) $  gunicorn --log-level debug --reload --bind 0.0.0.0:5000 paycheck.wsgi:app
    # Deploye mode
    (venv) $  gunicorn --bind 0.0.0.0:5000 paycheck.wsgi:app &
    ```



### Docker

Blah blah



## Testing

Blah blah



## Contribution

Blah Blah









