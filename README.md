# Banking System

A Django web application for managing a simple banking workflow with users, employees, banks, accounts, approval messages, and check redemption.

The project models three main user roles:

- **Client** - opens accounts, closes accounts, changes bank, redeems checks, and checks balances.
- **Employee** - receives client requests and approves or rejects account operations.
- **Third person** - sends checks to clients.

The application uses Django authentication, a custom user model, SQLite for local development, and separate Django apps for banking, account operations, users, and messages.

## Features

- User registration and login
- Role-based registration for clients, employees, and third-party users
- Custom user model with EGN, age, and role fields
- Bank creation by admin users
- Employee assignment to banks
- Client account opening requests
- Client account closing requests
- Bank change requests for existing accounts
- Employee approval and rejection workflow
- Internal message pages for users and employees
- Check sending by third-party users
- Check redemption by clients
- Balance checking
- Django admin support
- Automated tests for forms, URLs, and views

## Tech Stack

- Python
- Django
- SQLite
- HTML templates
- CSS static files

## Project Structure

```text
banking_system/
|-- account/        # Account operations, checks, balances, approval requests
|-- bank/           # Bank models, forms, and bank creation
|-- bankSystem/     # Main Django project settings and URL configuration
|-- posts/          # Welcome page, profile page, messages, approvals
|-- static/         # CSS and static assets
|-- templates/      # Shared base layout
|-- users/          # Custom users, registration, login, employee assignment
|-- db.sqlite3      # Local SQLite database
|-- logic.py        # Helper banking logic
|-- manage.py       # Django management script
`-- README.md
```

## Main URLs

| URL | Description |
| --- | --- |
| `/` | Redirects to `/posts/welcome/` |
| `/admin/` | Django admin panel |
| `/posts/welcome/` | Welcome page |
| `/posts/message/` | User or employee messages |
| `/posts/profile/` | User profile |
| `/users/register/` | Select registration role |
| `/users/login/` | Login |
| `/users/logout/` | Logout |
| `/users/add_employee/` | Assign an employee to a bank |
| `/bank/create_bank/` | Create a bank |
| `/account/open_account/` | Request account opening |
| `/account/close_account/` | Request account closing |
| `/account/change_bank/` | Request moving an account to another bank |
| `/account/send_check/` | Send a check |
| `/account/redem_check/` | Redeem a check |
| `/account/check_balance/` | Check account balance |

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd banking_system
```

### 2. Create and activate a virtual environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Install Django manually:

```bash
pip install django
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open the app at:

```text
http://127.0.0.1:8000/
```

## Typical Workflow

1. Create a superuser.
2. Log in to the admin panel.
3. Create one or more banks.
4. Register users with different roles.
5. Assign employees to banks.
6. Log in as a client and request an account operation.
7. Log in as an employee and approve or reject the request.
8. Use the message pages to track request status.

## Running Tests

Run all tests with:

```bash
python manage.py test
```

The project includes tests for:

- `account`
- `bank`
- `posts`
- `users`

## Notes

- This project is configured for local development with `DEBUG = True`.
- SQLite is used as the default database.
- The root URL `/` redirects to `/posts/welcome/`, so the project does not require `home.html` or `about.html`.
- Before deploying, move secrets out of `settings.py`, set `DEBUG = False`, configure `ALLOWED_HOSTS`, and use a production-ready database.

## License

This project is for educational purposes.
