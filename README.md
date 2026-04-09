Python Port Scanner

A lightweight Python-based port scanner that checks for open ports on a target host and identifies common services. This project demonstrates fundamental networking concepts and basic cybersecurity techniques using Python sockets.

Features
Scans a list of common ports (FTP, SSH, HTTP, HTTPS, etc.)
Resolves hostnames to IP addresses
Identifies open vs. closed ports
Performs basic banner grabbing
Saves results to a file (scan_results.txt)
Displays scan duration and summary
🛠️ Technologies Used
Python 3
Built-in libraries:
socket
time
 
How It Works
The user enters a target IP or hostname
The program resolves it into an IP address
It scans predefined ports using TCP connections
If a port is open:
It prints the port and service name
Attempts to grab a banner (if available)
Results are saved to a file

How to Run
1. Clone the repository
git clone https://github.com/joladapo15/python-port-scanner.git
cd python-port-scanner
2. Run the program
python scanner.py
3. Enter a target

Example:

Enter target IP or hostname: scanme.nmap.org
📄 Example Output
Scanning 45.33.32.156...

[OPEN]   Port 80    | HTTP
         └─ Banner: HTTP/1.1 200 OK
[CLOSED] Port 22    | SSH

Scan complete in 2.14 seconds
1 open port(s) found: [80]
Results saved to scan_results.txt


 Author
Joshua Oladapo
Information Technology Student | Aspiring Cybersecurity Professional
