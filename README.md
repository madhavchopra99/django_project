## Django Blog Application

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a fully functional blog site built with Django, featuring user authentication, blog post management, comments, and user profiles.

## Features

- ✅ User Registration, Login, and Logout
- ✅ Create, Read, Update, and Delete blog posts
- ✅ Add comments to posts
- ✅ User profiles with custom profile pictures
- ✅ Search functionality for blog posts
- ✅ Pagination for posts and comments
- ✅ Password reset functionality
- ✅ Responsive design
- ✅ Admin interface

## Technologies

- Python 3.8+
- Django 3.0+
- SQLite (default database)
- Bootstrap 4 (via crispy forms)
- PIL/Pillow for image processing
- Django REST Framework (not used but available for future API development)

## Project Structure

```
django_project/
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── post_search_list.html
│   │       ├── user_posts.html
│   │       └── about.html
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── users/
│   ├── migrations/
│   ├── templates/
│   │   └── users/
│   │       ├── register.html
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── password_reset_*.html
│   │       └── profile.html
│   ├── views.py
│   ├── forms.py
│   └── models.py
├── django_project/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── README.md
├── requirements.txt
└── media/
    └── profile_pics/
    └── posts/
```

## Prerequisites

- Python 3.8 or higher
- Django 3.0 or higher
- Git
- SQLite3
- ImageMagick (for profile picture processing)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd django_project
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root with the following variables:

```env
EMAIL_ID=your_email@gmail.com
EMAIL_PASS=your_email_password
SECRET_KEY='ohbe@gs6gt80vnc^fw1@ijw@o+kmk6dnnwuf-!t&9r!+lpk%$*'
DEBUG=True
ALLOWED_HOSTS=
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

## Running the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Admin Interface

Access the admin panel at `http://localhost:8000/admin/` with your superuser credentials.

## Media Files

Media files (profile pictures and uploaded images) are stored in the `media/` directory. Ensure this directory is writable by the web server.

## Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure proper ALLOWED_HOSTS
3. Use a production-ready database (PostgreSQL, MySQL, etc.)
4. Set up SSL/TLS
5. Use a WSGI server like Gunicorn
6. Configure a reverse proxy like Nginx
7. Set up proper static files handling

## Usage

1. **Register**: Visit `/register/` to create a new account
2. **Login**: Visit `/login/` to access your account
3. **Create Post**: Visit `/` to create a new blog post
4. **View Posts**: Browse blog posts on the home page
5. **Profile**: Visit `/profile/` to manage your profile and posts
6. **Search**: Use the search bar to find posts

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django team for the excellent framework
- Bootstrap and crispy forms for rapid development
- The open source community

## Contact

If you have any questions, please open an issue or contact me through GitHub.