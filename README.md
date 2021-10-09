# Data Engineering 1
[![License](https://img.shields.io/github/license/jads-master-team-1/de-1)](https://github.com/jads-master-team-1/de-1/blob/master/LICENSE)

Project for assignment 1 of the Data Engineering course of the [Master Data Science & Entrepreneurship](https://www.jads.nl/education/master-data-science-entrepreneurship/).

# How To Run

Prerequisites:
* docker version ```20.10.8``` or later
* docker-compose version ```1.27.4``` or later
* make version ```4.2.1``` or later (optional)

### Development

1. Run ```docker-compose -p data_engineering_1_dev -f docker-compose.dev.yml build``` or ```make build/dev``` to build the containers (optional).
2. Run ```docker-compose -p data_engineering_1_dev -f docker-compose.dev.yml up``` or ```make run/dev``` to start the containers.

### Production

1. Run ```docker-compose -p data_engineering_1_prod -f docker-compose.prod.yml build``` or ```make build/prod``` to build the containers (optional).
2. Run ```docker-compose -p data_engineering_1_prod -f docker-compose.prod.yml up``` or ```make run/prod``` to start the containers.

Run ```make init``` to install the requirements of each service on your local machine (optional).

# Architecture

### App

The application consists out of 5 individual components. Each component runs in it's own docker container. All communication between the components runs over the [http](https://developer.mozilla.org/en-US/docs/Web/HTTP) protocol.

![App Architecture Diagram](/docs/app-architecture.png?raw=true)

### Service

Each of the services follows the [3-Tier Architecture Model](https://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture). The resources layer is responsible for communicating with the users or other services. It handles incoming API requests and passes the parsed data to the interactions layer. The interactions layer is the business layer in the service. It sits in between the resources and repositories layer and determines what actions need to be taken to fulfill a user's or other service's request. The repositories layer is the data layer. This layer is responsible for communicating with databases, storage systems or other services.

![Service Architecture Diagram](/docs/service-architecture.png?raw=true)

# Specification

### Database

#### GET: `/api/models/`

Retrieves the current model from the database.

##### Request

```json
-
```

##### Response

```json
{
    "id": 1,
    "file": "43ef3586395168439d53e5c776ea3e4b.pkl",
    "created_on": "2021-01-01T00:00:00.000000",
    "updated_on": "2021-01-01T00:00:00.000000"
}
```

#### POST: `/api/models/`

Stores a new model in the database.

##### Request

```json
{
    "file": "43ef3586395168439d53e5c776ea3e4b.pkl"
}
```

##### Response

```json
{
    "id": 1,
    "file": "43ef3586395168439d53e5c776ea3e4b.pkl",
    "created_on": "2021-01-01T00:00:00.000000",
    "updated_on": "2021-01-01T00:00:00.000000"
}
```

#### GET: `/api/predictions/`

Retrieves all predictions from the database.

##### Request

```json
-
```

##### Response

```json
[
    {
        "id": 1,
        "input": [5.7, 3.0, 4.2, 1.2],
        "output": 1,
        "created_on": "2021-01-01T00:00:00.000000",
        "updated_on": "2021-01-01T00:00:00.000000"
    },
    {
        "id": 2,
        "input": [6.8, 3.2, 5.9, 2.3],
        "output": 2,
        "created_on": "2021-01-01T00:00:00.000000",
        "updated_on": "2021-01-01T00:00:00.000000"
    }
]
```

#### POST: `/api/predictions/`

Stores a new prediction in the database.

##### Request

```json
{
    "input": [5.7, 3.0, 4.2, 1.2],
    "output": 1
}
```

##### Response

```json
{
    "id": 1,
    "input": [5.7, 3.0, 4.2, 1.2],
    "output": 1,
    "created_on": "2021-01-01T00:00:00.000000",
    "updated_on": "2021-01-01T00:00:00.000000"
}
```

### Predictor

#### POST: `/api/predictions/`

Creates a new prediction.

##### Request

```json
[
    5.7,
    3.0,
    4.2,
    1.2
]
```

##### Response

```json
{
    "id": 1,
    "input": [5.7, 3.0, 4.2, 1.2],
    "output": 1,
    "created_on": "2021-01-01T00:00:00.000000",
    "updated_on": "2021-01-01T00:00:00.000000"
}
```

#### PUT: `/api/models/`

Updates to the latest model stored the database and storage system.

##### Request

```json
-
```

##### Response

```json
-
```

### Storage

#### GET: `/api/files/<name>`

Loads a file from the storage system.

##### Request

```text
-
```

##### Response

```json
file=@/path/to/model.pkl
```

#### POST: `/api/files/`

Stores a file on the storage system.

**Note:** This request uses `multipart/form-data` to upload the file (see [docs](https://learning.postman.com/docs/sending-requests/requests/#form-data) or [video](https://www.youtube.com/watch?v=S7bwkys6D0E)).

##### Request

```text
file=@/path/to/model.pkl
```

##### Response

```json
{
    "name": "43ef3586395168439d53e5c776ea3e4b.pkl"
}
```

### Visualization

#### POST: `/api/visualization/`

Creates a new visualization from provided predictions.

##### Request

```json
[
    {
        "id": 1,
        "input": [5.7, 3.0, 4.2, 1.2],
        "output": 1,
        "created_on": "2021-01-01T00:00:00.000000",
        "updated_on": "2021-01-01T00:00:00.000000"
    },
]
```

##### Response

```text
file=@/path/to/visualization.png
```

### Web

#### POST: `/api/models/`

Stores a new model in the database and storage system.

**Note:** This request uses `multipart/form-data` to upload the model (see [docs](https://learning.postman.com/docs/sending-requests/requests/#form-data) or [video](https://www.youtube.com/watch?v=S7bwkys6D0E)).

##### Request

With cURL: `curl -X POST http://localhost:8080/api/models/ -F 'file=@iris-svc-v0.1.0.pkl`

```text
file=@/path/to/model.pkl
```

##### Response

```json
{
    "id": 1,
    "file": "43ef3586395168439d53e5c776ea3e4b.pkl",
    "created_on": "2021-01-01T00:00:00.000000",
    "updated_on": "2021-01-01T00:00:00.000000"
}
```

#### GET: `/api/predictions/`

Retrieves all predictions from the database.

##### Request

With cURL: `curl -X GET http://localhost:8080/api/predictions/`

```json
-
```

##### Response

```json
[
    {
        "id": 1,
        "input": [5.7, 3.0, 4.2, 1.2],
        "output": 1,
        "created_on": "2021-01-01T00:00:00.000000",
        "updated_on": "2021-01-01T00:00:00.000000"
    },
    {
        "id": 2,
        "input": [6.8, 3.2, 5.9, 2.3],
        "output": 2,
        "created_on": "2021-01-01T00:00:00.000000",
        "updated_on": "2021-01-01T00:00:00.000000"
    }
]
```

#### POST: `/api/predictions/`

Creates a new prediction and stores it in the database.

##### Request

With cURL: `curl -X POST http://localhost:8080/api/predictions/ -H 'Content-Type: application/json' -d '[5.7, 3.0, 4.2, 1.2]'`

With cURL: `curl -X POST http://localhost:8080/api/predictions/ -H 'Content-Type: application/json' -d '[6.8, 3.2, 5.9, 2.3]'`

```json
[
    5.7,
    3.0,
    4.2,
    1.2
]
```

##### Response

```json
{
    "id": 1,
    "input": [5.7, 3.0, 4.2, 1.2],
    "output": 1,
    "created_on": "2021-01-01T00:00:00.000000",
    "updated_on": "2021-01-01T00:00:00.000000"
}
```

#### GET: `/api/visualization/`

Creates a visualization from all predictions.

##### Request

With cURL: `curl -X GET http://localhost:8080/api/visualization/ > visualization.png`

```json
-
```

##### Response

```text
file=@/path/to/visualization.png
```

# References

[Python Docs](https://docs.python.org/3/)

[Docker Docs](https://docs.docker.com/)

[Docker Compose Docs](https://docs.docker.com/compose/)

[Black Formatter Docs](https://black.readthedocs.io/en/stable/)

[Pylint Linter Docs](https://pylint.pycqa.org/en/latest/)

[Flask Web Framework Docs](https://flask.palletsprojects.com/en/2.0.x/)

[Flask SQLAlchemy Docs](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

[SQLAlchemy Database ORM Docs](https://docs.sqlalchemy.org/en/14/)

[Requests Web Client Docs](https://docs.python-requests.org/en/latest/)
