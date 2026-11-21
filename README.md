 <div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=venom&height=260&color=0:080D19,45:102B50,100:5427A8&text=SSH%20BRUTE-FORCE%20DETECTOR&fontColor=FFFFFF&fontSize=34&fontAlignY=42&desc=LINUX%20SECURITY%20%7C%20PYTHON%20%7C%20LOG%20ANALYSIS&descSize=13&descAlignY=62&animation=fadeIn" />

### DETECT. ANALYZE. DEFEND.

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=16&duration=2600&pause=900&color=38BDF8&center=true&vCenter=true&width=700&lines=Analyzing+Linux+SSH+Authentication+Logs;Tracking+Failed+Login+Attempts;Identifying+Suspicious+IP+Addresses;Built+With+Python+%7C+Defensive+Security" />

<br/>

<img src="https://img.shields.io/badge/PYTHON-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/PLATFORM-LINUX-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
<img src="https://img.shields.io/badge/DOMAIN-CYBERSECURITY-8B5CF6?style=for-the-badge&logo=hackthebox&logoColor=white" />
<img src="https://img.shields.io/badge/VERSION-1.0-0EA5E9?style=for-the-badge" />

<br/><br/>

**[OVERVIEW](#01--project-overview) · [FEATURES](#02--core-capabilities) · [INSTALLATION](#05--installation) · [USAGE](#06--usage) · [DEMO](#08--sample-output)**

</div>

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=38BDF8&center=true&vCenter=true&width=700&lines=01+%E2%80%94+PROJECT+OVERVIEW;Understanding+SSH+Login+Activity" />

</div>

## About The Project

**SSH Brute-Force Detector** is a lightweight Python-based defensive security tool that analyzes Linux SSH authentication logs, counts failed login attempts, and identifies potentially suspicious IP addresses.

It examines authentication events, tracks attempted usernames, records the first and last observed attempts, and flags IP addresses that reach a configurable failure threshold.

The objective is to simplify basic SSH security log analysis through Python automation.

```yaml
project:
  name: SSH Brute-Force Detector
  version: 1.0
  language: Python
  platform: Linux
  category: Defensive Security
  input: SSH Authentication Logs
  output: Terminal Report / CSV Report
  status: Initial Release
```

> A practical Python project exploring the fundamentals of security monitoring and authentication log analysis.

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=A78BFA&center=true&vCenter=true&width=700&lines=02+%E2%80%94+CORE+CAPABILITIES;What+The+Detector+Can+Do" />

</div>

## Features

<table>
<tr>
<td width="50%">

### 🔍 Failed Login Detection

Counts failed SSH authentication attempts for each IP address.

</td>
<td width="50%">

### 🌐 IP Address Tracking

Supports IPv4 and IPv6 addresses.

</td>
</tr>
<tr>
<td width="50%">

### 👤 Username Analysis

Tracks the number of distinct usernames attempted from each IP.

</td>
<td width="50%">

### ⏱️ Timestamp Analysis

Records first and last observed login attempts.

</td>
</tr>
<tr>
<td width="50%">

### 🚨 Suspicious IP Detection

Flags IP addresses that meet or exceed the configured threshold.

</td>
<td width="50%">

### 📄 Log Validation

Skips malformed or unsupported log entries without crashing.

</td>
</tr>
<tr>
<td colspan="2">

### 📊 CSV Report Generation

Exports analysis results into a CSV file for further examination.

</td>
</tr>
</table>

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=818CF8&center=true&vCenter=true&width=700&lines=03+%E2%80%94+DETECTION+WORKFLOW;From+Raw+Logs+To+Security+Insights" />

</div>

## How It Works

The detector follows a straightforward log analysis pipeline.

```text
┌─────────────────────────────┐
│   LINUX SSH AUTH LOG FILE   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       READ LOG ENTRIES      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      PARSE SSH EVENTS       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   IDENTIFY FAILED LOGINS    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    GROUP ATTEMPTS BY IP     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    CHECK FAILURE THRESHOLD  │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      GENERATE REPORT        │
└──────────────┬──────────────┘
               │
          ┌────┴────┐
          ▼         ▼
     TERMINAL     CSV FILE
```

### Detection Logic

An IP address is marked `SUSPICIOUS` when its total failed login attempts are greater than or equal to the configured threshold.

For example:

```python
if failed_attempts >= threshold:
    status = "SUSPICIOUS"
else:
    status = "ok"
```

*Illustrative explanation of the detection rule.*

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=C084FC&center=true&vCenter=true&width=700&lines=04+%E2%80%94+TECHNOLOGY+STACK;Tools+Behind+The+Project" />

</div>

## Built With

<div align="center">

**PROGRAMMING LANGUAGE**

<img src="https://skillicons.dev/icons?i=python&theme=dark" />

<br/>

**PLATFORM**

<img src="https://skillicons.dev/icons?i=linux&theme=dark" />

</div>

### Python Standard Library

| Module | Purpose |
|:--|:--|
| `re` | Regular expression-based log parsing |
| `argparse` | Command-line argument handling |
| `ipaddress` | IP address validation |
| `csv` | CSV report generation |
| `collections` | Data organization, where used |
| File Handling | Reading authentication logs |

**Dependencies:** No third-party Python packages are required. The project uses Python's built-in standard library.

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=38BDF8&center=true&vCenter=true&width=700&lines=05+%E2%80%94+INSTALLATION;Get+The+Detector+Running" />

</div>

## Prerequisites

Before running the project, make sure you have:

- Python 3.8 or newer
- Git
- A Linux SSH authentication log or the included sample log

Check your Python version:

```bash
python --version
```

### Clone The Repository

```bash
git clone https://github.com/siddharthkumar-sec/ssh-bruteforce-detector.git
```

Navigate into the project directory:

```bash
cd ssh-bruteforce-detector
```

No additional package installation is necessary.

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=A78BFA&center=true&vCenter=true&width=700&lines=06+%E2%80%94+USAGE;Execute+The+Detection+Engine" />

</div>

## Command Syntax

```bash
python analyzer.py [logfile] [-t THRESHOLD] [-o CSV_FILE]
```

### Command-Line Arguments

| Argument | Description | Default |
|:--|:--|:--|
| `logfile` | Path to the authentication log | `sample_auth.log` |
| `-t`, `--threshold` | Minimum failed attempts to flag an IP | `5` |
| `-o`, `--csv` | Export results to a CSV file | Disabled |

### Execution Examples

**01 — Analyze the default sample log**

```bash
python analyzer.py
```

**02 — Set a custom detection threshold**

```bash
python analyzer.py sample_auth.log -t 3
```

**03 — Generate a CSV report**

```bash
python analyzer.py sample_auth.log -t 3 -o report.csv
```

**04 — Analyze a real Linux authentication log**

```bash
python analyzer.py /var/log/auth.log
```

Some Linux distributions use `/var/log/secure` instead.

For protected system logs, appropriate read permissions may be required:

```bash
sudo python3 analyzer.py /var/log/auth.log
```

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=818CF8&center=true&vCenter=true&width=700&lines=07+%E2%80%94+SUPPORTED+LOGS;Know+Your+Input+Format" />

</div>

## Supported Log Format

The detector is designed for Linux OpenSSH authentication log entries.

### Example Entries

```text
Nov  5 08:14:02 web01 sshd[2201]: Failed password for root from 203.0.113.50 port 40122 ssh2

Nov  5 08:14:09 web01 sshd[2203]: Failed password for invalid user admin from 203.0.113.50 port 40130 ssh2
```

### Compatibility

| Log Source | Support |
|:--|:--:|
| Linux OpenSSH authentication logs | ✅ |
| IPv4 addresses | ✅ |
| IPv6 addresses | ✅ |
| Windows Event Logs | ❌ |
| Apache access logs | ❌ |
| Nginx access logs | ❌ |

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=C084FC&center=true&vCenter=true&width=700&lines=08+%E2%80%94+SAMPLE+OUTPUT;Detection+In+Action" />

</div>

## Terminal Demonstration

The following is an illustrative output using the included sample dataset.

```text
File: sample_auth.log | Threshold: 5

IP                  FAILS  USERS  FIRST SEEN       LAST SEEN        STATUS
203.0.113.50             7      4  Nov  5 08:14:02  Nov  5 08:22:33  SUSPICIOUS
198.51.100.7             3      2  Nov  5 08:16:44  Nov  5 08:16:52  ok
2001:db8::1              3      1  Nov  5 08:21:20  Nov  5 08:21:30  ok

Lines read: 28 | Failed IPs: 7 | Suspicious: 1 | Skipped: 2
```

### Understanding The Results

| Field | Meaning |
|:--|:--|
| IP | Source IP address |
| FAILS | Total failed login attempts |
| USERS | Distinct usernames attempted |
| FIRST SEEN | First observed attempt |
| LAST SEEN | Last observed attempt |
| STATUS | Detection result |

<details>
<summary><b>What does SUSPICIOUS mean?</b></summary>

An IP address receives the `SUSPICIOUS` status when its failed login count reaches or exceeds the configured threshold.

This is a detection indicator for further investigation, not proof that an account was compromised or that an attack was successful.

</details>

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=38BDF8&center=true&vCenter=true&width=700&lines=09+%E2%80%94+EXIT+CODES;Understanding+Program+Results" />

</div>

## Exit Codes

| Code | Meaning |
|:--:|:--|
| `0` | No suspicious IP detected |
| `1` | At least one suspicious IP detected |
| `2` | Unable to read the log file |

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=A78BFA&center=true&vCenter=true&width=700&lines=10+%E2%80%94+PROJECT+STRUCTURE;Inside+The+Repository" />

</div>

## Repository Structure

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

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=818CF8&center=true&vCenter=true&width=700&lines=11+%E2%80%94+LEARNING+OUTCOMES;Knowledge+Applied+Through+Building" />

</div>

## What I Learned

Building this project helped me apply Python fundamentals to a practical defensive cybersecurity use case.

### Python Development

- File handling and text processing
- Dictionaries and data structures
- Regular expressions
- Functions and modular programming
- Command-line argument parsing
- CSV file generation
- Exception handling

### Cybersecurity Concepts

- SSH authentication logs
- Brute-force attack patterns
- Failed login analysis
- IP address tracking
- Basic security event monitoring

**The biggest takeaway:** Understanding programming concepts becomes more meaningful when they are applied to real-world technical problems.

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=C084FC&center=true&vCenter=true&width=700&lines=12+%E2%80%94+DEVELOPMENT+ROADMAP;One+Version+At+A+Time" />

</div>

## Version History

<details open>
<summary><b>V1.0 — Initial Release</b></summary>

- Linux SSH authentication log analysis
- Failed login attempt counting
- IPv4 and IPv6 support
- Username tracking
- First and last attempt timestamps
- Configurable suspicious IP threshold
- CSV report export

</details>

### Future Development

This repository currently represents V1.0.

Future versions will introduce improvements incrementally as development progresses.

| Version | Status |
|:--|:--|
| V1.0 | Initial release |
| V1.x | Future incremental improvements |
| V2.0+ | Future major development |

*Planned improvements are not implemented features of the current release.*

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=38BDF8&center=true&vCenter=true&width=700&lines=13+%E2%80%94+DISCLAIMER;Responsible+Security+Development" />

</div>

## Responsible Use

This project is developed for educational purposes, defensive security monitoring, and authorized authentication log analysis.

- Analyze only systems you own or have explicit permission to monitor.
- A suspicious IP flag is an indicator for further investigation, not proof of a successful attack.
- The included `sample_auth.log` contains synthetic test data.
- This tool does not automatically block IP addresses or prevent attacks.

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=1000&color=A78BFA&center=true&vCenter=true&width=700&lines=14+%E2%80%94+PROJECT+CREDITS;Built+Through+Learning+And+Experimentation" />

<br/>

### DEVELOPED BY

# SIDDHARTH KUMAR

**Python Developer in Progress | Cybersecurity Learner**

<br/>

<a href="https://github.com/siddharthkumar-sec">
<img src="https://img.shields.io/badge/GITHUB-161B22?style=for-the-badge&logo=github&logoColor=white" />
</a>

<a href="https://github.com/siddharthkumar-sec/ssh-bruteforce-detector">
<img src="https://img.shields.io/badge/PROJECT_REPOSITORY-5427A8?style=for-the-badge&logo=github&logoColor=white" />
</a>

<br/><br/>

**UNDERSTAND THE SYSTEM. ANALYZE THE SIGNAL. BUILD THE SOLUTION.**

<br/>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:5427A8,50:142B4D,100:080D19&height=130&section=footer" />

</div>
