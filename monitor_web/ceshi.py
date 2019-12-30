from flask import Flask,jsonify
from celery import Celery
import paramiko

# app = Flask(__name__)
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/1'
#
# celery = Celery(app.name,broker=app.config['CELERY_BROKER_URL'],backend=app.config['CELERY_RESULT_BACKEND'])
# celery.conf.update(app.config)
#
# @celery.task
# def my_back_task(arg1,arg2):
#     return arg1+arg2
#
# @app.route('/',methods=['POST'])
# def index():
#     my_back_task.delay(1,2)
#     return jsonify(error_code=1)
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8002,debug = True)
local_file = "/home/user/Monitor_script/"

def run():
    # with open(config_path, 'r') as f:
    #     conf_txt = f.readlines()
    # for dics in conf_txt:
    #     dicc = eval(dics)
    #     host = dicc['host']
    #     user = dicc['user']
    #     pwd = dicc['pwd']
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("192.168.88.109", 22, username="user", password="priv123", timeout=4)
    cmd = 'ls {}'.format(local_file)
    sdtin, stdout, stderr = client.exec_command(cmd)
    if stdout.readline() != '':
        print("exist")
    else:
        print("not exist")
        cmd = 'mkdir {}'.format(local_file)
        client.exec_command(cmd)

if __name__ == '__main__':
    run()