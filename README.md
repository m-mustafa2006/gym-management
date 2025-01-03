# Gym Website Project

## Overview
This project is a beginner-friendly web application for a gym. It demonstrates how to integrate frontend design using HTML and CSS with backend functionality using Flask, a lightweight Python web framework. The website includes basic pages such as Home, About, Services, Login, and Registration. It is designed to be visually appealing and simple enough for new developers to understand and build upon.

## Purpose
The purpose of this project is to provide an introduction to web development by building a functional multi-page website. It showcases how Flask can manage routes and render HTML templates while keeping the codebase clean and modular.

## Features
1. **Home Page**: A welcoming landing page with a hero section and brief description.
2. **About Page**: Information about the gym and its creators, including a contact email.
3. **Services Page**: A list of gym services displayed in a clean layout.
4. **Login Page**: A simple login form to simulate user authentication.
5. **Registration Page**: A basic registration form for new users.

## Project Structure
```
gym-website/
├── app.py                   # Main Flask application
├── static/                  # Static assets (CSS, images)
│   ├── styles.css           # CSS file for styling
│   └── images/              # Folder for images
│       └── banner.jpg       # Example banner image
├── templates/               # HTML templates
│   ├── base.html            # Base layout template
│   ├── home.html            # Home page template
│   ├── about.html           # About page template
│   ├── services.html        # Services page template
│   ├── login.html           # Login page template
│   └── register.html        # Registration page template
└── README.md                # Project documentation
```

## Requirements
- Python 3.7+
- Flask 2.0+

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/gym-website.git
   cd gym-website
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. **Install Flask**:
   ```bash
   pip install flask
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Website**:
   Open your browser and navigate to `http://127.0.0.1:5000/`.

## Usage
- Navigate through the different pages using the navigation bar.
- Use the Login and Registration forms to simulate user actions (no actual authentication logic is implemented).

## Customization
You can extend this project by:
- Adding a database (e.g., SQLite) for user authentication and data storage.
- Enhancing the design with more advanced CSS or JavaScript frameworks.
- Adding additional features such as a blog, contact form, or schedule page.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the license terms.

## Acknowledgments
This project is intended for educational purposes and serves as a starting point for learning web development with Flask.
# gym-management
