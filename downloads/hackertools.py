import time
import random
import sys
import os
from datetime import datetime

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def progress_bar(text, duration=2, length=50):
    print(f"\n{Colors.CYAN}[*]{Colors.RESET} {text}")
    for i in range(length + 1):
        percent = (i / length) * 100
        filled = '█' * i
        empty = '░' * (length - i)
        sys.stdout.write(f'\r{Colors.GREEN}[{filled}{empty}]{Colors.RESET} {percent:.0f}%')
        sys.stdout.flush()
        time.sleep(duration / length)
    print()

def fake_ip():
    return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

def fake_mac():
    return ':'.join([f'{random.randint(0,255):02x}' for _ in range(6)])

def fake_port():
    return random.randint(1000, 65535)

def banner():
    clear()
    print(f"{Colors.RED}{Colors.BOLD}")
    print("""
    ██╗  ██╗ ██████╗ ██████╗ ██████╗  █████╗ 
    ██║ ██╔╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
    █████╔╝ ██║   ██║██║  ██║██████╔╝███████║
    ██╔═██╗ ██║   ██║██║  ██║██╔══██╗██╔══██║
    ██║  ██╗╚██████╔╝██████╔╝██║  ██║██║  ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
    ╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗  ╔╦╗╔═╗╔═╗╦  ╔═╗
    ╠═╣╠═╣║  ╠╩╗║╣ ╠╦╝   ║ ║ ║║ ║║  ╚═╗
    ╩ ╩╩ ╩╚═╝╩ ╩╚═╝╩╚═   ╩ ╚═╝╚═╝╩═╝╚═╝
    """)
    print(f"{Colors.RESET}{Colors.DIM}    Version 3.7.2 | Build 2024.11.16")
    print(f"    Advanced Penetration Testing Suite{Colors.RESET}\n")
    time.sleep(1)

def main_menu():
    print(f"\n{Colors.GREEN}{'═'*60}")
    print(f"{Colors.BOLD}                    MAIN CONTROL PANEL{Colors.RESET}{Colors.GREEN}")
    print(f"{'═'*60}{Colors.RESET}\n")
    
    menu = [
        ("1", "Network Penetration", "WiFi/LAN Attack Vectors"),
        ("2", "Social Engineering", "Phishing Campaign Manager"),
        ("3", "DDoS Launcher", "Distributed Denial of Service"),
        ("4", "Credential Harvester", "Multi-Protocol Password Recovery"),
        ("5", "Port Scanner", "Advanced Network Reconnaissance"),
        ("6", "Payload Injector", "Remote Access Deployment"),
        ("7", "SQL Injection", "Database Exploitation Module"),
        ("8", "Keylogger Deploy", "Remote Monitoring System"),
        ("9", "Ransomware Sim", "File Encryption Toolkit"),
        ("10", "Trojan Builder", "Custom Malware Generator"),
        ("0", "Exit", "Shutdown System")
    ]
    
    for num, name, desc in menu:
        print(f"{Colors.CYAN}{num:>3}.{Colors.RESET} {Colors.BOLD}{name:<25}{Colors.RESET} {Colors.DIM}| {desc}{Colors.RESET}")
    
    print(f"\n{Colors.YELLOW}{'═'*60}{Colors.RESET}")

