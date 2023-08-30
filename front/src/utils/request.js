import axios from 'axios'
// 封装 baseURL
const request = axios.create({
    baseURL: "https://pkuinfo.lcpu.dev/api"
    // baseURL: "http://localhost:8080/api"
})
// 向外暴露 request
export default request;