# Decoded Security - Hashing Lab

**Password Cracking: See It For Yourself**

A hands-on Docker lab for Decoded Security subscribers. You will crack real password hashes using John the Ripper and understand exactly why algorithm choice and salting matter.

---

## Quick Start

```bash
git clone https://github.com/winkleri-23/DS_hashing_lab.git
cd DS_hashing_lab
docker build -t decoded-hashing-lab .
docker run -it decoded-hashing-lab
```

That's it. The lab environment starts automatically.

---

## What's Inside

| File | Description |
|------|-------------|
| `hashes.txt` | Overview of all targets with context |
| `hashes_md5.txt` | MD5 hashes to crack |
| `hashes_sha1.txt` | SHA-1 hash to crack |
| `hashes_bcrypt.txt` | bcrypt hash (the one that won't crack) |
| `wordlists/decoded_wordlist.txt` | Your attack wordlist |
| `scripts/welcome.sh` | Incident briefing shown on startup |

Type `cat /lab/hints.txt` inside the container for step-by-step guidance.

---

## What You Will Learn

- Why MD5 and SHA-1 are dangerous for password storage
- How dictionary attacks work in practice
- Why bcrypt resists cracking
- What salting does and why it matters

---

## Part of the Article

This lab accompanies the Decoded Security article:  
**Password Cracking Explained: Why Your Password Is Weaker Than You Think**

Read it at [decodedsecurity.com](https://www.decodedsecurity.com)


*Built by [Decoded Security](https://www.decodedsecurity.com) 
