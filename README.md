# 🌐 IP Address Finder

A modern and intuitive desktop application to find and manage your public and local IP addresses, with advanced geolocation features and system integration.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Key Features

### 🔍 **Advanced IP Detection**
- **Public IP**: Automatically detects your public IP address using multiple services for reliability
- **Local IP**: Instantly displays your local IP address on your home/corporate network
- **Multi-Service Backup**: Fallback system using different providers (ipify.org, httpbin.org, myip.com)

### 🌍 **Smart Geolocation**
- **Geographic Information**: Get complete details about your public IP location
- **ISP Data**: View information about your internet service provider
- **GPS Coordinates**: Precise latitude and longitude coordinates
- **Timezone**: Time zone associated with your location

### 🖥️ **Modern Interface**
- **Dark Theme Design**: Elegant interface with modern dark theme
- **Responsive UI**: Optimized layout for better user experience
- **Hover Animations**: Interactive effects on buttons and elements
- **Semantic Color Coding**: Distinctive colors for success, error, and information

### 📋 **Clipboard Management**
- **Quick Copy**: Instantly copy IP addresses to clipboard
- **Visual Feedback**: Immediate confirmation of copy operations
- **Cross-platform Compatibility**: Clipboard support for all operating systems

## 🚀 Installation and Launch

### Method 1: Automatic Launch (Recommended)
```bash
# Windows
start.bat

# Linux/macOS
python start.py
```

### Method 2: Manual Installation
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch the application
python main.py
```

## 📁 Project Structure

```
ip-address-finder/
├── 📄 main.py              # Main application with GUI
├── 🚀 start.py             # Automatic startup script
├── 💾 start.bat            # Windows launcher
├── 📋 requirements.txt     # Python dependencies
├── 📖 README.md            # Project documentation
└── 🖼️ ico/                 # Icons directory (optional)
    └── app_icon.ico        # Application icon
```

## 🔧 File Descriptions

### `main.py` - 🎯 **Core Application**
The heart of the application containing:

- **`AdvancedIPFinder`**: Main class managing the entire user interface
- **GUI Components**: Graphical interface built with Tkinter
- **IP Detection**: Logic for detecting public and local IPs
- **Network Services**: Integration with web services for IP and geolocation
- **Clipboard Management**: Clipboard copy functionality
- **Threading**: Asynchronous operations to prevent UI blocking

**Technical Features:**
- 🎨 **Design System**: Consistent and modern color scheme
- 🔄 **Multi-threading**: Non-blocking network requests
- 🛡️ **Error Handling**: Robust network error management
- 📱 **Responsive Layout**: Adaptive and centered interface

### `start.py` - ⚡ **Smart Launcher**
Intelligent startup system including:

- **Dependency Checker**: Automatic Python dependency verification
- **Auto-installer**: Automatic installation of missing packages
- **Environment Validation**: Execution environment checks
- **Colored Output**: Colored output for better user experience
- **Error Recovery**: Intelligent installation error handling

**Features:**
- ✅ **Auto-setup**: Automatically configures the environment
- 🔍 **Smart Detection**: Detects Python and required libraries
- 🎨 **Colored CLI**: Colored command line interface
- ⏱️ **Timeout Handling**: Installation timeout management

### `start.bat` - 🏁 **Windows Quick Launcher**
Simplified launcher for Windows users:
- Double-click launch
- Custom window title
- Final pause to view any errors

### `requirements.txt` - 📦 **Dependencies**
List of essential dependencies:
- **`requests`**: For HTTP calls to IP detection services
- **`pyperclip`**: For advanced cross-platform clipboard management

## 🎮 How to Use

### 1️⃣ **Get Public IP**
1. Click the **"🔍 Get Public IP"** button
2. Wait for loading (progress indicator)
3. View the result with additional options

### 2️⃣ **View Local IP**
- Local IP is automatically displayed on startup
- Use the **"📋 Copy"** button to copy it

### 3️⃣ **Explore Geographic Information**
1. After getting the public IP, click **"🌍 Geo Info"**
2. View complete details about:
   - 🌍 Country and city
   - 📍 Region and coordinates
   - 🌐 Internet provider (ISP)
   - 🕐 Time zone

### 4️⃣ **Copy to Clipboard**
- Use **"📋 Copy"** buttons to quickly copy IPs
- Get immediate operation confirmation

## 🛠️ System Requirements

### **Software Requirements**
- **Python**: 3.7 or higher
- **Operating System**: Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+)
- **Internet Connection**: Required for public IP detection

### **Hardware Requirements**
- **RAM**: Minimum 512 MB available
- **Storage**: 50 MB free space
- **Display**: Minimum resolution 800x600

## 🔒 Privacy and Security

### **Data Protection**
- ✅ **No Data Storage**: No data is saved locally
- ✅ **No Tracking**: No behavior or preferences tracking
- ✅ **HTTPS Only**: All communications use secure protocols
- ✅ **Local Processing**: Completely local data processing

### **External Services Used**
The following external services are used exclusively for IP detection:
- 🔗 **ipify.org**: Primary service for public IP
- 🔗 **httpbin.org**: Backup service
- 🔗 **myip.com**: Alternative service
- 🔗 **ip-api.com**: For geolocation information

## 🐛 Troubleshooting

### **Common Issues and Solutions**

#### ❌ **"Error retrieving public IP"**
**Possible causes:**
- No internet connection or unstable connection
- Firewall blocking HTTP requests
- IP detection services temporarily unavailable

**Solutions:**
1. Check internet connection
2. Try again after a few seconds
3. Check firewall settings

#### ❌ **"Local IP not available"**
**Possible causes:**
- Network configuration issues
- Network interfaces disabled

**Solutions:**
1. Restart the application
2. Check active network connections
3. Restart network adapter if necessary

#### ❌ **"Unable to get geolocation information"**
**Possible causes:**
- Invalid public IP
- Geolocation service unavailable
- Corporate network restrictions

**Solutions:**
1. Verify you have a valid public IP
2. Try again after a few minutes
3. Contact network administrator if in corporate environment

## 📈 Roadmap and Future Development

### **Version 2.0 - Planned**
- 🌐 **Multi-language Support**: Support for multiple languages
- 📊 **Network Monitoring**: Continuous connection monitoring
- 🕐 **History Tracking**: History of detected IPs
- 🔄 **Auto-refresh**: Periodic automatic updates
- 📱 **Mobile Version**: Mobile device version

### **Version 2.5 - Under Evaluation**
- 🛡️ **VPN Detection**: VPN/Proxy connection detection
- 🌍 **Extended Geo Info**: Extended geographic information
- 📧 **Export Features**: Data export in various formats
- 🎨 **Theme Customization**: Theme and color customization

## 👨‍💻 Developer Information

**Developed by**: EventExecutor  
**Year**: 2025  
**Current Version**: 1.0  

### **Contact and Support**
For bug reports, feature requests, or general support, please open an issue in the project repository.

---

## 📜 License

This project is distributed under the MIT License. See the `LICENSE` file for complete details.

---

<div align="center">

**🌟 If this project was useful to you, consider leaving a star! 🌟**

**Made with ❤️ and Python**

</div>
