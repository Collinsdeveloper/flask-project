# Flask Full CRUD RESTful API

## Overview

This project is a simple RESTful API built with Flask that performs full CRUD (Create, Read, Update, Delete) operations on event data. Event information is stored in memory using a Python list, meaning all data resets when the server is restarted.

## Features

* View all events
* Create new events
* Update existing events
* Delete events
* Return JSON responses
* Use appropriate HTTP status codes

## Technologies Used

* Python 3
* Flask

## How the Application Works

### Event Class

The `Event` class represents an event and contains:

* `id` – Unique event identifier
* `title` – Event name

The `to_dict()` method converts an event object into a dictionary that can be returned as JSON.

### Data Storage

Events are stored in an in-memory list:

```python
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]
```

### API Endpoints

| Method | Endpoint       | Description               |
| ------ | -------------- | ------------------------- |
| GET    | `/`            | Returns a welcome message |
| GET    | `/events`      | Returns all events        |
| POST   | `/events`      | Creates a new event       |
| PATCH  | `/events/<id>` | Updates an event          |
| DELETE | `/events/<id>` | Deletes an event          |

## Running the Application

Activate the virtual environment:

```bash
source venv/bin/activate
```

Run the Flask application:

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000
```

## Example Request

Create a new event:

```bash
curl -X POST http://127.0.0.1:5000/events \
-H "Content-Type: application/json" \
-d '{"title":"Hackathon"}'
```

## Learning Objectives

This project demonstrates:

* Flask routing
* RESTful API design
* CRUD operations
* JSON request and response handling
* HTTP status codes
* Python classes and functions