def wifi_attack():
    clear()
    type_text(f"{Colors.PURPLE}[*] Initializing WiFi Attack Module...{Colors.RESET}", 0.03)
    progress_bar("Loading wireless drivers", 1.5)
    
    print(f"\n{Colors.GREEN}[+] Adapter detected: wlan0mon{Colors.RESET}")
    print(f"{Colors.GREEN}[+] Chipset: RTL8812AU{Colors.RESET}")
    time.sleep(0.5)
    
    progress_bar("Scanning for networks", 2)
    
    networks = [
        ("TP-Link_5G", fake_mac(), random.randint(-90, -30), "WPA2"),
        ("iPhone_Net", fake_mac(), random.randint(-90, -30), "WPA3"),
        ("Tashkent_WiFi", fake_mac(), random.randint(-90, -30), "WPA2"),
        ("Office_Secure", fake_mac(), random.randint(-90, -30), "WPA2-Enterprise"),
        ("Guest_Network", fake_mac(), random.randint(-90, -30), "WPA"),
        ("HUAWEI-" + str(random.randint(1000,9999)), fake_mac(), random.randint(-90, -30), "WPA2"),
    ]
    
    print(f"\n{Colors.CYAN}{'SSID':<20} {'BSSID':<20} {'Signal':<10} {'Security'}{Colors.RESET}")
    print(f"{Colors.DIM}{'─'*70}{Colors.RESET}")
    
    for ssid, mac, signal, sec in networks:
        print(f"{Colors.WHITE}{ssid:<20}{Colors.RESET} {Colors.DIM}{mac:<20}{Colors.RESET} {Colors.YELLOW}{signal} dBm{Colors.RESET:<10} {Colors.RED}{sec}{Colors.RESET}")
        time.sleep(0.3)
    
    target = random.choice(networks)
    print(f"\n{Colors.GREEN}[+] Target selected: {target[0]}{Colors.RESET}")
    print(f"{Colors.CYAN}[*] BSSID: {target[1]}{Colors.RESET}")
    
    progress_bar("Capturing handshake packets", 3)
    
    for i in range(random.randint(50, 200)):
        print(f"{Colors.DIM}[{datetime.now().strftime('%H:%M:%S')}]{Colors.RESET} Packet {i+1}: {fake_mac()} → {target[1]}")
        time.sleep(0.05)
    
    print(f"\n{Colors.GREEN}[+] Handshake captured successfully!{Colors.RESET}")
    progress_bar("Running dictionary attack", 4)
    
    passwords = ["password123", "admin2024", "qwerty123", "tashkent2024", "wifi12345"]
    for pw in passwords:
        print(f"{Colors.YELLOW}[*] Testing: {pw}{Colors.RESET}")
        time.sleep(0.8)
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}[✓] PASSWORD FOUND: {random.choice(passwords)}{Colors.RESET}")
    time.sleep(2)

def phishing_campaign():
    clear()
    type_text(f"{Colors.PURPLE}[*] Launching Social Engineering Module...{Colors.RESET}", 0.03)
    progress_bar("Loading phishing templates", 1.5)
    
    templates = ["Facebook Login", "Gmail Security Alert", "Bank Verification", "Instagram Recovery", "PayPal Update"]
    
    print(f"\n{Colors.CYAN}Available Templates:{Colors.RESET}")
    for i, temp in enumerate(templates, 1):
        print(f"{Colors.WHITE}{i}. {temp}{Colors.RESET}")
        time.sleep(0.2)
    
    selected = random.choice(templates)
    print(f"\n{Colors.GREEN}[+] Template selected: {selected}{Colors.RESET}")
    
    progress_bar("Cloning target website", 2)
    progress_bar("Configuring email server", 1.5)
    
    print(f"\n{Colors.CYAN}[*] Server started on: http://{fake_ip()}:8080{Colors.RESET}")
    print(f"{Colors.CYAN}[*] Sending phishing emails...{Colors.RESET}\n")
    
    emails = ["user" + str(random.randint(100,999)) + "@gmail.com" for _ in range(15)]
    
    for email in emails:
        status = random.choice(["Sent", "Sent", "Sent", "Failed", "Blocked"])
        color = Colors.GREEN if status == "Sent" else Colors.RED
        print(f"{color}[{status}]{Colors.RESET} {email}")
        time.sleep(0.4)
    
    print(f"\n{Colors.GREEN}[+] Campaign deployed: 12/15 emails delivered{Colors.RESET}")
    
    time.sleep(2)
    print(f"\n{Colors.YELLOW}[*] Monitoring incoming credentials...{Colors.RESET}\n")
    
    for i in range(5):
        victim_ip = fake_ip()
        username = "user" + str(random.randint(100, 999))
        password = "pass" + str(random.randint(1000, 9999))
        print(f"{Colors.GREEN}[NEW] {victim_ip}{Colors.RESET} → {Colors.CYAN}{username}:{password}{Colors.RESET}")
        time.sleep(1.5)
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}[✓] 5 credentials harvested{Colors.RESET}")
    time.sleep(2)

