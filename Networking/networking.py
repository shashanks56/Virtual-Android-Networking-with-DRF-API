import requests
import subprocess

adb_path = r"C:\Users\Shashank\AppData\Local\Android\Sdk\platform-tools\adb"

def retrieve_mock_data():
    """Retrieve dynamic data from the emulator."""
    print("Retrieving data from the emulator...")
    result = subprocess.run([adb_path, "shell", "getprop"], stdout=subprocess.PIPE, text=True)
    
    # Extract specific properties dynamically
    all_properties = result.stdout
    device_name = extract_property(all_properties, "ro.product.model")
    os_version = extract_property(all_properties, "ro.build.version.release")

    device_data = {
        "app_name": f"Device_{device_name}",
        "version": os_version,
        "description": f"Model: {device_name}, OS: {os_version}"
    }
    print("Mock Data Retrieved:", device_data)
    return device_data

def extract_property(all_properties, property_name):
    """Helper function to extract specific property values."""
    for line in all_properties.splitlines():
        if property_name in line:
            return line.split(":")[1].strip().strip("[]")
    return "Unknown"

def send_data_to_backend(data):
    """Send the retrieved mock data to the backend API."""
    backend_url = "http://127.0.0.1:8000/api/add_app/"
    print(f"Sending data to backend at {backend_url}...")
    try:
        response = requests.post(backend_url, json=data)
        if response.status_code in [200, 201]:
            print("Response from server:", response.json())
            print("Data sent successfully!")
        else:
            print(f"Failed to send data. HTTP {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    # Retrieve data from the emulator
    device_data = retrieve_mock_data()

    # Send the retrieved data to the backend
    send_data_to_backend(device_data)
