addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  // 获取访问者信息
  const userAgent = request.headers.get('User-Agent')
  const ip = request.headers.get('CF-Connecting-IP')
  const timestamp = new Date().toISOString()
  
  // 这里可以添加日志记录逻辑
  // 注意：在 Workers 中，我们需要使用其他方式存储日志，比如 Workers KV 或外部服务
  
  const visitorInfo = {
    ip: ip,
    userAgent: userAgent,
    timestamp: timestamp
  }
  
  // 返回简单的响应
  return new Response('访问已记录', {
    headers: { 'content-type': 'text/plain;charset=UTF-8' }
  })
} 