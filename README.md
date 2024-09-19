# User Details API

A Django-based API that fetches user details from the JSONPlaceholder API and returns a modified response containing selected user information.

## Features

- Fetches user data from an external API.
- Returns a structured response with user ID, name, latitude, longitude, and company name.
- Handles errors gracefully.

## Technologies Used

- Django
- Django REST Framework
- Python
- Requests library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shreyapate/display_user_data.git
2. Run developement server:
   python manage.py runserver
3. Access the API:
   Open your browser and go to http://127.0.0.1:8000/get/user/details/
4. Example Response:
[
{
"id": 1,
"name": "Leanne Graham",
"lat": "-37.3159",
"lng": "81.1496",
"company_name": "Romaguera-Crona"
}
]
5.Error Handling:
"There was an error in getting response!"
