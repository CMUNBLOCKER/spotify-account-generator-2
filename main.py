import threading, requests, ctypes, os, time, random, string
from datetime import datetime
from colorama import Fore, Style

name = "SpotyGen"

os.system("cls"); ctypes.windll.kernel32.SetConsoleTitleW(f"{name}")

lock = threading.Lock()
proxies = []
combos = []
proxy_counter = 0
counter = 0

w = Fore.WHITE
l = Fore.LIGHTBLUE_EX
rs = Style.RESET_ALL

date = datetime.now() 
today = date.today() 
today = str(today).split(".")[0] 
today = today.replace(":","-")

class MAIN:
    def __init__(self):
        self.session = requests.Session()
        self.Errors = 0
        self.Created = 0

    def safeprint(self, arg):
        lock.acquire()
        print(arg)
        lock.release()

    def loadproxies(self): 
        if os.path.exists("proxies.txt"):
            with open ("proxies.txt","r",encoding="UTF-8") as f:
                for line in f.readlines():
                    line = line.replace("\n", "")
                    proxies.append(line)
                if len(proxies) == 0:
                    print(Fore.RED + f"\a\n\t\t{l}[!] {w}Proxies file is empty, please put in proxies.")
                    input(Fore.BLACK + "\t\t" + Fore.BLACK); quit()
        else:
            print(Fore.RED + f"\a\n\t\t{l}[!] {w}Make proxies.txt and put proxies in proxies.txt")
            input(Fore.BLACK + "\t\t" + Fore.BLACK); quit()

    def Threads(self):
        try:
            threads = int(input(f'\n\t\t{w}> {l}Threads: {rs}'))
            os.system('cls')
            self.safeprint(ape)
            return threads
        except ValueError:
            self.Threads()    

    def title(self): 
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name} - Account created: {self.Created} | Errors while creating: {self.Errors}")

    def login(self,proxy,today): 
        self.title()
        try:
            email = ("").join(random.choices(string.ascii_letters + string.digits, k=16)) + "@gmail.com"
            password = ("").join(random.choices(string.ascii_letters + string.digits, k=16))
            username  = ("").join(random.choices(string.ascii_letters + string.digits, k=16))           
            proxiess = { 
            "http": f"http://{proxy}", 
            "https": f"http://{proxy}", 
            "ftp": f"ftp://{proxy}"}
            headers = { 
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
                "Referer": "https://www.spotify.com/",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "*/*"
            }

            url = "https://spclient.wg.spotify.com/signup/public/v1/account"
            data = f"&birth_day=2&birth_month=02&birth_year=1990&collect_personal_info=undefined&creation_flow=&creation_point=https%3A%2F%2Fwww.spotify.com%2Fnl%2F&displayname={username}&gender=male&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&platform=www&referrer=&send-email=1&thirdpartyemail=1&email={email}&password={password}&password_repeat={password}"
        
            r = self.session.post(url,headers=headers,data=data,proxies=proxiess)
            if '{"status":1,' in r.text:
                with open(f"created {today}.txt", "a") as f:
                    f.write(f"{email}:{password}\n")
                    self.Created += 1
            elif '{"status":320,"errors":' in r.text:
                self.Errors += 1
            elif '{"status":0,"errors":{"attempts":}' in r.text:
                self.Errors += 1
            elif '504' in r.text:
                self.Errors += 1
            elif 'The server encountered a temporary error and could not complete your request' in r.text:
                self.Errors += 1
            else:
                self.Errors += 1
                pass
            self.title()
        except Exception as e: 
            self.Errors += 1
            self.title()
            pass

def main():
    global MAIN
    global proxy_counter
    MAIN.loadproxies()
    threads = MAIN.Threads()
    
    def thread_starter():
        MAIN.login(proxies[proxy_counter], today)    

    ctypes.windll.kernel32.SetConsoleTitleW(f"{name} - Starting" ) 
    time.sleep(0.4)                                                           
    ctypes.windll.kernel32.SetConsoleTitleW(f"{name} - Starting." ) 
    time.sleep(0.4)                                                           
    ctypes.windll.kernel32.SetConsoleTitleW(f"{name} - Starting.." ) 
    time.sleep(0.4)                                                           
    ctypes.windll.kernel32.SetConsoleTitleW(f"{name} - Starting..." ) 
    time.sleep(0.4)   

    while True:
        try:
            if threading.active_count() <= threads:
                threading.Thread(target = thread_starter).start()
                proxy_counter += 1
            if len(proxies) <= proxy_counter:
                proxy_counter = 0
        except Exception as e:
            pass

ape = (Fore.LIGHTBLUE_EX + f"""
\t\t███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗
\t\t██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
\t\t███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝ 
\t\t╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝  
\t\t███████║██║     ╚██████╔╝   ██║   ██║██║        ██║   
\t\t╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝ {w}github.com/59n{l} 
                                                      
\t\t\t\t ██████╗ ███████╗███╗   ██╗                           
\t\t\t\t██╔════╝ ██╔════╝████╗  ██║                           
\t\t\t\t██║  ███╗█████╗  ██╔██╗ ██║                           
\t\t\t\t██║   ██║██╔══╝  ██║╚██╗██║                           
\t\t\t\t╚██████╔╝███████╗██║ ╚████║                           
\t\t\t\t ╚═════╝ ╚══════╝╚═╝  ╚═══╝                           
                                                                                                 
""")   

MAIN = MAIN()
print(ape) 
main()