def ddos_attack():
    clear()
    type_text(f"{Colors.PURPLE}[*] Initializing DDoS Attack Vector...{Colors.RESET}", 0.03)
    
    target_ip = fake_ip()
    print(f"\n{Colors.CYAN}[*] Target IP: {target_ip}{Colors.RESET}")
    print(f"{Colors.CYAN}[*] Target Port: {fake_port()}{Colors.RESET}")
    
    progress_bar("Recruiting botnet nodes", 2)
    
    botnet_size = random.randint(500, 2000)
    print(f"\n{Colors.GREEN}[+] Botnet assembled: {botnet_size} nodes online{Colors.RESET}")
    
    countries = ["US", "CN", "RU", "DE", "BR", "IN", "JP", "KR"]
    for _ in range(8):
        country = random.choice(countries)
        nodes = random.randint(50, 300)
        print(f"{Colors.WHITE}[+] {country}: {nodes} nodes ready{Colors.RESET}")
        time.sleep(0.3)
    
    progress_bar("Initiating attack sequence", 2)
    
    print(f"\n{Colors.RED}[!] ATTACK LAUNCHED{Colors.RESET}\n")
    
    for i in range(30):
        packets = random.randint(10000, 50000)
        bandwidth = random.randint(100, 800)
        print(f"{Colors.YELLOW}[{i+1}s]{Colors.RESET} Packets: {Colors.RED}{packets}/s{Colors.RESET} | Bandwidth: {Colors.RED}{bandwidth} Mbps{Colors.RESET}")
        time.sleep(0.5)
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}[✓] Target overwhelmed - Server offline{Colors.RESET}")
    time.sleep(2)

def password_cracker():
    clear()
    type_text(f"{Colors.PURPLE}[*] Starting Credential Harvesting Module...{Colors.RESET}", 0.03)
    
    protocols = ["FTP", "SSH", "SMB", "RDP", "HTTP", "HTTPS"]
    
    print(f"\n{Colors.CYAN}Select Protocol:{Colors.RESET}")
    for i, p in enumerate(protocols, 1):
        print(f"{Colors.WHITE}{i}. {p}{Colors.RESET}")
        time.sleep(0.1)
    
    selected_proto = random.choice(protocols)
    target_ip = fake_ip()
    
    print(f"\n{Colors.GREEN}[+] Protocol: {selected_proto}{Colors.RESET}")
    print(f"{Colors.GREEN}[+] Target: {target_ip}{Colors.RESET}")
    
    progress_bar("Loading wordlist (10M entries)", 2)
    progress_bar("Establishing connection", 1)
    
    print(f"\n{Colors.YELLOW}[*] Brute force attack initiated...{Colors.RESET}\n")
    
    usernames = ["admin", "root", "user", "administrator", "guest"]
    
    for _ in range(50):
        username = random.choice(usernames)
        password = "pass_" + str(random.randint(1000, 9999))
        status = random.choice(["Failed", "Failed", "Failed", "Failed", "Success"])
        
        if status == "Failed":
            print(f"{Colors.RED}[✗]{Colors.RESET} {username}:{password}")
            time.sleep(0.1)
        else:
            print(f"{Colors.GREEN}[✓]{Colors.RESET} {Colors.BOLD}{username}:{password}{Colors.RESET}")
            print(f"\n{Colors.GREEN}{Colors.BOLD}[SUCCESS] Valid credentials found!{Colors.RESET}")
            time.sleep(2)
            return
    
    time.sleep(1)

