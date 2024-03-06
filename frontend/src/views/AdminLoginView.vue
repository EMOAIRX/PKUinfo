<script setup>
import { reactive,ref } from 'vue';
import { request } from '@/utils/request';
import { useToast } from 'vue-toastification';
import { useRoute, useRouter } from 'vue-router';
import { useInfoStore } from '../stores/infoStore';
import { storeToRefs } from 'pinia';
import { Eye, EyeOff } from 'lucide-vue-next';

const infoStore = useInfoStore();
const { loginStatus } = storeToRefs(infoStore);
const toast = useToast();
const router = useRouter();
const route = useRoute();

const user = reactive({
  username: route.query.username ? route.query.username : '',
  password: ''
})
const showPassword = ref(false)

async function signin() {
  if (user.username === '' || user.password === '') {
    toast.error('用户名或密码不能为空')
    return;
  }
  await request.post('/admin/login', {
    username: user.username,
    password: user.password
  }).then((res) => {
    // console.log(res.data)
    if (res.data.code === 200) {
      loginStatus.value = true
      sessionStorage.setItem('admin', res.data.data.token)
      toast.success('登录成功')
      if (route.query.redirect) {
        const path = route.query.redirect
        router.replace({ path: path })
        } else {
        router.replace('/')
      }
    }
    else {
      toast.error('用户名或密码错误')
    }
  }).catch((err) => {
    console.log(err)
    toast.error('登录失败')
  })
}

</script>

<template>
  <div class="grow flex flex-col space-y-4 justify-center items-center h-full">
    <h1 class="text-2xl font-bold">管理员登录</h1>
    <label class="input input-bordered flex items-center gap-2">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" /></svg>
      <input type="text" class="grow" placeholder="用户名" v-model="user.username" />
    </label>
    <label class="input input-bordered flex items-center gap-2">
      <svg v-if="!user.password" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path fill-rule="evenodd" d="M14 6a4 4 0 0 1-4.899 3.899l-1.955 1.955a.5.5 0 0 1-.353.146H5v1.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-2.293a.5.5 0 0 1 .146-.353l3.955-3.955A4 4 0 1 1 14 6Zm-4-2a.75.75 0 0 0 0 1.5.5.5 0 0 1 .5.5.75.75 0 0 0 1.5 0 2 2 0 0 0-2-2Z" clip-rule="evenodd" /></svg>
      <input :type="showPassword? 'text':'password'" class="grow" v-model="user.password" placeholder="密码" @keyup.enter="signin"/>
      <!-- 查看密码按钮 -->
      <span v-if="user.password" @click="showPassword=!showPassword">
        <EyeOff class="w-4"  v-if="showPassword"/>
        <Eye class="w-4" v-else/>
      </span>
    </label>
    <!-- <label class="label cursor-pointer">
      <input type="checkbox" v-model="isConstant" class="checkbox checkbox-primary checkbox-sm" />
      <span class="label-text ml-2">保持登录状态</span> 
    </label> -->
    <div class="flex flex-row justify-center items-center space-x-4">
      <button class="btn btn-primary px-10 text-primary-content" @click="signin">登录</button>
    </div>
  </div>
</template>