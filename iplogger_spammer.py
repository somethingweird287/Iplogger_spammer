
from stem.control import Controller
import requests
from time import sleep

target_url = "<IpLogger Link Here>"
tor_proxy = "socks5h://127.0.0.1:9050"  # Tor proxy
control_port_password = "password"  # Replace with your ControlPort password
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"

referer = "https://yourmom.com"; #reference url

def get_tor_ip():
    try:
        response = requests.get("http://httpbin.org/ip", proxies={"http": tor_proxy, "https": tor_proxy}, timeout=5)
        return response.json()["origin"]
    except Exception as e:
        print(f"Error getting Tor IP: {e}")
        return None

def change_tor_identity():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=control_port_password)
        controller.signal("NEWNYM")
        print("Tor identity changed!")
        sleep(2)  # Wait for Tor to establish a new circuit

def send_requests():
    while True:
        try:
            headers = {
                "user-agent": agent,
                "referer": referer
            }   
            change_tor_identity()
            ip_before_request = get_tor_ip()
            if ip_before_request:
                print(f"Using IP: {ip_before_request}")
                response = requests.get(target_url, headers=headers, proxies={"http": tor_proxy, "https": tor_proxy}, timeout=5)
                print(f"Status Code: {response.status_code}")
            else:
                print("Failed to retrieve a new IP.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    send_requests()
