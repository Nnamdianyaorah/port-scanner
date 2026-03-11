"""
Professional Port Scanner v3.0
A complete network port scanning tool with service detention and reporting
Author: Nnamdi Victor Anyaorah
Date: 2025-11-06
"""

import socket
import threading
from datetime import datetime
import json
import sys
import time

class PortScanner:
    """ Professional Port Scanner Class"""

    def __init__(self, target, start_port, end_port):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.open_ports = []
        self.lock = threading.Lock()
        self.scan_start_time = None
        self.scan_end_time = None

    def get_service_name(self, port):
        """Get service name for a port"""
        try:
            service = socket.getservbyport(port)
            return service
        except:
            return "unknown"
        
    def check_port(self, port):
        """Check if a single port is open"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            result = sock.connect_ex((self.target, port))

            if result == 0:
                service = self.get_service_name(port)

                # Thread-safe update
                with self.lock:
                    self.open_ports.append({
                        "port": port,
                        "service": service,
                        "status": "open"
                    })
                    print(f"[+] Port {port:5d} - OPEN ✅ - Service: {service:20s}")

            sock.close()

        except socket.error:
            pass
        except KeyboardInterrupt:
            print("\n\n[!] Scan interrupted by user")
            sys.exit(0)

    def display_banner(self):
        """Display scanner banner"""
        banner = """
╔══════════════════════════════════════════════════════════════════════╗
║                    PROFESSIONAL PORT SCANNER v3.0                    ║
║                         Network Security Tool                        ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        print(banner)

    def display_scan_info(self):
        """Display scan information"""
        print("\n" + "="*70)
        print("SCAN CONFIGURATION")
        print("="*70)
        print(f"Target Host      : {self.target}")
        print(f"Port Range       : {self.start_port}-{self.end_port}")
        print(f"Total Ports      : {self.end_port - self.start_port + 1}")
        print(f"Scan Started     : {self.scan_start_time}")
        print(f"Max Threads      : 100")
        print("="*70)
        print("\nScanning in progress...\n")

    def scan(self):
        """Execute the port scan"""
        self.scan_start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.display_banner()
        self.display_scan_info()

        threads = []

        try:
            # Create and start threads
            for port in range(self.start_port, self.end_port + 1):
                thread = threading.Thread(target=self.check_port, args=(port,))
                threads.append(thread)
                thread.start()

                # Limit concurrent threads to 100
                if len(threads) >= 100:
                    for t in threads:
                        t.join()
                    threads = []

            # Wait for the remaining threads
            for thread in threads:
                thread.join()

        except KeyboardInterrupt:
            print("\n\n[!] Scan interrupted by user")
            sys.exit(0)

        self.scan_end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Sort result by port number
        self.open_ports.sort(key=lambda x: x['port'])

    def display_results(self):
        """Display scan results"""
        print("\n"+ "="*70)
        print("SCAN RESULTS")
        print("="*70)

        if self.open_ports:
            print(f"\n✅ Found {len(self.open_ports)} open port(s):\n")

            print(f"{'PORT':<10} {'SERVICE':<20} {'STATUS':<10}")
            print("-" * 70)

            for item in self.open_ports:
                print(f"{item['port']:<10} {item['service']:<20} {item['status']:<10}")
        else:
            print("\n❌ No open ports found in the specific range")

        print("\n" + "="*70)
        print(f"Scan Started  : {self.scan_start_time}")
        print(f"Scan Finished  : {self.scan_end_time}")
        print("="*70)

    def generate_report(self):
        """Generate JSON report"""
        report = {
            "scan_metadata": {
                "tool": "Professional Port Scanner v3.0",
                "target": self.target,
                "port_range": {
                    "start": self.start_port,
                    "end": self.end_port,
                    "total": self.end_port - self.start_port + 1
                },
                "scan_time": {
                    "started": self.scan_start_time,
                    "finished": self.scan_end_time
                },
                "results_summary": {
                    "total_open_ports": len(self.open_ports),
                    "ports_scanned": self.end_port - self.start_port + 1
                }
            },
            "open_ports": self.open_ports
        }

        return report
    
    def save_results(self, filename=None):
        """Save scan results to file"""
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            safe_target = self.target.replace('.', '_').replace(':', '_')
            filename = f"scan_{safe_target}_{timestamp}.json"

        try:
            report = self.generate_report()

            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)

            print(f"\n✅ Results saved to: {filename}")
            return True
        
        except Exception as e:
            print(f"\n❌ Error saving results: {e}")
            return False
        
    def display_recommendations(self):
        """Display security recommendations"""
        if not self.open_ports:
            return
        
        print("\n" + "="*70)
        print("SECURITY RECOMMENDATIONS")
        print("="*70)

        dangerous_ports = {
            21: "FTP - Consider using SFTP instead",
            23: "Telnet - Use SSH instead (port 22)",
            25: "SMTP - Ensure proper authentication",
            3389: "RDP - Ensure strong passwords and VPN",
            3306: "MySQL - Should not be exposed to internet",
            5432: "PostgreSQL - Should not be exposed to internet",
            6379: "Redis - Should not be exposed to internet",
            27017: "MonogDB - Should not be exposed to internet"
        }

        found_issues = False

        for port_info in self.open_ports:
            port = port_info['port']
            if port in dangerous_ports:
                if not found_issues:
                    print("\n⚠️ Potentially risky ports detected:\n")
                    found_issues = True

                print(f"Port - {dangerous_ports[port]}  {port:5d} ({port_info['service']})")

        if not found_issues:
            print("\n✅ No obviously dangerous port detected")
            print("However, ensure all open ports are intentional and properly secured")
        print("\n" + "="*70)

