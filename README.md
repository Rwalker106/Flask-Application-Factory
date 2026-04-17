# Cafe & Wifi Directory

A stylish, full-stack Flask application designed to manage a curated directory of coffee shops, specifically tailored for remote workers, digital nomads, and students looking for a good working environment.

## Features

- **Full CRUD Functionality**: Easily Create, Read, Update, and Delete cafe entries straight from your web browser.
- **Interactive Directory Table**: Seamlessly view important cafe amenities at a glance (Sockets, Toilet, WiFi, Phone Calling, Seats, etc.).
- **SQLite Database Integration**: Powered by SQLAlchemy ORM to reliably store detailed cafe data.
- **Form Validation**: Clean and robust backend form processing using Flask-WTF and Bootstrap-Flask.
- **Premium UI/UX Engine**: Completely custom-styled frontend CSS matching a sleek, responsive design scheme featuring a beautiful gradient navigation bar and micro-animations.

## Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd cafe-and-wifi-portfolio-project
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```powershell
     .\.venv\Scripts\activate
     ```
   - **MacOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install required dependencies:**
   Ensure your virtual environment is active, then run:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Insert required environment variables (replace with your own key):
     ```env
     SECRET_KEY=your_secret_flask_key_here
     ```

6. **Run the Application:**
   Start your development server directly with Python:
   ```bash
   python run.py
   ```
   *The application will boot up at http://127.0.0.1:5000/*

## Repository Structure

- `app/`: Main application package including routes, templates, and static CSS/JS files.
- `instance/`: Local database storage directory (`cafes.db`).
- `run.py`: The application entry point script.
