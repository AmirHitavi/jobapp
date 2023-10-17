# JobApp Project

This is a simple  Django project for a job posting and subscription website called JobApp.

## Requirements
- Git
- Python
- Django

## Installation

1. Clone the repository: 
   ```
   git clone jobapp
   ```
2. Setup and activate a virtual environment:
   ```
   python -m venv env
   source env/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Open your web browser and access the application at `http://localhost:8000`.

you can also have access to the admin panel with username `admin` and password `12345678`.

## Usage

- The homepage displays list of all jobs.
- Click on a job post to view its details.
- To subscribe to the newsletter, go to the `Subscribe` page, fill out the form, and click Submit.

## Project Structure

- `app/` - Contains the main application files and views related to job posts.
- `subscribe/` - Contains the files and views related to newsletter subscription.
- `templates/` - Contains HTML templates for rendering views.
- `static/` - Contains static files such as CSS and JavaScript.

### Thank you
