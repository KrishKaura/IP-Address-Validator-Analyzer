# IP Address Validator-Analyzer

## 📌 Overview
This Python project validates and analyzes IPv4 and IPv6 addresses from a text file.  
It classifies IPs, separates valid/invalid entries, and generates network information.

---

## ⚙️ Features
- IPv4 and IPv6 validation
- Reads IPs from input file (`list_ips.txt`)
- Separates valid and invalid IPs
- Generates network details: for ipv4
  - Network address
  - Broadcast address
  - Subnet mask
  - Usable hosts
- IP classification:
  - Private
  - Public
  - Loopback
  - Multicast
  - Reserved

---

## 🚀 Version Updates

### v1.0
- IPv4 address validation and analysis
- Network details (subnet, broadcast, hosts)
- IP classification system

### v2.0 (Planned)
- IPv6 support (IP version 6)
- Extended validation for mixed IP datasets
- Improved classification and reporting

  
## 📂 Input Format
Each line in `list_ips.txt` should contain one IP address.  
The input file name can be customized in the source code.

