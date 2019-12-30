import subprocess
import time
import paramiko
import select
import redis
import socket
import pymysql
import os
import datetime
import sys
from pymongo import MongoClient

# from config import *
dir_path = os.getcwd()
config_path = dir_path+'/config/config.txt'
# conn = MongoClient('127.0.0.1',27017)
# db = conn.monitor
# moni_data = db.moni_data
# moni_script = db.moni_script
def run(moni_time):
    while True:

        with open(config_path,'r') as yaml_file:
            yaml_obj = yaml_file.readlines()

        for dict in yaml_obj:
            time1 = time.time()
            dict = eval(dict)
            host = dict['host']
            user = dict['user']
            pwd = dict['pwd']
            time_run = dict['time']
            # print('------------开始连接服务器(%s)-----------' % host)
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # print('------------开始认证......-----------')
            try:
                client.connect("192.168.88.91", 22, username="user", password="priv123", timeout=4)
                print(dir_path+'/monitor_perf.py')
                cmd = 'python3 {} {}'.format(dir_path+'/monitor_perf.py',1800)
                stdin, stdout, stderr = client.exec_command(cmd)
                #     if dic_data:
                #         total_mess = dic_data['total_mess']
                #         pid_list = dic_data['pid_mess']
                #         moni_data.insert(total_mess)
                #         for pid_ss in pid_list:
                #             if pid_ss:
                #                 timestamp = time.time()
                #                 pid_ss['net_ip'] = host
                #                 pid_ss['timestamp'] = int(timestamp)
                #                 moni_script.insert(pid_ss)
                        # my_set.insert(dic_data)

                # print('result----{}'.format(result))
                # 服务器开启
                # print('------------认证成功!.....-----------')
            except Exception as e:
                # 服务器禁用或者账号密码错误
                # print('------------认证失败!.....-----------')
                status = 0
                print(e)
                continue

            client.close()
            time2=time.time()
            print(time2-time1)

        time.sleep(moni_time)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        moni_time = 1800
    else:
        moni_time = int(sys.argv[1])

    run(moni_time)