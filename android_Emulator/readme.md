# Virtual Android System Simulation

## Overview
This Python script simulates a virtual Android system capable of running basic tasks. It performs the following actions:
1. Creates a virtual Android environment using the Android Emulator.
2. Launches the emulator and waits for it to boot.
3. Installs a sample APK into the emulator.
4. Retrieves and logs system information, such as OS version, device model, and available memory.

The logged system information is saved in a file named `system_info.log`.


## How to Run the Script:->

### Prerequisites:
1. **Android SDK**: Ensure the Android SDK is installed, and the `emulator` and `adb` tools are configured.
- Emulator path: `C:\Users\Shashank\AppData\Local\Android\Sdk\emulator\emulator`
- ADB path: `C:\Users\Shashank\AppData\Local\Android\Sdk\platform-tools\adb`

2. **Android Virtual Device (AVD)**: An AVD should be pre-configured in your system. Update the `avd_name` in the script with your AVD's name.
   - Example AVD Name: `Medium_Phone_API_34`

3. **Python Environment**:
   - Install Python 3.8+.
   - Install necessary Python packages if required (e.g., `subprocess` is built-in).

### Steps to Run:
1. Place APK file in the designated path. Update the `apk_path` variable in the script with the file's location.
   - Example APK Path: `C:\\Users\\Shashank\\Desktop\\Python\\EMULATOR\\chess.apk`.

2. Run the script using Python:
   ```
   python emulator.py
   ```
   
## How to install an app on the virtual system:
The script uses the adb install command to install an app into the virtual Android system.
Ensure the APK path is correctly specified in the apk_path variable.

## Summary of the System Information Logged:
The Full information is saved in a file named system_info.log , here is Summary:

OS Version: 14
Device Model: sdk_gphone64_x86_64
Memory Info:
MemTotal:        2021520 kB
MemFree:          204360 kB
MemAvailable:     796836 kB