import time
from datetime import datetime as dt
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
temp = "hosts"
redirect = "127.0.0.1"
website_list=["www.facebook.com","facebook.com","fmovies.pe"]
while True:
    if(dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,20)):

        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("sleeping hours hahahahahha\n")

    else:
        print("working hours")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n"+redirect+" "+website+"\n")

    time.sleep(5)
