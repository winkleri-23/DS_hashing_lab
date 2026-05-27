#!/usr/bin/env python3
"""
Decoded Security - Dictionary Attack Demo
Shows exactly how an attacker cracks unsalted MD5/SHA-1 hashes.
"""

import hashlib
import sys
import time

RESET  = "\033[0m"
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"

def crack(hash_file, wordlist, algorithm):
    algorithm = algorithm.lower()

    try:
        with open(hash_file) as f:
            targets = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{RED}Hash file not found: {hash_file}{RESET}")
        sys.exit(1)

    try:
        with open(wordlist) as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{RED}Wordlist not found: {wordlist}{RESET}")
        sys.exit(1)

    print(f"\n{BOLD}{CYAN}============================================{RESET}")
    print(f"{BOLD}{CYAN}  DECODED SECURITY - DICTIONARY ATTACK DEMO {RESET}")
    print(f"{BOLD}{CYAN}============================================{RESET}")
    print(f"\n  Algorithm : {YELLOW}{algorithm.upper()}{RESET}")
    print(f"  Targets   : {YELLOW}{len(targets)} hash(es){RESET}")
    print(f"  Wordlist  : {YELLOW}{len(words)} passwords{RESET}")
    print(f"\n{BOLD}  Starting attack...{RESET}\n")

    cracked = {}
    start = time.time()
    attempts = 0

    for word in words:
        if algorithm == "md5":
            digest = hashlib.md5(word.encode()).hexdigest()
        elif algorithm in ("sha1", "sha-1"):
            digest = hashlib.sha1(word.encode()).hexdigest()
        elif algorithm == "sha256":
            digest = hashlib.sha256(word.encode()).hexdigest()
        else:
            print(f"{RED}Unsupported algorithm: {algorithm}{RESET}")
            sys.exit(1)

        attempts += 1

        for target in targets:
            if digest == target and target not in cracked:
                elapsed = time.time() - start
                cracked[target] = word
                print(f"  {GREEN}[CRACKED]{RESET}  {target[:16]}...  =>  {BOLD}{GREEN}{word}{RESET}  ({elapsed:.4f}s, attempt #{attempts})")

        if len(cracked) == len(targets):
            break

    elapsed = time.time() - start

    print(f"\n{BOLD}  Results{RESET}")
    print(f"  {'─'*44}")
    print(f"  Cracked   : {GREEN}{len(cracked)}{RESET} / {len(targets)}")
    print(f"  Attempts  : {attempts}")
    print(f"  Time      : {elapsed:.4f}s")

    not_cracked = [t for t in targets if t not in cracked]
    if not_cracked:
        print(f"\n  {YELLOW}Not cracked (not in wordlist):{RESET}")
        for h in not_cracked:
            print(f"    {h}")

    print(f"\n{BOLD}{CYAN}============================================{RESET}\n")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"\nUsage: python3 crack.py <hash_file> <wordlist> <algorithm>")
        print(f"       python3 crack.py /lab/hashes_md5.txt /lab/wordlists/decoded_wordlist.txt md5")
        print(f"       python3 crack.py /lab/hashes_sha1.txt /lab/wordlists/decoded_wordlist.txt sha1\n")
        sys.exit(1)

    crack(sys.argv[1], sys.argv[2], sys.argv[3])
