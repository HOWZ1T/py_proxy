from bs4 import BeautifulSoup
import requests
import sys


class Proxy:
    def __init__(self):
        self.index = 0
        self.proxies = self.fetch_proxies()
        self.proxy_count = len(self.proxies)
        self.proxy = self.format_proxy(self.proxies[self.index])

    def cycle(self):
        self.index = (self.index+1) % self.proxy_count
        self.proxy = self.format_proxy(self.proxies[self.index])

    @staticmethod
    def fetch_proxies():
        print("fetching proxies...")
        url = "https://free-proxy-list.net/"
        page = requests.get(url)

        if page.status_code != 200:
            print("Couldn't fetch proxies list! received bad response with code: " + str(page.status_code))
            sys.exit(1)
        else:
            print("parsing data...")
            soup = BeautifulSoup(page.content, "html.parser")
            rows = soup.find_all("tr")

            proxies = []
            for row in rows:
                parts = row.find_all("td")
                if len(parts) == 8:
                    ip = parts[0].text
                    port = parts[1].text
                    country_code = parts[2].text
                    country = parts[3].text
                    provider = parts[4].text
                    google = parts[5].text
                    https = parts[6].text
                    last_checked = parts[7].text

                    if https == "yes":
                        proxies.append([ip, port, country_code, country, provider, google, https, last_checked])

            print("retrieved " + str(len(proxies)) + " proxies")
            return proxies

    @staticmethod
    def format_proxy(proxy):
        http = "http://" + proxy[0] + ":" + proxy[1]
        https = "https://" + proxy[0] + ":" + proxy[1]
        proxy_dict = {
            "http": http,
            "https": https
        }

        return proxy_dict

    @staticmethod
    def test_proxy(proxy_):
        url = "https://www.iplocation.net/find-ip-address"
        print("testing proxy...")
        try:
            page = requests.get(url, proxies=proxy_)
            soup = BeautifulSoup(page.content, "html.parser")

            ip_tbl = soup.find("table", {"class": "iptable"})
            data = ip_tbl.find_all("td")

            ip = data[0].find("span").text
            location = data[1].text.split("[")[0]
            device = data[3].text
            os = data[4].text
            browser = data[5].text
            user_agent = data[6].text

            print("\n\nSuccess! Able to connect with proxy\nConnection Details:\nip: " + ip + "\nlocation: " + location)
            print("device: " + device + "\nos: " + os + "\nbrowser: " + browser + "\nuser agent: " + user_agent)
            return 1
        except requests.exceptions.ProxyError:
            print("request caused a proxy error!")
            return 0