def port_scanner():
    clear()
    type_text(f"{Colors.PURPLE}[*] Launching Advanced Port Scanner...{Colors.RESET}", 0.03)
    
    target_ip = fake_ip()
    print(f"\n{Colors.CYAN}[*] Target: {target_ip}{Colors.RESET}")
    print(f"{Colors.CYAN}[*] Scan Type: SYN Stealth Scan{Colors.RESET}")
    
    progress_bar("Resolving hostname", 1)
    
    print(f"\n{Colors.GREEN}[+] Host is up (0.052s latency){Colors.RESET}")
    
    progress_bar("Scanning 65535 ports", 3)
    
    open_ports = [
        (21, "FTP", "vsftpd 3.0.3"),
        (22, "SSH", "OpenSSH 8.2p1"),
        (80, "HTTP", "Apache 2.4.41"),
        (443, "HTTPS", "nginx 1.18.0"),
        (3306, "MySQL", "MySQL 5.7.33"),
        (3389, "RDP", "Microsoft Terminal Services"),
        (8080, "HTTP-Proxy", "Squid 4.10"),
    ]
    
    print(f"\n{Colors.CYAN}{'PORT':<10} {'STATE':<10} {'SERVICE':<15} {'VERSION'}{Colors.RESET}")
    print(f"{Colors.DIM}{'─'*60}{Colors.RESET}")
    
    for port, service, version in open_ports:
        print(f"{Colors.WHITE}{port:<10}{Colors.RESET} {Colors.GREEN}{'OPEN':<10}{Colors.RESET} {Colors.YELLOW}{service:<15}{Colors.RESET} {Colors.DIM}{version}{Colors.RESET}")
        time.sleep(0.4)
    
    print(f"\n{Colors.GREEN}[+] Scan complete: {len(open_ports)} open ports found{Colors.RESET}")
    
    progress_bar("Running vulnerability scan", 2.5)
    
    vulns = [
        "CVE-2021-44228 (Log4Shell) - CRITICAL",
        "CVE-2022-22965 (Spring4Shell) - HIGH",
        "CVE-2020-1472 (Zerologon) - CRITICAL"
    ]
    
    print(f"\n{Colors.RED}[!] Vulnerabilities Detected:{Colors.RESET}")
    for vuln in vulns:
        print(f"{Colors.RED}  → {vuln}{Colors.RESET}")
        time.sleep(0.5)
    
    time.sleep(2)

def payload_injector():
    clear()
    type_text(f"{Colors.PURPLE}[*] Loading Payload Injection System...{Colors.RESET}", 0.03)
    
    payloads = ["Reverse Shell", "Meterpreter", "Bind Shell", "Web Shell", "PowerShell Empire"]
    
    print(f"\n{Colors.CYAN}Available Payloads:{Colors.RESET}")
    for i, p in enumerate(payloads, 1):
        print(f"{Colors.WHITE}{i}. {p}{Colors.RESET}")
        time.sleep(0.2)
    
    selected = random.choice(payloads)
    print(f"\n{Colors.GREEN}[+] Selected: {selected}{Colors.RESET}")
    
    progress_bar("Generating payload", 1.5)
    progress_bar("Encoding with Shikata Ga Nai", 1.5)
    progress_bar("Bypassing AV signatures", 2)
    
    target_ip = fake_ip()
    print(f"\n{Colors.CYAN}[*] Target: {target_ip}{Colors.RESET}")
    print(f"{Colors.CYAN}[*] Listener: {fake_ip()}:{fake_port()}{Colors.RESET}")
    
    progress_bar("Deploying payload", 2)
    
    print(f"\n{Colors.YELLOW}[*] Establishing connection...{Colors.RESET}")
    time.sleep(2)
    print(f"{Colors.GREEN}[+] Connection established!{Colors.RESET}")
    time.sleep(1)
    print(f"{Colors.GREEN}[+] Session 1 opened{Colors.RESET}")
    time.sleep(1)
    
    print(f"\n{Colors.CYAN}[*] System Information:{Colors.RESET}")
    print(f"{Colors.WHITE}  OS: Windows 10 Pro (Build 19045){Colors.RESET}")
    print(f"{Colors.WHITE}  User: administrator{Colors.RESET}")
    print(f"{Colors.WHITE}  Privileges: SYSTEM{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}[✓] Remote access established{Colors.RESET}")
    time.sleep(2)

