import requests
import random,string,time,os


def logo():
    print('''
                                                                           /$$           /$$      
                                                                      | $$          | $$      
  /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$$| $$ /$$   /$$| $$$$$$$ 
 |____  $$| $$__  $$ /$$__  $$| $$  | $$ |____  $$| $$__  $$ /$$_____/| $$| $$  | $$| $$__  $$
  /$$$$$$$| $$  \ $$| $$  \ $$| $$  | $$  /$$$$$$$| $$  \ $$| $$      | $$| $$  | $$| $$  \ $$
 /$$__  $$| $$  | $$| $$  | $$| $$  | $$ /$$__  $$| $$  | $$| $$      | $$| $$  | $$| $$  | $$
|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$|  $$$$$$/| $$$$$$$/
 \_______/|__/  |__/ \____  $$ \______/  \_______/|__/  |__/ \_______/|__/ \______/ |_______/ 
                          | $$                                                                
                          | $$                                                                
                          |__/                                                                ''')
    print("                                                                                     ")
    print("                        Ewomail一键批量生成邮箱脚本                                    ")
    print("                                  沐寒                                               ")
    print("                               安全小天地                                             ")
    print("                            www.anquanclub.cn                                        ")
    print("          如果生成失败，请删除配置文件，重新获取cookie，或者直接修改cookie                ")
    print("                                                                                     ")


logo()

if(os.path.exists("配置信息.txt")):
    data = open('配置信息.txt',encoding="utf-8").readlines()
    
    url_base = data[0].replace('\n','').replace('邮件管理器后台地址：','')
    global email_addr
    email_addr = data[1].replace('\n','').replace('邮箱后缀：','')
    global cookie
    cookie = data[2].replace('\n','').replace('cookie：','')
else:
    url_base = str(input("请输入邮件管理器后台地址(eg：http://mail.anquanclub.cn:8010)："))
    email_addr = str(input("请输入邮箱后缀(eg：anquanclub.cn)："))
    cookie = str(input("请输入cookie："))
    with open('配置信息.txt','w',encoding='utf-8') as f:
        f.write('邮件管理器后台地址：' + url_base + '\n' + '邮箱后缀：' + email_addr + '\n' + 'cookie：' + cookie + '\n')

def ask_url(cookie,url_base):
    url = str(url_base) + "/Users/edit"
    cookies = {"PHPSESSID": cookie}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "http://mail.anquanclub.cn:8010", "Connection": "close", "Referer": "http://mail.anquanclub.cn:8010/Users/edit"}
    data = {"email": str(email), "uname": "12345", "tel": "12345", "active": "1", "password": str(passwd), "password2": str(passwd), "_method": "put", "_forward": "%2FUsers"}
    requests.post(url, headers=headers, cookies=cookies, data=data,timeout=60)



def create_email(count,email_legth,passwd_legth,email_addr,cookie):
    with open('create_email.txt','a+',encoding="utf-8") as f:
        for i in range(count):
            str1 = ''.join(random.sample(string.ascii_letters,email_legth-1))
            str2 = ''.join(random.sample(string.digits,3))
            str3 = ''.join(random.sample(string.ascii_letters,passwd_legth-1))
            str4 = ''.join(random.sample(string.digits,5))

            global email,passwd
            email = str1.lower() + str2.lower() + '@' + email_addr
            passwd = str3 + str4

            ask_url(cookie,url_base)
            f.write('邮箱：' + email + '        ' + '密码：' + passwd + '\n')







count = int(input('请输入需要产生邮箱的个数:').strip())
email_legth = int(input('请输入邮箱长度:').strip())
passwd_legth = int(input('请输入密码长度:').strip())


create_email(count,email_legth,passwd_legth,email_addr,cookie)
print("创建完成，请查看create_email文本，并登录后台查看(cookie失效则后台不会生成邮箱)！！！")
time.sleep(10)
