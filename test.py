from proxy import Proxy

p = Proxy()

def main():
    print("Valid proxies for this session; \n")
    for prx in p.validproxy:
        print(p)
        print("\n")

if __name__ == '__main__':
    main()
