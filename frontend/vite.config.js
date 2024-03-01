import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  // server: {
  //   proxy: {
  //     // 类型： Record<string, string | ProxyOp 为开发服务器配置自定义代理规则
  //     '/api': {
  //       target: 'http://111.229.135.84:8080/',
  //       changeOrigin: true,
  //       // secure: false,
  //       rewrite: (path) => path.replace('/api', '')
  //     }
  //   }
  // },
  server: {
    proxy:{
      '/api': {
        target: 'https://pkuinfo.lcpu.dev',
        changeOrigin: true,
        secure: false,
        pathRewrite: {
          '^/api':'/'
        }
      },
    }
  }
})
