# Simple Web Application

This is a simple web application using [Python Flask](http://flask.pocoo.org/) and [MySQL](https://www.mysql.com/) database. 
This is used in the demonstration of the development of Ansible Playbooks.
  
  Below are the steps required to get this working on a base linux system.
  
  - **Install all required dependencies**
  - **Install and Configure Web Server**
  - **Start Web Server**
   
## 1. Install all required dependencies
  
  Python and its dependencies
  ```bash
  apt-get install -y python3 python3-setuptools python3-dev build-essential python3-pip default-libmysqlclient-dev
  ```
   
## 2. Install and Configure Web Server

Install Python Flask dependency
```bash
pip3 install flask
export HOSTNAME=$machineName
```


## 3. Start Web Server

Start web server
```bash
sudo FLASK_APP=app.py flask run --host=0.0.0.0 --port 80
```

## 4. Test

Open a browser and go to URL
```
http://<IP>:80                       => Welcome
http://<IP>:80/healtcheck            => Json server health output 
```
