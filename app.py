from flask import Flask, request
import logging
from datetime import datetime
import socket
import netifaces

app = Flask(__name__)

# 配置日志
logging.basicConfig(
    filename='visitor_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def get_local_ip():
    try:
        # 获取所有网络接口的IP地址
        ips = []
        for interface in netifaces.interfaces():
            try:
                addrs = netifaces.ifaddresses(interface)
                if netifaces.AF_INET in addrs:
                    for addr in addrs[netifaces.AF_INET]:
                        ips.append(addr['addr'])
            except:
                continue
        return ips
    except:
        return ["无法获取本机IP"]

@app.route('/')
def get_device_info():
    # 获取访问者信息
    user_agent = request.headers.get('User-Agent')
    # 直接从请求头获取 CF-Connecting-IP
    ip_address = request.headers.get('CF-Connecting-IP', request.remote_addr)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 记录信息到日志
    visitor_info = f"IP: {ip_address} | User-Agent: {user_agent}"
    logging.info(visitor_info)
    
    return "访问已记录"

@app.route('/_health')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    local_ip = get_local_ip()
    print(f"\n可通过以下地址访问：")
    print(f"本地访问: http://localhost:5000")
    print("所有可用地址:")
    for ip in local_ip:
        print(f"http://{ip}:5000")
    print("")
    app.run(host='0.0.0.0', port=5000) 