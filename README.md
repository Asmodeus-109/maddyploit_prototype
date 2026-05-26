# Maddyploit

A modular Python-based penetration testing and network reconnaissance framework inspired by the architecture of the Metasploit Framework.

## Features

- Modular framework design
- Interactive command-line interface
- Port scanning module
- DNS lookup module
- Dynamic module loading
- Easy to expand with custom modules

---

## Project Structure

```text
maddyploit/
│
├── core/
│   ├── console.py
│   ├── loader.py
│   └── banner.py
│
├── modules/
│   ├── scanners/
│   │   └── portscan.py
│   │
│   └── info/
│       └── dnslookup.py
│
├── main.py
├── README.md
└── .gitignore
Installation

git clone https://github.com/yourusername/maddyploit.git
cd maddyploit

Run the framework:

python main.py
Usage

Start the framework:

python main.py

Example commands:

maddyploit > use scanners/portscan
maddyploit > set target 127.0.0.1
maddyploit > run

DNS Lookup Example:

maddyploit > use info/dnslookup
maddyploit > set domain google.com
maddyploit > run
Current Modules
Scanners
Port Scanner
Information Gathering
DNS Lookup
Goals
Build a fully modular exploitation framework
Learn cybersecurity tool architecture
Practice Python networking and socket programming
Simulate Metasploit-style workflow
Technologies Used
Python 3
Socket Programming
CLI Design
Modular Architecture
Disclaimer

This project is created for educational and ethical testing purposes only.
Do not use this framework against systems without permission.

Future Improvements
Better command parser
Multi-threaded scanning
Service detection
Plugin system
Colored terminal UI
Session handling
Reverse shell simulation


Author
Created by Maddy
