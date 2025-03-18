# WMI Data Extraction PyQT5 App

## Description
This app is designed to extract and display detailed system information using Windows Management Instrumentation (WMI) and WMIC commands. The tool gathers hardware specifications presents them in a clean, interactive interface.

This information could be used in various software to alter/hijack core computer function & encrypt/steal/delete sensitive data.


> **Disclaimer:**  
> Unauthorized use of this tool is illegal and unethical. Use it only on systems you own or for which you have explicit permission. I am not responsible for any misuse of this software.



## Key Features
- **System Information Display:**  
  Retrieves data such as OS, username, CPU details, motherboard model, memory, and graphics card information via WMI.
- **Disk Information:**  
  Uses WMIC commands to extract disk drive identifiers and sizes.
- **Interactive GUI:**  
  Provides a specifications page and a settings page (with a “Stay On Top” toggle) using a stacked layout.
- **Customizable Settings:**  
  Stores configuration in a JSON file (`config.json`) to manage features like window behavior.
- **Creator Information:**  
  Includes an "About the Creator" link that directs users to your GitHub profile.

## Installation

### Requirements
- **Operating System:** Windows
- **Python:** 3.x
- **Libraries:**  
  - PyQt5  
  - wmi

### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/wmi-data-extraction-gui.git
   cd wmi-data-extraction-gui
