import subprocess
from database_setup import Database 
#import libraries

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')#gets all the wifis the device has connected to
wifi = [line.split(':')[1][1:-1] for line in data if 'All User Profile' in line]#splits up each line from the output into induvisual wifi connection ines

db = Database('passwords.db')

for w in wifi:
    results = subprocess.check_output('netsh wlan show profile ' + '"' + w + '"' + ' key=clear',
                                           shell=True).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        insert = True
        for row in db.view():
            if w==row[1]:
                insert = False
                break
        if insert:
            db.insert(w,results[0])
        else:
            continue
    except IndexError:
        db.insert(w,'Cannot be read')
#loops through all the wifis and adds then to the database

for row in db.view():
    print(row)