# Database Management

# Database Schema
The database schema is defined in the `schema.sql` file. 
It creates the `api_app` table with the following columns:

**id**: Primary key
**app_name**: Name of the app (varchar, max length 105)
**version**: Version of the app (varchar, max length 105)
**description**: Description of the app (text)

# Sample Data
The `sample_data.sql` file provides sample data for testing the database. It inserts values into the `api_app` table.
