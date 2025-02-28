from flask import Flask, request
import logging
from datetime import datetime
from flask_cloudflare import Cloudflare

app = Flask(__name__)
cloudflare = Cloudflare(app)

# 配置日志
logging.basicConfig(
    filename='visitor_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

@app.route('/')
def get_device_info():
    # 获取访问者信息
    user_agent = request.headers.get('User-Agent')
    # 使用 Cloudflare 的真实 IP
    ip_address = request.headers.get('CF-Connecting-IP', request.remote_addr)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 记录信息到日志
    visitor_info = f"IP: {ip_address} | User-Agent: {user_agent}"
    logging.info(visitor_info)
    
    return "访问已记录"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 