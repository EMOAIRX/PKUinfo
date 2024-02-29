<script setup>
import { reactive } from 'vue';
import { request } from '@/utils/request';
import { useToast } from 'vue-toastification';
import { useRoute, useRouter } from 'vue-router';
import { useInfoStore } from '../stores/infoStore';
import { storeToRefs } from 'pinia';
import { encrypt } from '@/utils/aes';

const infoStore = useInfoStore();
const { loginStatus } = storeToRefs(infoStore);
const toast = useToast();
const router = useRouter();
const route = useRoute();

console.log(route.query.username)

const user = reactive({
  username: route.query.username ? route.query.username : '',
  password: ''
})

function signin() {
  request.post('/login', {
    username: user.username,
    password: encrypt(user.password)
  }).then((res) => {
    console.log(res.data)
    if (res.data.code === 200) {
      loginStatus.value = true
      sessionStorage.setItem('auth', JSON.stringify(res.data))
      sessionStorage.setItem('token', res.data.data.token)
      toast.success('登录成功',{
        timeout: 2000
      })
      if (route.query.redirect) {
        const path = route.query.redirect
        router.push({ path: path })
        } else {
        router.push('/')
      }
    }
    else {
      toast.error('用户名或密码错误',{
        timeout: 2000
      })
    }
  }).catch((err) => {
    console.log(err)
    toast.error('登录失败',{
      timeout: 2000
    })
  })
}

</script>

<template>
  <div class="grow flex flex-col space-y-4 justify-center items-center h-full">
    <h1 class="text-2xl font-bold">登录</h1>
    <label class="input input-bordered flex items-center gap-2">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" /></svg>
      <input type="text" class="grow" placeholder="Username" v-model="user.username" />
    </label>
    <label class="input input-bordered flex items-center gap-2">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path fill-rule="evenodd" d="M14 6a4 4 0 0 1-4.899 3.899l-1.955 1.955a.5.5 0 0 1-.353.146H5v1.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-2.293a.5.5 0 0 1 .146-.353l3.955-3.955A4 4 0 1 1 14 6Zm-4-2a.75.75 0 0 0 0 1.5.5.5 0 0 1 .5.5.75.75 0 0 0 1.5 0 2 2 0 0 0-2-2Z" clip-rule="evenodd" /></svg>
      <input type="password" class="grow" v-model="user.password" />
    </label>
    <div class="flex flex-row justify-center items-center space-x-4">
      <button class="btn btn-primary px-6 text-primary-content" @click="signin">登录</button>
    <button class="btn btn-neutral px-6" @click="router.push('/register')">注册</button>
    </div>
  </div>
</template>