# 🔒 Professional Port Scanner

A Python-based network security tool for identifying open ports and services on target systems. Built with multi-threading for fast scanning and includes automated security recommendations.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Security Recommendations](#security-recommendations)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [Author](#author)

## ✨ Features

- **Fast Scanning**: Multi-threaded architecture scans 1000 ports in ~15 seconds
- **Service Detection**: Automatically identifies services running on open ports
- **Security Analysis**: Provides recommendations for potentially dangerous ports
- **Professional Reports**: Generates comprehensive JSON reports with metadata
- **User-Friendly**: Input validation and clear error messages
- **Keyboard Interrupt Handling**: Graceful exit on Ctrl+C

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- No external dependencies (uses only Python standard library)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Nnamdianyaorah/port-scanner.git
cd port-scanner
```

2. No additional installation needed! All required modules are part of Python's standard library.

## 💻 Usage

### Basic Usage
```bash
python port_scanner.py
```

### Interactive Mode

The scanner will prompt you for:
1. **Target host** (e.g., scanme.nmap.org)
2. **Start port** (1-65535)
3. **End port** (1-65535)
4. **Confirmation** before scanning
5. **Save option** for results

### Example Session
```
======================================================================
                       PORT SCANNER SETUP
======================================================================

[?] Enter scan parameters:

Target host (e.g., scanme.nmap.org): scanme.nmap.org
Start port (1-65535): 1
End port (1-65535): 1000

======================================================================
SCAN CONFIRMATION
======================================================================
Target      : scanme.nmap.org
Port Range  : 1-1000
Total Ports : 1000
======================================================================

Proceed with scan? (yes/no): yes
```

## 📊 Examples

### Scanning Common Ports

**Scan standard service ports (1-1024):**
```
Target: scanme.nmap.org
Start port: 1
End port: 1024
```

**Expected output:**
```
[+] Port    22 - OPEN ✅ - Service: ssh
[+] Port    80 - OPEN ✅ - Service: http
```

### Scanning Specific Services

**Check if web services are running:**
```
Target: example.com
Start port: 80
End port: 443
```

### Full Range Scan

**Comprehensive security audit:**
```
Target: your-server.com
Start port: 1
End port: 65535
```
⚠️ **Note**: Full scans take longer (~15-20 minutes)

## 🛡️ Security Recommendations

The scanner automatically detects and warns about potentially risky open ports:

| Port | Service | Risk | Recommendation |
|------|---------|------|----------------|
| 21 | FTP | High | Use SFTP instead |
| 23 | Telnet | Critical | Use SSH (port 22) |
| 3306 | MySQL | High | Should not be exposed to internet |
| 3389 | RDP | High | Ensure strong passwords and VPN |
| 27017 | MongoDB | High | Should not be exposed to internet |

## 🔧 Technical Details

### Architecture

- **Language**: Python 3.8+
- **Threading**: Up to 100 concurrent threads
- **Timeout**: 1 second per port
- **Socket Type**: TCP (SOCK_STREAM)

### Output Format

**Console Output:**
- Real-time progress display
- Color-coded status indicators
- Formatted tables for results

**JSON Report Structure:**
```json
{
  "scan_metadata": {
    "tool": "Professional Port Scanner v3.0",
    "target": "scanme.nmap.org",
    "port_range": {
      "start": 1,
      "end": 1000,
      "total": 1000
    },
    "scan_time": {
      "started": "2026-03-06 15:30:00",
      "finished": "2026-03-06 15:30:15"
    },
    "results_summary": {
      "total_open_ports": 2,
      "ports_scanned": 1000
    }
  },
  "open_ports": [
    {
      "port": 22,
      "service": "ssh",
      "status": "open"
    }
  ]
}
```

## ⚖️ Legal Disclaimer

**IMPORTANT**: This tool is for educational and authorized security testing only.

✅ **Legal Uses:**
- Scanning your own systems
- Authorized penetration testing
- Security audits with permission
- Using test servers like `scanme.nmap.org`

❌ **Illegal Uses:**
- Scanning systems without permission
- Unauthorized network reconnaissance
- Any malicious activity

**Always obtain written permission before scanning networks you do not own.**

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Future Enhancements

- [ ] Banner grabbing for service version detection
- [ ] OS fingerprinting
- [ ] UDP port scanning
- [ ] Export to CSV/PDF formats
- [ ] GUI interface
- [ ] Scheduled scanning

## 👨‍💻 Author

**Nnamdi Victor Anyaorah**

- MSc CyberSecurity - University of Chester
- GitHub: [@Nnamdianyaorah](https://github.com/Nnamdianyaorah)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/nnamdi-anyaorah-345724126)
- Email: Nnamdianyaorah@gmail.com

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built as part of cybersecurity portfolio development
- Inspired by industry-standard tools like Nmap
- Created for educational purposes

---

**⭐ If you found this tool useful, please give it a star!**
