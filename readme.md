# MovieSign Project

## Overview
MovieSign is a Django-based web application that allows users to view and manage movie screenings in various cinema rooms. The application uses Django Channels for real-time updates via WebSockets.

## Features
- View cinema details and upcoming screenings
- Real-time updates for screening statuses
- Responsive design using Tailwind CSS

<img height="250" alt="Screenshot 2025-02-02 at 14 11 25" src="https://github.com/user-attachments/assets/51bd7614-118c-470e-b602-9ab0f200fb9d" /><img height="250" alt="Screenshot 2025-02-02 at 14 12 08" src="https://github.com/user-attachments/assets/fd31d889-05c0-4639-baad-61d25e8d9c87" />



## Requirements
- Python 3.8+
- Django 5.1
- Redis server

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/moviesign.git
cd moviesign
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up Redis
Ensure you have Redis installed and running. You can install Redis using the following commands:

#### On macOS
```bash
brew install redis
brew services start redis
```

#### On Ubuntu
```bash
sudo apt update
sudo apt install redis-server
sudo systemctl enable redis-server.service
sudo systemctl start redis-server.service
```

### 5. Create a `.env` file
Create a `.env` file in the root directory of your project and add the secret key:
```env
SECRET_KEY=*your_secret_key_here*
```

### 6. Configure Django settings
Update the `settings.py` file with your configuration. Ensure the `CHANNEL_LAYERS` setting is configured to use Redis:
```python
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

### 7. Apply migrations
```bash
python manage.py migrate
```

### 8. Run the development server
```bash
python manage.py runserver
```

## Usage
- Access the application at `http://127.0.0.1:8000/`
- Navigate to different cinema rooms to view and manage screenings
- Real-time updates will be reflected automatically

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
```