def get_valid_input(prompt, input_type=str, min_val=None, max_val=None):
    """Get and validate your input"""
    while True:
        try:
            value = input_type(input(prompt))

            if min_val is not None and value < min_val:
                print(f"❌ Value must be at least {min_val}")
                continue

            if max_val is not None and value > max_val:
                print(f"❌ Value must be at most {max_val}")
                continue

            return value
        
        except ValueError:
            print(f"❌ Invalid input. Please enter a valid {input_type.__name__}")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)

def main():
    """Main program"""
    print("\n" + "="*70)
    print(" "*20 + "PORT SCANNER SETUP")
    print("="*70)

    # Get scan parameters
    print("\n[?] Enter scan parameters:\n")

    target = get_valid_input("Target host (e.g., scanme.nmap.org): ", str)
    start_port = get_valid_input("Start port (1-65535): ", int, 1, 65535)
    end_port = get_valid_input("End port (1-65535): ", int, start_port, 65535)

    # Confirm scan
    print("\n" + "="*70)
    print("SCAN CONFIRMATION")
    print("="*70)
    print(f"Target      : {target}")
    print(f"Port Range  : {start_port}-{end_port}")
    print(f"Total Ports : {end_port - start_port + 1}")
    print("="*70)

    confirm = input("\nProceed with scan? (yes/no): ").lower()

    if confirm not in ['yes', 'y']:
        print("\n[!] Scan cancelled")
        return
    
    # Create scanner and run scan
    scanner = PortScanner(target, start_port, end_port)

    try:
        scanner.scan()
        scanner.display_results()
        scanner.display_recommendations()

        # Ask to svae results
        save = input("\nSave results to file? (yes,no): ").lower()
        if save in ['yes', 'y']:
            scanner.save_results()

        # Ask to perform another scan
        again = input("\nPerform another scan? (yes/no): ").lower()
        if again in ['yes', 'y']:
            print("\n" + "="*70 + "\n")
            main()

    except KeyboardInterrupt:
        print("\n\n[!] Scan interrupted by user")
        sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExisting...")
        sys.exit(0)