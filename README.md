 <div align="center">

# 🛡️ SSH BRUTE-FORCE DETECTOR

### `LINUX SECURITY TOOL · PYTHON · LOG ANALYSIS`

**Detect. Analyze. Monitor.**

A lightweight Python-based defensive security tool that analyzes Linux SSH authentication logs, identifies repeated failed login attempts, and flags potentially suspicious IP addresses.

<br>

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux-black?style=for-the-badge&logo=linux&logoColor=white)
![Security](https://img.shields.io/badge/Domain-Cybersecurity-red?style=for-the-badge&logo=shield&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.0-blueviolet?style=for-the-badge)

<br>

**[ FEATURES ](#-features) · [ INSTALLATION ](#-installation) · [ USAGE ](#-usage) · [ DEMO ](#-sample-output)**

</div>

---

## `01` — PROJECT OVERVIEW

SSH Brute-Force Detector is a command-line security tool designed to analyze Linux SSH authentication logs and identify IP addresses generating repeated failed login attempts.

It processes authentication events, groups failed attempts by IP address, tracks attempted usernames, and flags IPs that reach a configurable detection threshold.

The goal is simple: make basic SSH log analysis easier through Python automation.

> **Project Status:** V1.0 — Initial Release

---

## `02` — FEATURES

| Feature | Description |
|:--|:--|
| 🔍 Failed Login Detection | Counts failed SSH authentication attempts per IP |
| 🌐 IP Tracking | Supports both IPv4 and IPv6 addresses |
| 👤 Username Analysis | Tracks the number of distinct usernames attempted |
| ⏱️ Timestamp Tracking | Records first and last observed attempts |
| 🚨 Suspicious IP Detection | Flags IPs based on a configurable threshold |
| 📄 Log Validation | Skips malformed or unsupported log entries |
| 📊 CSV Export | Saves analysis results to a CSV report |

---

## `03` — HOW IT WORKS

```text
       LINUX SSH AUTH LOG
                |
                v
       +------------------+
       |   Read Log File  |
       +------------------+
                |
                v
       +------------------+
       |   Parse Entries  |
       +------------------+
                |
                v
       +------------------+
       | Detect Failed    |
       | Login Attempts   |
       +------------------+
                |
                v
       +------------------+
       | Group Data by IP |
       +------------------+
                |
                v
       +------------------+
       | Check Threshold  |
       +------------------+
                |
                v
       +------------------+
       | Generate Report  |
       +------------------+
                |
          +-----+-----+
          |           |
          v           v
      Terminal     CSV Export
```

**Detection Logic:** An IP address is marked `SUSPICIOUS` when its failed login count meets or exceeds the configured threshold.

---

## `04` — TECH STACK

| Technology | Purpose |
|:--|:--|
| Python 3.8+ | Core programming language |
| Regular Expressions (`re`) | SSH log parsing |
| `argparse` | Command-line argument handling |
| `ipaddress` | IP address validation |
| `csv` | Report generation |
| File Handling | Reading authentication logs |

**Dependencies:** No external Python packages required. Uses Python's built-in standard library.

---

## `05` — INSTALLATION

### Prerequisites

- Python 3.8 or newer
- Git
- Linux SSH authentication logs (or the included sample log)

Check your Python installation:

```bash
python --version
```

### Clone the Repository

```bash
git clone https://github.com/siddharthkumar-sec/ssh-bruteforce-detector.git
```

```bash
cd ssh-bruteforce-detector
```

---

## `06` — USAGE

### Command Syntax

```bash
python analyzer.py [logfile] [-t THRESHOLD] [-o CSV_FILE]
```

### Available Arguments

| Argument | Description | Default |
|:--|:--|:--|
| `logfile` | Path to the authentication log | `sample_auth.log` |
| `-t`, `--threshold` | Minimum failed attempts to flag an IP | `5` |
| `-o`, `--csv` | Export results to a CSV file | Disabled |

### Examples

**1. Analyze the default sample log**

```bash
python analyzer.py
```

**2. Set a custom detection threshold**

```bash
python analyzer.py sample_auth.log -t 3
```

**3. Export results to CSV**

```bash
python analyzer.py sample_auth.log -t 3 -o report.csv
```

**4. Analyze a Linux authentication log**

```bash
python analyzer.py /var/log/auth.log
```

Some Linux distributions may store authentication logs at `/var/log/secure` instead.

For protected system logs, appropriate read permissions may be required:

```bash
sudo python3 analyzer.py /var/log/auth.log
```

---

## `07` — SAMPLE OUTPUT

```text
File: sample_auth.log | Threshold: 5

IP                  FAILS  USERS  FIRST SEEN       LAST SEEN        STATUS
203.0.113.50             7      4  Nov  5 08:14:02  Nov  5 08:22:33  SUSPICIOUS
198.51.100.7             3      2  Nov  5 08:16:44  Nov  5 08:16:52  ok
2001:db8::1              3      1  Nov  5 08:21:20  Nov  5 08:21:30  ok

Lines read: 28 | Failed IPs: 7 | Suspicious: 1 | Skipped: 2
```

*Illustrative output from the included sample dataset.*

---

## `08` — SUPPORTED LOG FORMAT

The detector is designed for Linux OpenSSH authentication log entries.

Example:

```text
Nov  5 08:14:02 web01 sshd[2201]: Failed password for root from 203.0.113.50 port 40122 ssh2

Nov  5 08:14:09 web01 sshd[2203]: Failed password for invalid user admin from 203.0.113.50 port 40130 ssh2
```

**Supported:**
- Linux OpenSSH authentication logs.
- Failed password entries.
- IPv4 and IPv6 addresses.

**Not supported:**
- Windows Event Logs.
- Apache access logs.
- Nginx access logs.

---

## `09` — EXIT CODES

| Exit Code | Meaning |
|:--:|:--|
| `0` | No suspicious IP detected |
| `1` | At least one suspicious IP detected |
| `2` | Unable to read the log file |

---

## `10` — PROJECT STRUCTURE

```text
ssh-bruteforce-detector/
│
├── analyzer.py
│
├── sample_auth.log
│
└── README.md
```

---

## `11` — WHAT I LEARNED

Building this project helped me apply Python fundamentals to a practical cybersecurity use case.

**Python Development**
- File handling and text processing.
- Dictionaries and data structures.
- Regular expressions.
- Functions and modular programming.
- Command-line argument parsing.
- CSV file generation.
- Exception handling.

**Cybersecurity Concepts**
- SSH authentication logs.
- Brute-force attack patterns.
- Failed login analysis.
- IP address tracking.
- Basic security event monitoring.

---

## `12` — DEVELOPMENT ROADMAP

This repository represents the initial V1.0 release.

Future versions will focus on gradually improving the tool's functionality, reliability, and capabilities.

| Release | Development |
|:--|:--|
| V1.0 | Initial SSH log analysis and suspicious IP detection |
| V1.x | Planned incremental improvements |
| V2.0+ | Future feature development |

*Future features are not part of the current V1.0 release.*

---

## `13` — DISCLAIMER

This tool is intended for defensive security monitoring, educational purposes, and authorized log analysis.

- Use it only on systems you own or have permission to monitor.
- A suspicious IP flag is an indicator for further investigation, not proof of a successful attack.
- The included `sample_auth.log` contains synthetic test data, not real attack records.
- This tool does not automatically block IP addresses or prevent attacks.

---

<div align="center">

### BUILT WITH PYTHON. INSPIRED BY CYBERSECURITY.

**Siddharth Kumar**

*Learning · Building · Securing*

[GitHub Profile](https://github.com/siddharthkumar-sec) · [Project Repository](https://github.com/siddharthkumar-sec/ssh-bruteforce-detector)

<br>

`END OF V1.0`

</div>
