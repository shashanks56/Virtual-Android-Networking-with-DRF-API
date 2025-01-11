### Backend Development

This project provides a REST API for the following endpoints:
1. POST: Add app details to the database.
2. GET: Retrieve app details by ID.
3. DELETE: Remove an app by ID.

## Setting Up and Running Locally

Follow these steps to set up the API on your local machine:

1. Extract the zip file to a folder on your computer.
   Navigate to the project directory:
   ```  
   cd <extracted_folder_name>
   ```

2. Set up the environment and install dependencies:
   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure and initialize the database:
   ```
   python manage.py migrate
   ```

4. Start the development server:
   ```
   python manage.py runserver
   ```

The API will be accessible at `http://127.0.0.1:8000/`

- **POST**: Add app details
  URL: `http://127.0.0.1:8000/api/add_app/`

- **GET**: Retrieve app details by ID
  URL: `http://127.0.0.1:8000/api/get_app/<id>/`  
  Replace `<id>` with the desired application's ID.

- **DELETE**: Remove an app by ID
  URL: `http://127.0.0.1:8000/api/delete_app/<id>/`  
  Replace `<id>` with the desired application's ID.
