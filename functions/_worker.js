export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    // 将所有请求转发到 Flask 应用
    return await fetch(`http://127.0.0.1:5000${url.pathname}${url.search}`, {
      headers: request.headers,
      method: request.method,
      body: request.body
    });
  }
}; 