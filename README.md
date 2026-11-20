# SSH Brute-Force Detector

Ek chhota Python tool jo Linux SSH auth log padhta hai, failed login attempts
ginta hai, aur brute-force attack karne wale IP addresses ko SUSPICIOUS flag karta hai.

## Features

- Har IP ke failed login attempts ginta hai
- Har IP ne kitne alag usernames try kiye, ye dikhata hai
- Pehla aur aakhri attempt ka time dikhata hai
- IPv4 aur IPv6 dono support karta hai
- Kharab ya corrupt lines par crash nahi hota, unhe "skipped" ginta hai
- Result CSV file mein save kar sakta hai

## Requirements

- Python 3.8 ya naya
- Koi extra library install nahi karni padti (sirf Python ki built-in modules)

Check karne ke liye: `python --version`

## Setup

```
git clone https://github.com/siddharthkumar-sec/ssh-bruteforce-detector.git
cd ssh-bruteforce-detector
```

## Usage

```
python analyzer.py [logfile] [-t THRESHOLD] [-o CSV_FILE]
```

| Option | Matlab | Default |
|---|---|---|
| `logfile` | Auth log ka path | `sample_auth.log` |
| `-t`, `--threshold` | Itne ya zyada failures par SUSPICIOUS | 5 |
| `-o`, `--csv` | Report CSV file mein save karo | save nahi hota |

### Examples

```
python analyzer.py
python analyzer.py sample_auth.log -t 3
python analyzer.py sample_auth.log -t 3 -o report.csv
python analyzer.py /var/log/auth.log
```

Asli Linux log ke liye permission chahiye ho sakti hai:

```
sudo python3 analyzer.py /var/log/auth.log
```

## Sample Output

```
File: sample_auth.log | Threshold: 5

IP                                       FAILS USERS  FIRST SEEN       LAST SEEN        STATUS
203.0.113.50                                 7     4  Nov  5 08:14:02  Nov  5 08:22:33  SUSPICIOUS
198.51.100.7                                 3     2  Nov  5 08:16:44  Nov  5 08:16:52  ok
2001:db8::1                                  3     1  Nov  5 08:21:20  Nov  5 08:21:30  ok

Lines padhi: 28 | Failed IPs: 7 | Suspicious: 1 | Skipped (samajh nahi aayi): 2
```

## Supported Log Format

Ye tool Linux `sshd` ki lines samajhta hai, jaise:

```
Nov  5 08:14:02 web01 sshd[2201]: Failed password for root from 203.0.113.50 port 40122 ssh2
Nov  5 08:14:09 web01 sshd[2203]: Failed password for invalid user admin from 203.0.113.50 port 40130 ssh2
```

Ye Windows Event Log, Apache ya Nginx log ke liye nahi hai.
Kuch Linux (RHEL/CentOS) mein log `/var/log/secure` mein hota hai.

## Exit Codes

| Code | Matlab |
|---|---|
| 0 | Koi suspicious IP nahi mila |
| 1 | Kam se kam ek suspicious IP mila |
| 2 | Log file padh nahi payi |

## Project Structure

```
.
├── analyzer.py
├── sample_auth.log
└── README.md
```

## Note

`sample_auth.log` mein sirf test ke liye banaya hua nakli data hai.
Is tool ko sirf apne ya jinki permission ho, un systems ke logs par use karo.

## What I Learned

Python file handling, dictionaries, regex, argparse, aur functions. Security ke
nazariye se brute-force detection aur log analysis.
