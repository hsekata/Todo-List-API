# To-Do API

This is a simple To-Do API built using Django Rest Framework (DRF) with JWT authentication.

## Features
- User registration
- User authentication (JWT-based)
- CRUD operations for To-Dos


## Authentication
This API uses JWT for authentication. Users must log in to get a token, which must be included in the `Authorization` header for protected endpoints.

### Register a new user
**Endpoint:** `POST /register`
```json
{
  "email": "user@example.com",
  "password": "yourpassword",
  "name": "John Doe"
}
```

### Log in to get a token
**Endpoint:** `POST /login`
```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```
Response:
```json
{
  "access": "<JWT_ACCESS_TOKEN>",
  "refresh": "<JWT_REFRESH_TOKEN>",
}
```

Use the `access` token in the `Authorization` header for all authenticated requests:
```sh
Authorization: Bearer <JWT_ACCESS_TOKEN>
```

## API Endpoints

### Create a To-Do
**Endpoint:** `POST /todos`
- **Authentication required**: Yes
```json
{
  "title": "My first task",
  "description": "Complete the project"
}
```

### Get all To-Dos
**Endpoint:** `GET /todos`
- **Authentication required**: Yes

### Get a single To-Do
**Endpoint:** `GET /todos/{id}/`
- **Authentication required**: Yes

### Update a To-Do (Partial Update - PATCH)
**Endpoint:** `PATCH /todos/{id}/`
- **Authentication required**: Yes
```json
{
  "done": true
}
```

### Update a To-Do (Full Update - PUT)
**Endpoint:** `PUT /todos/{id}/`
- **Authentication required**: Yes
```json
{
  "title": "Updated Task",
  "description": "Updated description",
  "done": true
}
```

### Delete a To-Do
**Endpoint:** `DELETE /todos/{id}/`
- **Authentication required**: Yes
