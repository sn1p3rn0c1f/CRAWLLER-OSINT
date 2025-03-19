from modules.social_scan import check_username
from modules.email_check import check_email_leaks
from modules.whois_lookup import get_whois_info
from modules.name_scraper import search_name
from modules.search_engine import search_name
import subprocess
import os

title = "//CRAWLLER OSINT//"
os.system(f"title {title}")

subprocess.run ('color C', shell=True)
subprocess.run ('cls', shell=True)

menu = """
              ______       ________        ____  __
________________<  /_________|__  /_______ __  |/ /
__  ___/_  __ \_  /___  __ \__/_ <__  ___/ __    / 
_(__  )_  / / /  / __  /_/ /___/ /_  /     _    |  
/____/ /_/ /_//_/  _  .___//____/ /_/      /_/|_|  
                   /_/                             
       _______      _____________                  
_________  __ \_______<  /__  __/                  
__  __ \  / / /  ___/_  /__  /_                    
_  / / / /_/ // /__ _  / _  __/                    
/_/ /_/\____/ \___/ /_/  /_/                       
"""
print(menu)

def main():
    print("=== OSINT CRAWLER ===\n")
    
    username = input("Enter username to scan: ")
    social = check_username(username)
    print("\n[+] Social Scan Results:")
    for platform, link in social.items():
        if link:
            print(f"{platform}: Found -> {link}")
        else:
            print(f"{platform}: Not Found")

    email = input("\nEnter email to check leaks: ")
    api_key = input("Enter HaveIBeenPwned API Key: ")
    leaks = check_email_leaks(email, api_key)
    print("\n[+] Email Leak Results:")
    print(leaks if leaks else "No leaks found!")
    
    domain = input("\nEnter domain to check WHOIS: ")
    whois_info = get_whois_info(domain)
    print("\n[+] Whois Info:")
    print(whois_info)

first = input("\nEnter First Name: ")
last = input("Enter Last Name: ")

name_results = search_name(first, last)
print("\n[+] Name Search Results:")
for engine, links in name_results.items():
    print(f"\n{engine}:")
    for link in links[:10]: 
        print(f"- {link}")

first_name = input("\nEnter First Name: ")
last_name = input("Enter Last Name: ")

print("\n[+] Performing Name Search...")
results = search_name(first_name, last_name)

for engine, links in results.items():
    print(f"\n--- {engine} Results ---")
    for link in links[:10]:  
        print(f"- {link}")

if __name__ == "__main__":
    main()
