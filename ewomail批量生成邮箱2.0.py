import requests
import random,string,time,os,json


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
    print("                                                                                     ")
    print("                            ****功能列表****                                          ")
    print("                        ****功能1：批量生成邮箱****                                    ")
    print("              ****功能2：批量添加邮箱到指定邮箱，方便接收验证码****                      ")
    print("                                                                                     ")

def check_create_mail_config():
    if(os.path.exists("create_mail_config.txt")):
        data = open('create_mail_config.txt',encoding="utf-8").readlines()
        
        url_base = data[0].replace('\n','').replace('邮件管理器后台地址：','').replace(' ','')
        global email_addr
        email_addr = data[1].replace('\n','').replace('邮箱后缀：','').replace(' ','')
        global houtai_cookie
        houtai_cookie = data[2].replace('\n','').replace('邮件管理员后台cookie：','').replace(' ','')
    else:
        url_base = str(input("请输入邮件管理器后台地址(eg：http://mail.anquanclub.cn:8010)：")).replace(' ','')
        email_addr = str(input("请输入邮箱后缀(eg：anquanclub.cn)：")).replace(' ','')
        houtai_cookie = str(input("请输入邮件管理员后台cookie：")).replace(' ','')
        with open('create_mail_config.txt','w',encoding='utf-8') as f:
            f.write('邮件管理器后台地址：' + url_base + '\n' + '邮箱后缀：' + email_addr + '\n' + '邮件管理员后台cookie：' + houtai_cookie + '\n')
    return url_base,email_addr,houtai_cookie

def check_add_mail_config():
    if(os.path.exists("add_mail_config.txt")):
        data = open('add_mail_config.txt',encoding="utf-8").readlines()
        
        global url_mail
        url_mail = data[0].replace('\n','').replace('邮箱网址：','').replace(' ','')
        global url_add_mail
        url_add_mail = data[1].replace('\n','').replace('添加邮箱的连接：','').replace(' ','')
        global mail_cookies
        mail_cookies = data[2].replace('\n','').replace('添加邮箱的cookies：','').replace(' ','')
        global add_mail_cookies
        add_mail_cookies = json.loads(mail_cookies)
        global XToken
        XToken = data[3].replace('\n','').replace('添加邮箱的XToken：','').replace(' ','')
    else:
        url_mail = str(input("请输入获取的邮箱网址(eg:http://xx.cn:8000):")).replace(' ','')
        url_add_mail = str(input("请输入获取的添加邮箱的连接(eg:http://xx.cn:8000/?/Ajax/&q[]=/_xxxxxx/):")).replace(' ','')
        mail_cookies = str(input('请输入获取的添加邮箱的cookies(eg:{"rltoken": "xxx", "rlsession": "xxx", "PHPSESSID": "xxx"}):')).replace(' ','')
        XToken = str(input('请输入获取的添加邮箱的XToken(eg:f5e2d4a777fbd158087e0aa44f395415):')).replace(' ','')
        
        with open('add_mail_config.txt','w',encoding='utf-8') as f:
            f.write('邮箱网址：' + url_mail + '\n' + '添加邮箱的连接：' + url_add_mail + '\n' + '添加邮箱的cookies：' + mail_cookies + '\n' + '添加邮箱的XToken：' + XToken + '\n')
        add_mail_cookies = json.loads(mail_cookies)
    return url_mail,url_add_mail,mail_cookies,add_mail_cookies,mail_cookies

def ask_url(cookie,url_base):
    url = str(url_base) + "/Users/edit"
    cookies = {"PHPSESSID": cookie}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "http://mail.anquanclub.cn:8010", "Connection": "close", "Referer": "http://mail.anquanclub.cn:8010/Users/edit"}
    data = {"email": str(email), "uname": "12345", "tel": "12345", "active": "1", "password": str(passwd), "password2": str(passwd), "_method": "put", "_forward": "%2FUsers"}
    requests.post(url, headers=headers, cookies=cookies, data=data,timeout=60)

def ask_url_add(url_add_mail,add_email,add_email_password,XToken,url_mail,add_mail_cookies):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": url_mail, "Connection": "close", "Referer": url_mail}
    data = {"Email": add_email, "Password": add_email_password, "New": "1", "Action": "AccountSetup", "XToken": XToken}
    requests.post(url_add_mail, headers=headers, cookies=add_mail_cookies, data=data,timeout=60)

def create_email(count,email_legth,passwd_legth,email_addr,houtai_cookie):
    with open('create_email.txt','a+',encoding="utf-8") as f:
        for i in range(count):
            str1 = ''.join(random.sample(string.ascii_letters,email_legth-1))
            str2 = ''.join(random.sample(string.digits,3))
            str3 = ''.join(random.sample(string.ascii_letters,passwd_legth-1))
            str4 = ''.join(random.sample(string.digits,5))

            global email,passwd
            email = str1.lower() + str2.lower() + '@' + email_addr
            passwd = str3 + str4

            ask_url(houtai_cookie,check_create_mail_config[0])
            f.write('邮箱：' + email + '        ' + '密码：' + passwd + '\n')





logo()

while 1:
    flag = input("请输入你需要进行的操作：")
    if(flag == '1'):
        try:
            check_create_mail_config = check_create_mail_config()

            count = int(input('请输入需要产生邮箱的个数:').strip())
            email_legth = int(input('请输入邮箱长度:').strip())
            passwd_legth = int(input('请输入密码长度:').strip())


            create_email(count,email_legth,passwd_legth,email_addr,houtai_cookie)
            print("创建完成，请查看create_email文本，并登录后台查看(cookie失效则后台不会生成邮箱)！！！")
            print("              ")
            time.sleep(10)
            continue
        except Exception as e:
            print("请检查端口信息是否填写正确，配置是否完善，然后再次重新运行该工具！！！")
            time.sleep(5)
            break
    elif(flag == '2'):
        try:
            check_add_mail_config = check_add_mail_config()
            print("正在进行初始化配置，请稍等~~~")
            for i in open('create_email.txt','r',encoding='utf-8'):
                i = i.replace(' ','').replace('：','').replace('邮箱','').replace('\n','').replace(' ','')
                add_email = i.split('密码')[0]
                add_email_password = i.split('密码')[1]
                ask_url_add(url_add_mail,add_email,add_email_password,XToken,url_mail,check_add_mail_config[3])
            
            print("添加完成，请登录该邮箱点击设置查看(cookie失效则后台不会添加邮箱)！！！")
            time.sleep(10)
            break
        except Exception as e:
            print("请检查端口信息是否填写正确，配置是否完善，然后再次重新运行该工具！！！")
            time.sleep(5)
            break
    else:
        print("请不要输入其他内容，谢谢！！！")
        print("                           ")
        continue
