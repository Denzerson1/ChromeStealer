import os
import sys 
import argparse
import sqlite3
import shutil
import pypyodbc as odbc
import pandas as pd
import pyodbc

os_Platform = sys.platform
        
def getpath():
    if os_Platform =="win32" or os_Platform == "cygwin":
        PathName = os.getenv("localappdata") + '\\\Google\\Chrome\\User Data\\Default\\'
    else:
        if os_Platform == "linux" or os_Platform == "linux2":
            PathName = '/.config/google-chrome/Defaults '
        else:
            print("Currently Operating System Not Supported")
    return PathName


def Extracter(): 
    path = getpath()
    info_list = []
    login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\History'
    shutil.copy2(login_db, "Historyvault.db") #making a temp copy since Login Data DB is locked while Chrome is running

    try:
        connection = sqlite3.connect('Historyvault.db')
        with connection:   # Context Manager
            cursor = connection.cursor()
            v = cursor.execute("""SELECT url, title, datetime((last_visit_time/1000000)-11644473600, 'unixepoch', 'localtime') 
                                    AS last_visit_time FROM urls ORDER BY last_visit_time DESC""")
            value = v.fetchall()
        
            for url,title,last_visit_time in value:
                info_list.append({
                    "Url": url,
                    "Title": title,
                    "Date&Time":last_visit_time 
                })
        cursor.close()
        connection.close()
        os.remove("Historyvault.db")
        
    except sqlite3.OperationalError as e:
        print(e)
    return info_list

def output_text(info):
    with open('Chrome_history.txt','wb') as txt_file:
        for data in info:
            txt_file.write(f"{data['Url']} \t\t {data['Title']} \t\t{data['Date&Time']} \n".encode('utf-8'))  #bytes to string
    print("Data written in Chrome_history.txt")
    

if __name__ == "__main__":
    output_text(Extracter())