def sql_injection():
    clear()
    type_text(f"{Colors.PURPLE}[*] SQL Injection Module Active...{Colors.RESET}", 0.03)
    
    target_url = f"http://{fake_ip()}/login.php"
    print(f"\n{Colors.CYAN}[*] Target URL: {target_url}{Colors.RESET}")
    
    progress_bar("Testing injection points", 2)
    
    injections = [
        "' OR '1'='1",
        "admin'--",
        "' UNION SELECT NULL--",
        "1' AND 1=1--"
    ]
    
    print(f"\n{Colors.YELLOW}[*] Testing payloads...{Colors.RESET}\n")
    
    for inj in injections:
        print(f"{Colors.DIM}[*] Payload: {inj}{Colors.RESET}")
        time.sleep(0.8)
        print(f"{Colors.RED}[✗] Failed{Colors.RESET}\n")
    
    print(f"{Colors.GREEN}[✓] Vulnerable endpoint found!{Colors.RESET}")
    
    progress_bar("Extracting database structure", 2.5)
    
    tables = ["users", "accounts", "orders", "products", "admin_logs"]
    
    print(f"\n{Colors.CYAN}[*] Database Tables:{Colors.RESET}")
    for table in tables:
        print(f"{Colors.WHITE}  → {table}{Colors.RESET}")
        time.sleep(0.3)
    
    progress_bar("Dumping user credentials", 3)
    
    print(f"\n{Colors.GREEN}[+] Extracted Records:{Colors.RESET}\n")
    for i in range(8):
        username = "user" + str(random.randint(100, 999))
        email = username + "@example.com"
        password_hash = ''.join([random.choice('0123456789abcdef') for _ in range(32)])
        print(f"{Colors.WHITE}{username:<15} {email:<25} {Colors.DIM}{password_hash}{Colors.RESET}")
        time.sleep(0.5)
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}[✓] Database compromised{Colors.RESET}")
    time.sleep(2)

def keylogger_deploy():
    clear()
    type_text(f"{Colors.PURPLE}[*] Deploying Keylogger System...{Colors.RESET}", 0.03)
    
    target_ip = fake_ip()
    print(f"\n{Colors.CYAN}[*] Target: {target_ip}{Colors.RESET}")
    
    progress_bar("Compiling keylogger binary", 1.5)
    progress_bar("Obfuscating code", 1.5)
    progress_bar("Uploading to target", 2)
    
    print(f"\n{Colors.GREEN}[+] Keylogger installed successfully{Colors.RESET}")
    print(f"{Colors.GREEN}[+] Persistence established{Colors.RESET}")
    
    time.sleep(1)
    print(f"\n{Colors.YELLOW}[*] Monitoring keystrokes...{Colors.RESET}\n")
    
    keys_logged = [
        "gmail.com - username: john.doe@gmail.com",
        "gmail.com - password: MyP@ssw0rd123",
        "facebook.com - login attempt",
        "online-bank.com - PIN: 4529",
        "Search: how to secure my computer",
        "Document: quarterly_report_2024.docx"
    ]
    
    for log in keys_logged:
        timestamp = datetime.now().strftime('%H:%M:%S')
        print(f"{Colors.DIM}[{timestamp}]{Colors.RESET} {Colors.WHITE}{log}{Colors.RESET}")
        time.sleep(1.5)
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}[✓] Surveillance active{Colors.RESET}")
    time.sleep(2)

