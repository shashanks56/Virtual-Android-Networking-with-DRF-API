# Virtual-Android-Networking-with-DRF-API

A project integrating backend API development using Django REST Framework, Android system simulation, and data communication between the simulator and the backend server.

Features:
  -Backend API: Perform CRUD operations to manage app data. 
  -Virtual Android Simulation: Simulate an Android environment using ADB commands. 
  -Networking: Send mock data (e.g., device information) to the backend server and log responses.

Setup: { Task-Specific Setup is also given, navigate to individual task directories and follow the instructions in their README files}.

#Prerequisites: 
  -Python 3.8+: Ensure Python is installed. 
  -Android SDK: Includes ADB and emulator tools. 
  -Django: Install using pip install django. 
  -Django REST Framework: Install using pip install djangorestframework.

Steps:

Clone the Repository:

#Set Up the Backend API: 
  -Navigate to the API directory. 
  -Run the following commands: 
              `python manage.py migrate   
               python manage.py runserver`

#Run the Emulator Scripts: 
  -Ensure the Android Emulator and ADB are set up. 
  -Run the emulator script from the Emulator directory to simulate the Android environment.

#Networking Script: 
  -Use the script in networking to send mock data from the simulator to the backend API.

Tech Stack: 
  -Python: Core language for backend and scripting. 
  -Django REST Framework: For creating robust APIs. 
  -SQLite: Lightweight database for data storage. 
  -Android Emulator: To simulate the virtual Android environment.
