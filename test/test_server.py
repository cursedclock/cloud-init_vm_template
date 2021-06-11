from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/meta-data')
@app.route('/user-data')
@app.route('/vendor-data')
def send_config_data():
    print('Guest machine requested {}.'.format(request.path[1:]))
    data = ''
    with open('config'+request.path, 'r') as f:
        data = f.read()
    print('sending data:\n'+data)
    return data

@app.route('/done',methods = ['POST'])
def log_phone_home_data():
    data = ''.join([i+': '+request.form[i]+'\n' for i in request.form])
    print('Guest machine posted data:\n'+data)
    with open('config/output', 'w+') as f:
        f.write(data)
    return ''
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