def ransomware_sim():
    clear()
    type_text(f"{Colors.PURPLE}[*] Ransomware Deployment System...{Colors.RESET}", 0.03)
    
    target_ip = fake_ip()
    print(f"\n{Colors.CYAN}[*] Target: {target_ip}{Colors.RESET}")
    
    progress_bar("Generating encryption keys", 1.5)
    
    print(f"\n{Colors.GREEN}[+] RSA-4096 key pair generated{Colors.RESET}")
    print(f"{Colors.GREEN}[+] AES-256 encryption ready{Colors.RESET}")
    
    progress_bar("Scanning file system", 2)
    
    file_types = [".doc", ".pdf", ".jpg", ".xlsx", ".ppt", ".txt", ".mp4", ".zip"]
    total_files = random.randint(5000, 15000)
    
    print(f"\n{Colors.YELLOW}[*] Found {total_files} files{Colors.RESET}")
    
    progress_bar("Encrypting files", 4)
    
    print(f"\n{Colors.RED}[!] Encryption Progress:{Colors.RESET}\n")
    
    for ftype in file_types:
        count = random.randint(200, 2000)
        print(f"{Colors.RED}[✓]{Colors.RESET} {count} {ftype} files encrypted")
        time.sleep(0.5)
    
    print(f"\n{Colors.RED}{Colors.BOLD}[!] ALL FILES ENCRYPTED{Colors.RESET}")
    
    progress_bar("Deploying ransom note", 1)
    
    bitcoin_address = "1" + ''.join([random.choice('0123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz') for _ in range(33)])
    
    print(f"\n{Colors.RED}{'═'*60}")
    print(f"{Colors.BOLD}  YOUR FILES HAVE BEEN ENCRYPTED{Colors.RESET}")
    print(f"{Colors.RED}{'═'*60}{Colors.RESET}")
    print(f"\n{Colors.WHITE}  Payment: 0.5 BTC{Colors.RESET}")
    print(f"{Colors.YELLOW}  Address: {bitcoin_address}{Colors.RESET}")
    print(f"{Colors.WHITE}  Deadline: 72 hours{Colors.RESET}\n")
    
    time.sleep(3)

def trojan_builder():
    clear()
    type_text(f"{Colors.PURPLE}[*] Custom Trojan Builder v2.8...{Colors.RESET}", 0.03)
    
    print(f"\n{Colors.CYAN}[*] Configuration Menu:{Colors.RESET}\n")
    
    options = [
        "Persistence: Enabled",
        "Anti-VM: Enabled",
        "Anti-Debug: Enabled",
        "Keylogger: Enabled",
        "Screen Capture: Enabled",
        "Webcam Access: Enabled",
        "Microphone Access: Enabled",
        "File Exfiltration: Enabled"
    ]
    
    for opt in options:
        print(f"{Colors.WHITE}  [✓] {opt}{Colors.RESET}")
        time.sleep(0.3)
    
    progress_bar("\nCompiling trojan", 2)
    progress_bar("Packing with UPX", 1)
    progress_bar("Code signing", 1.5)
    progress_bar("Icon injection", 1)
    
    filename = f"system_update_{random.randint(1000,9999)}.exe"
    print(f"\n{Colors.GREEN}[+] Trojan compiled: {filename}{Colors.RESET}")
    print(f"{Colors.GREEN}[+] Size: {random.randint(500,1500)} KB{Colors.RESET}")
    print(f"{Colors.GREEN}[+] Detection rate: 0/70 AV engines{Colors.RESET}")
    
    progress_bar("\nTesting payload", 2)
    
    print(f"\n{Colors.GREEN}[+] All systems operational{Colors.RESET}")
    print(f"{Colors.GREEN}[+] C2 Server: {fake_ip()}:443{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}[✓] Trojan ready for deployment{Colors.RESET}")
    time.sleep(2)

def main():
    banner()
    
    while True:
        main_menu()
        
        try:
            choice = input(f"\n{Colors.BOLD}kodra@tools{Colors.RESET}:{Colors.BLUE}~${Colors.RESET} ")
            
            if choice == "1":
                wifi_attack()
            elif choice == "2":
                phishing_campaign()
            elif choice == "3":
                ddos_attack()
            elif choice == "4":
                password_cracker()
            elif choice == "5":
                port_scanner()
            elif choice == "6":
                payload_injector()
            elif choice == "7":
                sql_injection()
            elif choice == "8":
                keylogger_deploy()
            elif choice == "9":
                ransomware_sim()
            elif choice == "10":
                trojan_builder()
            elif choice == "0":
                print(f"\n{Colors.RED}[*] Shutting down...{Colors.RESET}")
                time.sleep(1)
                clear()
                break
            else:
                print(f"{Colors.RED}[!] Invalid option{Colors.RESET}")
                time.sleep(1)
            
            input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.RED}[*] Operation cancelled{Colors.RESET}")
            time.sleep(1)
            break
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
            time.sleep(2)

if __name__ == "__main__":
    main()