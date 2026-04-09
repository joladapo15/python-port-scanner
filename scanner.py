import socket
import time

# Our lookup table of common ports and their services
PORT_NAMES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP",
}

# ── Step 1: Get the target from the user ──────────────────────────────
target = input("Enter target IP or hostname: ")

# Convert hostname to IP (if already an IP, nothing changes)
ip = socket.gethostbyname(target)
print(f"\nScanning {ip}...\n")

# ── Step 2: Start the timer ───────────────────────────────────────────
start_time = time.time()

# ── Step 3: Create a list to track open ports ─────────────────────────
open_ports = []

# ── Main scan loop ────────────────────────────────────────────────────
for port in PORT_NAMES:

    # Create a fresh socket (connection tool) for each port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # wait max 0.5 seconds for a response

    # Knock on the door — returns 0 if open, anything else if closed
    status = s.connect_ex((ip, port))

    if status == 0:
        open_ports.append(port)
        print(f"[OPEN]   Port {port:5} | {PORT_NAMES[port]}")

        # ── Step 4: Try to grab a banner ──────────────────────────────
        try:
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024).decode(errors="ignore").strip()
            if banner:
                print(f"         └─ Banner: {banner[:80]}")
        except:
            pass

        # ── Step 5: Save open ports to a file ─────────────────────────
        with open("scan_results.txt", "a") as f:
            f.write(f"[OPEN] {port} | {PORT_NAMES[port]}\n")

    else:
        print(f"[CLOSED] Port {port:5} | {PORT_NAMES[port]}")

    s.close()  # close the connection before moving to the next port

# ── Final summary ─────────────────────────────────────────────────────
elapsed = round(time.time() - start_time, 2)  # end time minus start time
print(f"\n Scan complete in {elapsed} seconds")
print(f"{len(open_ports)} open port(s) found: {open_ports}")
print(f"Results saved to scan_results.txt")

