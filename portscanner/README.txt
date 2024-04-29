Multi-threaded Port Scanner

Description
The Multi-threaded Port Scanner is a Python script that allows users to scan ports on a target IP address using multiple threads concurrently. It leverages the concurrent.futures module to distribute port scanning tasks across multiple threads, improving scanning efficiency and speed. The script provides a flexible command-line interface for specifying the target IP address, port range, and number of threads, making it suitable for various network scanning and security analysis tasks.

Features
-Multi-threaded Port Scanning: Utilizes multiple threads to scan ports concurrently, enhancing scanning efficiency.
-Customizable Port Range: Specify the range of ports to scan, from the start port to the end port.
-Flexible Thread Configuration: Control the number of threads used for port scanning to optimize performance.
-Real-time Feedback: Provides real-time feedback on open, closed, and timed-out ports during the scanning process.
-Error Handling: Robust error handling to gracefully handle network errors and exceptions during port scanning.

Usage
1. Clone the repository or download the script file (portscanner.py).
2. Ensure you have Python installed on your system.
3. Run the script using the command line or terminal: python portscanner.py <target> <start_port> <end_port> [--threads <num_threads>]

<target>: Target IP address to scan.
<start_port>: Start port of the port range to scan.
<end_port>: End port of the port range to scan.
--threads <num_threads> (optional): Number of threads to use for scanning (default: 10).

4. The script will start scanning the specified port range on the target IP address using multiple threads.
5. Open, closed, and timed-out ports will be reported in real-time during the scanning process.

Requirements
Python 3.x

Security Considerations
-Use Responsibly: Ensure that you have appropriate permissions before scanning ports on any target IP address.
-Respect Legal and Ethical Boundaries: Use the port scanner for legitimate purposes and adhere to legal and ethical guidelines regarding network scanning activities.

Author
[Philipp Bielinski]