import requests, random, base64, itertools, hashlib, threading, time
from string import ascii_letters, digits

possible_letters = ascii_letters + digits

print("2.2 List Likebot / Dislikebot by Sevenworks bruh hes cool lmao !!! would date")
listID = input("List ID: ")
liketype = input("Like/Dislike (0/1): ")

def icedcave_plz_unblock_me(bozo):
    with open(bozo, 'r') as file: proxies = [line.strip() for line in file]
    return proxies

def get_proxy(proxies):
    return random.choice(proxies)

proxies = icedcave_plz_unblock_me("proxies.txt")

def SAF(file_path):
    gjuser = []
    gjpass = []
    gjaccid = []
    with open(file_path, 'r') as file:
        for line in file:
            homer, simpson, doh = line.strip().split(' / ')
            gjuser.append(homer)
            gjpass.append(simpson)
            gjaccid.append(doh)
    return gjuser, gjpass, gjaccid

gjuser, gjpass, gjaccid = SAF("accounts.txt")

def xor(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, itertools.cycle(key)))

def gjp_encrypt(data):
    return base64.b64encode(xor(data,"37526").encode()).decode()

def generate_chk(values: [int, str] = [], key: str = "", salt: str = "") -> str:
    values.append(salt)
    string = ("").join(map(str, values))
    hashed = hashlib.sha1(string.encode()).hexdigest()
    xored = xor_cipher(hashed, key)
    final = base64.urlsafe_b64encode(xored.encode()).decode()
    return final

def generate_rs(n: int) -> str:
    return ("").join(random.choices(possible_letters, k=n))

def generate_uuid(parts: [int] = (8, 4, 4, 4, 10)) -> str:
    return ("-").join(map(generate_rs, parts))

def generate_udid(start: int = 100_000, end: int = 100_000_000) -> str:
    return "S" + str(random.randint(start, end))

def bot():
  for i in range(len(gjuser)):
    proxy = get_proxy(proxies)
    proxies = { "http": proxy, "https": proxy }
    data = {
        "gameVersion": "20",
        "binaryVersion": "35",
        "gdw": "0",
        "accountID": gjaccid[i],
        "gjp": gjp_encrypt(gjpass[i]),
        "udid": generate_udid(),
        "uuid": generate_uuid(),
        "itemID": listID,
        "like": liketype,
        "type": "4",
        "secret": "Wmfd2893gb7",
        "special": "0"
    }
    req = requests.post("http://www.boomlings.com/database/likeGJItem211.php", data=data, headers={"User-Agent":""}, proxies=proxies)

while True:
  threading.Thread(target=bot).start()
  time.sleep(2)
