import subprocess
import time

def start_emulator(avd_name, emulator_path):
    """Launch the Android Emulator using a specific AVD."""
    print("Starting Android Emulator...")
    emulator_cmd = f"{emulator_path} -avd {avd_name}"
    try:
        subprocess.Popen(emulator_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Emulator launched. Waiting for it to boot...")
    except Exception as e:
        print(f"Error starting emulator: {e}")

def wait_for_emulator(adb_path):
    """Wait for the emulator to boot."""
    print("Waiting for emulator to boot...")
    try:
        subprocess.run([adb_path, "wait-for-device"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Emulator is ready!")
    except Exception as e:
        print(f"Error waiting for emulator: {e}")


def install_app(adb_path, apk_path):
    """Install an APK using adb."""
    print(f"Installing APK: {apk_path}")
    result = subprocess.run([adb_path, "install", apk_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if "Success" in result.stdout:
        print("APK installed successfully!")
    else:
        print("Failed to install APK:", result.stderr)


def get_system_info(adb_path):
    """Retrieve and log specific system information from the emulator."""
    print("Retrieving system information...")

    # Run 'adb shell getprop' to get all system properties
    result = subprocess.run([adb_path, "shell", "getprop"], stdout=subprocess.PIPE, text=True)
    all_properties = result.stdout

    # Extract specific properties
    os_version = extract_property(all_properties, "ro.build.version.release")  # OS version
    device_model = extract_property(all_properties, "ro.product.model")  # Device model

    # Get available memory using a separate ADB command
    mem_info_result = subprocess.run([adb_path, "shell", "cat", "/proc/meminfo"], stdout=subprocess.PIPE, text=True)
    mem_info = mem_info_result.stdout

    # Log the extracted information
    with open("system_info.log", "w") as log_file:
        log_file.write(f"OS Version: {os_version}\n")
        log_file.write(f"Device Model: {device_model}\n")
        log_file.write("Memory Info:\n")
        log_file.write(mem_info)

    print("System information saved in 'system_info.log'.")

def extract_property(all_properties, property_name):
    """Helper function to extract a specific property from system information."""
    for line in all_properties.splitlines():
        if property_name in line:
            return line.split(":")[1].strip().strip("[]")
    return "Unknown"


avd_name = "Medium_Phone_API_34"
emulator_path = "C:\\Users\\Shashank\\AppData\\Local\\Android\\Sdk\\emulator\\emulator"
adb_path = "C:\\Users\\Shashank\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb"
apk_path = "C:\\Users\\Shashank\\Desktop\\DRF_android_net\\android_Emulator\\chess.apk"


start_emulator(avd_name, emulator_path)
time.sleep(30)
wait_for_emulator(adb_path)
install_app(adb_path, apk_path)
get_system_info(adb_path)