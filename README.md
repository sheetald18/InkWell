# InkWell
# API Documentation

Welcome to the documentation for our InkWell note taking application API. This document outlines the available endpoints and their functionalities.

## Endpoints

### POST /login

This endpoint is used for user authentication. It creates a simple login view where users can provide their credentials to obtain access.

#### Request Body
- **username**: The username/email of the user.
- **password**: The password of the user.

### POST /signup

The `/signup` endpoint enables users to create a new account. It provides a single user sign-up view where users can register with their details.

#### Request Body
- **username**: The desired username for the new account.
- **password**: The password for the new account.
- **email**: The email address for the new account.

### POST /notes/create

Creates a new note. Users can send a request to this endpoint to create a note with a title and content.

#### Request Body
- **userid**: The userid of the note creator (logged in user).
- **title**: The title of the note.
- **content**: The content of the note.

### GET /notes/{id}

Retrieves a specific note by its ID. Users can provide the ID of the note they want to retrieve, and the endpoint will return the corresponding note.
#### Request Body
- **userid**: The userid of the note which has accessed to note (logged in user).

### POST /notes/share

Shares a note with other users. Users can specify the note they want to share and provide the usernames or IDs of the users they want to share it with.

#### Request Body
- **userid**: The userid of the note owner (logged in user).
- **noteid**: The ID of the note to be shared.
- **userid_list**: An array of IDs of the users to share the note with.

### PUT /notes/{id}

Updates an existing note. Users can provide the ID of the note they want to update along with the new data for the note.

#### Request Body
- **userid**: The userid of the note which has accessed to note (logged in user).
- **title**: (Optional) The new title of the note.
- **content**: (Optional) The new content of the note.

### GET /notes/version-history/{id}

Retrieves all the changes associated with a specific note. Users can provide the ID of the note, and the endpoint will return the version history of that note.
#### Request Body
- **userid**: The userid of the note which has accessed to note (logged in user).

## Error Responses

- **400 Bad Request**: The request is malformed.
- **401 Unauthorized**: Authentication failed.
- **404 Not Found**: Resource not found.
- **500 Internal Server Error**: Unexpected server error.

---

# Running the Python API

To run the Python API file, follow these steps:

1. Ensure you have Python installed on your system. You can download Python from the [official Python website](https://www.python.org/downloads/). Also  Ensure you have MongoDB installed on your system. You can download MongoDB from the [official MongoDB website](https://www.mongodb.com/try/download/community). 

2. Please create database with name "inkwell" in MongoDB along with 2 collections named as "users" and "notes" under same database.

3. Navigate to the directory containing your Python API file using the terminal or command prompt.

4. Install require packages using follwing command :

```bash

pip install -r requirement.txt
```

4. Run the Python API file using the following command:

```bash

python api_file.py
```

Replace `api_file.py` with the name of your Python API file.

4. Once the API server is running, you can use `curl` commands or any API testing tool to interact with the endpoints.

## Curl Commands for APIs

### 1. POST /login

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username/ your email", "password": "your_password"}' http://localhost:5100/login
```

### POST /signup

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password", "email": "your_email@example.com"}' http://localhost:5100/signup
```


### POST /notes/create

```bash
curl -X POST -H "Content-Type: application/json" -d '{{"userid": "logged in user id","title":"note title", "content":"content of your note"}' http://localhost:5100/notes/create
```

### GET /notes/{id}

```bash
curl -X GET -H "Content-Type: application/json" -d '{{"userid": "logged in user id"}' http://localhost:5100/notes/{noteid}
```


### POST /notes/share
```bash
curl -X POST -H "Content-Type: application/json" -d '{{"userid": "logged in user id","noteid":"note id to share with users", "userid_list":["id of user 1", "id of user 2"]}' http://localhost:5100/notes/share
```



### PUT /notes/{id}
```bash
curl -X PUT -H "Content-Type: application/json" -d '{{"userid": "logged in user id","title":"note title", "content":"content of your note"}' http://localhost:5100/notes/{noteid}
```


### GET /notes/version-history/{id}
```bash
curl -X GET -H "Content-Type: application/json" -d '{{"userid": "logged in user id"}' http://localhost:5100/notes/version-history/{noteid}
```

These curl commands can be used in the terminal or command prompt to interact with your API endpoints.

If you have any questions or need further assistance, please don't hesitate to contact me.

