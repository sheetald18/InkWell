# InkWell
# API Documentation

Welcome to the documentation for our API. This document outlines the available endpoints and their functionalities.

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

If you have any questions or need further assistance, please don't hesitate to contact me.

