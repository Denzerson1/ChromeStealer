# Chrome Stealer by Denzerson

This is a Password and History Stealer for the Chrome Browser.

It also has a Web implementation using JS Node and VueJS.

This Software is only for academic use and should not be used in criminal circumstances.

### 1) History Stealer

`HistoryData.py` first copies the History Database (AppData\Local\Google\Chrome\User Data\default\History), so the database can be read, while Google Chrome is running, as when it's running, the database is locked.

We then proceed to make an Sql Query to this SQLite Database, which gets the history, timestamp and title, which we then write into a text file.

### 2) Password Stealer

`LoginData.py` copies the needed Database (Login Data) aswell. The Passwords in this DB are encrypted using AES, which we decrypt by getting the masterkey, stored in Local State DB, which we then decrypt using base64 and win32crypt.

### 3) Webapp

The Data will be sent to a node server (line 53) using a POST HTTP request with the attributes in the url. The attributes (URL, Username, Password) will be written into a json file (`speicher.json`, german for memory), which will then be read and displayed by a VueJS function in `index.html`.


