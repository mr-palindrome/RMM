# RMM API

## Description

This is a RESTful API for a remote device management system.

## Prerequisites

- Python (3.x)
- Django
- Django Rest Framework
- djangorestframework-simplejwt
- WebSocket Server (Django Channels)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/mr-palindrome/RMM
   cd RMM
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Install and run Redis:

   - Install Redis: [Redis Installation Guide](https://redis.io/download)
   - Run Redis server locally. Example command:
   
     ```
     redis-server
     ```
4. Add environment variable:
    
    - Create a `.env` file in the root directory of the project.
    - Add the following line to the `.env` file:
    
      ```
      SECRET_KEY="django-insecure-dijyx=b&rgi9u438b_(!kkk5rhzrof2aqd*#caq@+x@#gtn*2^"
      ```

5. Run database migrations:

   ```
   python manage.py migrate
   ```

6. Start the server:

   ```
   python manage.py runserver
   ```

## Usage

### API Endpoints

- `/auth/login/` - `POST` - Login to the API and get an access token.
- `/auth/refresh-token/` - `POST` - Refresh an access token.
- `/auth/verify-token/` - `POST` - Verify an access token.


- `/device/` - `GET` - Get a list of all devices.
- `/device/` - `POST` - Create a new device.
- `/device/<int:pk>/` - `GET` - Get a single device.
- `/device/<int:pk>/` - `PUT` - Update a single device.
- `/device/<int:pk>/` - `DELETE` - Delete a single device.

### WebSocket Server

- `/ws/device_status/` - WebSocket endpoint for device status updates.

### Tkinter Dashboard

- Instructions on how to run and use the Tkinter dashboard:

   ```
   python dashboard.py
   ```

   - This dashboard connects to the WebSocket server to display real-time updates of remote devices.

### Testing the APIs

- Create a superuser:

   ```
   python manage.py createsuperuser
   ```

- You can use the Postman collection in the root directory to test the APIs:

   ```
   RMM.postman_collection.json
   ```


## Authentication

- This API uses JSON Web Tokens (JWT) for authentication.