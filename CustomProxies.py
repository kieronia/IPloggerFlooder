import random
import requests
from proxyscrape import create_collector
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
import threading
import time
import os 
os.system("Color 02")

os.system("title -ip logger spammer-")

ua = UserAgent()
collector = create_collector('my-collector', 'https')
executor = ThreadPoolExecutor(max_workers=1000)




def send_request(site,proxy):
    headers = {'user-agent': ua.random}
    try:
        e = requests.get(site, proxies={"http":proxy,"https":proxy}, headers=headers, timeout=15)
        print(e.status_code)
    except Exception:
        pass

link = input("Link?")


def my_function():
    lines = open('proxies.txt').read().splitlines()
    randomproxy =random.choice(lines)
    executor.submit(send_request, link, randomproxy)
    print(f"[+] Spam sent to {link} from {randomproxy} ")
    os.system(f"title -ip logger spammer- sending to {link} from {randomproxy}")
while True:
    threading.Thread(target = my_function).start()
    time.sleep(0.01)#like adding a delay -  makes it smoother




