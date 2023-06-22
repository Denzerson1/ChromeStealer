var http = require('http');
var url = require('url');
var fs = require('fs');
let list = read();

class Login {
  constructor(url,user,pwd) {
    this.url =  url,
    this.user = user,
    this.pwd = pwd;
  }
}

http.createServer(function (req, res) {
    const headers = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, GET",
      "Access-Control-Max-Age": 2592000,
      'Content-Type': 'text/json'
    };
    res.writeHead(200, headers);
    var u = url.parse(req.url, true)
    console.log(u.query)
    console.log(u.pathname)
    console.log("method: " + req.method)
    
  
    if(req.method === 'POST') {
      var info = new Login(u.query.url, u.query.user, u.query.pwd);
      sendData(info);
      syncsave();
    }

    res.end(JSON.stringify(list))
  }).listen(8080); 


  function sendData(obj) {
    list.push(obj);
  }

  function syncsave() {
    fs.writeFile('speicher.json', JSON.stringify(list), (err) => {
      if (err) throw err;
      console.log('Data written to file');
    });
  }

  function read() {
    return JSON.parse(fs.readFileSync('speicher.json'));
  }