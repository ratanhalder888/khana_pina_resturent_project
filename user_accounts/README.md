# User Accounts

This Django app handles user authentication and registration for the project. It supports both standard Token-based authentication and JWT (JSON Web Token) authentication.

## Features

- **User Registration**: Endpoints for creating new user accounts.
- **Authentication**:
    - **Token Authentication**: Uses Django REST Framework's built-in token authentication.
    - **JWT Authentication**: Uses `djangorestframework-simplejwt` for secure, stateless authentication.
- **Logout**: Endpoint to invalidate tokens (for Token Authentication).

## API Endpoints

### Token Authentication

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/token-login/` | Obtain an authentication token by providing username and password. |
| `POST` | `/token-register/` | Register a new user and receive an authentication token immediately. |
| `POST` | `/token-logout/` | Logout the current user by deleting their authentication token. |

### JWT Authentication

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/token/` | Obtain a JWT access and refresh token pair. |
| `POST` | `/api/token/refresh/` | Refresh an access token using a refresh token. |
| `POST` | `/api/token/verify/` | Verify if a token is valid. |
| `POST` | `/api/token/jwt-register/` | Register a new user and receive JWT access and refresh tokens. |

## Configuration

This app requires the following packages to be installed and configured in `settings.py`:

- `djangorestframework`
- `djangorestframework-simplejwt`

Ensure `user_accounts` is added to your `INSTALLED_APPS`.
