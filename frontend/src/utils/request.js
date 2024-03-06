import axios from 'axios'

// 封装 baseURL
const request = axios.create({
    // baseURL: "https://pkuinfo.lcpu.dev/api"
    // baseURL: "http://111.229.135.84:8080",
    baseURL: "/api",
    timeout: 100000,
})
request.defaults.headers['X-Requested-With'] = 'XMLHttpRequest'
request.defaults.headers.post['Content-Type'] = 'application/json'

// 请求拦截器
request.interceptors.request.use(
  (config) => {
    if (sessionStorage.getItem('auth')) {
      config.headers.Authorization = `Bearer ${sessionStorage.getItem('auth')}`
    }
    if (sessionStorage.getItem('admin')) {
      config.headers.Authorization = `Bearer ${sessionStorage.getItem('admin')}`
    }
    return config
  },
  (err) => Promise.reject(err)
)

// 向外暴露 request
export { request }