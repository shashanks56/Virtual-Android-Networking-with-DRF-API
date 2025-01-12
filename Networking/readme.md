# Basic Networking

## How the Script Works

1. **Retrieve Mock Data from the Virtual Android System:**
   - The script uses the `adb` tool to extract system properties from the running Android emulator.
   - It retrieves the following information:
     - `ro.product.model`: Device model.
     - `ro.build.version.release`: OS version.
   - The retrieved data is formatted into a JSON payload with the fields:
     - `app_name`: Device name.
     - `version`: OS version.
     - `description`: A description containing the device model and OS version.

2. **Establish Connection to Backend:**
   - The script sends the mock data to the backend API (`POST /api/add_app/`) using an HTTP POST request via the `requests` library.
   - The backend URL is defined as `http://127.0.0.1:8000/api/add_app/`.

3. **Log Server Response:**
   - The script logs the server's response to indicate whether the data was successfully received by the backend.
   - If successful, the response includes the created resource details. Errors, if any, are also logged.
