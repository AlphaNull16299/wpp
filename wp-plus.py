import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
import requests
import threading
import gzip
import shutil
os.system('cls' if os.name == 'nt' else 'clear')
f = open(__file__,'r',encoding='UTF-8')
p = f.read()
f.close()
update = requests.get("https://midokuriserver.com/warp/get.php").text
if update == "yes":
    choice = input("アップデートがあります、受信しますか?[y/n]: ")
    if choice == "y":
        print("バックアップ中...")
        shutil.copyfile(__file__,__file__+".backup")
        print("完了\n書き込み中...")
        f = open(__file__, 'w',encoding='UTF-8')
        f.write(update)
        f.close()
        print("完了")
        os._exit(0)
print("準備中だよ")
#referrer = input("[#] Enter the WARP+ ID:")
referrer = "93026e0e-1769-40dd-85e9-1c63c594ff3a"
global proxytype
proxytype = {}
global proxy_list
proxy_list = []

def get_proxies():
    global proxy_list
#    proxytype = {}
    temp_proxy_list = requests.get("https://api.good-proxies.ru/get.php?type%5Bhttp%5D=on&count=&ping=50000&time=600&works=100000&key=3269305ce8094af10e5933fe67db8529",timeout=500).text+"\n"
    temp_proxy_list = temp_proxy_list + requests.get("https://www.proxy-list.download/api/v1/get?type=http",timeout=500).text+"\n"
    temp_proxy_list = temp_proxy_list + requests.get("https://www.proxyscan.io/download?type=http",timeout=500).text+"\n"
    temp_proxy_list = temp_proxy_list + requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",timeout=500).text+"\n"
    temp_proxy_list = temp_proxy_list + requests.get("https://www.secproxy.org/getProxies?key=5ba922a5365e39d8d0c68b7111a11c66&type=https&service=all",timeout=500).text+"\n"
    for i in range(10):temp_proxy_list = temp_proxy_list.replace("\n\n","\n")
    proxy_list = temp_proxy_list.split("\n")
#    proxy_list = requests.get("https://midokuriserver.com/proxytool/",timeout=500).text.split("\n")
    print('\nProxy updated!')

def get_proxies_async():
    global proxy_list
    while True:
        proxytype = {}
        proxy_list = requests.get("https://api.good-proxies.ru/get.php?type%5Bhttp%5D=on&count=&ping=50000&time=600&works=100000&key=3269305ce8094af10e5933fe67db8529",timeout=500).text.split("\n")
        print('Proxy updated!')
        time.sleep(60)

def checking(tproxy):
    global proxytype,proxy_list
    proxy = tproxy.strip().split(":")
    if len(proxy) != 2:
        proxy_list.remove(tproxy)
        return
    err = 0
    num = 0
    while True:
        if err == 3:
            proxy_list.remove(tproxy)
            break
        try:
            num += 1
            s = socks.socksocket()
            if num == 1:
                s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
                ptype = "4"
                proxytype[proxy[0]+":"+proxy[1]] = 4
            if num == 2:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
                ptype = "5"
                proxytype[proxy[0]+":"+proxy[1]] = 5
            if num == 3:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
                ptype = "1"
                proxytype[proxy[0]+":"+proxy[1]] = 1
            s.settimeout(1)
#            s.connect((str(target), int(port)))
#            print(str(target))
            s.connect((str("172.104.90.60"), int(25565)))
#            if protocol == "https":
#                ctx = ssl.SSLContext()
#                s = ctx.wrap_socket(s, server_hostname=target)
#            s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
#            print("\r生存を確認しました: "+str(ptype)+" - "+tproxy,end="")
            s.close()
            break
        except:
            err += 1

def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)            
def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(stringLength)))    
    except Exception as error:
        print(error)    
def run(proxy):
    global proxytype
    try:
        install_id = genString(22)
        body = {"key": "{}=".format(genString(43)),
                "install_id": install_id,
                "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
                "referrer": referrer,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "+09:00",
                "type": "Android",
                "locale": "ja_JP"}
        data = json.dumps(body).encode('utf8')
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                    'Host': 'api.cloudflareclient.com',
                    'Connection': 'Keep-Alive',
                    'Accept-Encoding': 'gzip',
                    'User-Agent': 'okhttp/3.12.1'
                    }
#        req = urllib.request.Request(url, data, headers)
        url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
#        url = "https://midokuriserver.com/ip.php"
#        for num in range(3):
#            try:
#                num += 1
#                if num == 1:
#                    proxies = {"http":"socks4://"+proxy+"/","https":"socks4://"+proxy+"/"}
#                if num == 2:
#                    proxies = {"http":"socks5://"+proxy+"/","https":"socks5://"+proxy+"/"}
#                if num == 3:
#                print("http://"+proxy)
#                proxies = {"http":"http://"+proxy,"https":"http://"+proxy}
#                response = requests.post(url=url,data=data,headers=headers,cookies={},timeout=1)
#                break
#            except Exception as error:
#                if num == 3:
#                    print(error)
#                    return -1
        req = urllib.request.Request(url,data,headers)
        req.set_proxy(proxy, 'http')
        req.set_proxy(proxy, 'https')
        response    = urllib.request.urlopen(req,timeout=15)
        status_code = response.getcode()
        content = response.read()
#        print("\r"+str(status_code)+" - "+response.text,end='')
        return content
    except Exception as error:
#        print(error)
        return "error"

def restarter():
    time.sleep(300)
    print("\nrestart")

#get_proxies()
#threading.Thread(target=get_proxies_async).start()
global plusd
plusd = 0
def threadtarget(proxy):
    global plusd
    result = run(proxy)
    if result != "error":
        plusd += 1
        print("\r"+str(plusd)+"GB",end='')

threading.Thread(target=restarter).start()
try:
    num = 0
    while True:
        num += 1
        get_proxies()
        for proxy in proxy_list:
            while True:
                try:
                    threading.Thread(target=threadtarget,args=(proxy,)).start()
                    break
                except:
                    time.sleep(1)
                    continue
            time.sleep(0.01)
            try:
                while len(threading.enumerate) > 500:time.sleep(1)
            except:pass
        if num == 5:os._exit(0)
except:pass

#def runner():
#    global plusd
#    while True:
#        try:
#            proxy = random.choice(proxy_list)
#            result = run(proxy)
#            if result == 200:
#                plusd += 1
#                print("\r"+str(plusd)+"GB",end='')
#            if result == -1:
#                pass
##                print("proxy error")
##                try:proxy_list.remove(proxy)
##                except:pass
#        except:pass

#for _ in range(500):
#    threading.Thread(target=runner).start()
