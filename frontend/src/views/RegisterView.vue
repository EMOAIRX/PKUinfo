<script setup>
import { reactive, ref } from 'vue';
import { request } from '@/utils/request';
import { useToast } from 'vue-toastification';
import { useRoute, useRouter } from 'vue-router';
import { Mail } from 'lucide-vue-next';
import { encrypt } from '@/utils/aes';
import { Eye, EyeOff } from 'lucide-vue-next';
import zxcvbn from 'zxcvbn';
const toast = useToast();
const router = useRouter();
const route = useRoute();

const user = reactive({
  username: '',
  password: '',
  email: ''
})
const showPassword = ref(false)

async function signup() {
  if (user.username === '' || user.password === '' || user.email === '') {
    toast.error('填写信息不能为空')
    return;
  }
  // 验证user.email是否为邮箱
  if (!/^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/.test(user.email)) {
    toast.error('邮箱格式错误，请检查信息',{
      timeout: 3000
    })
    return;
  }
  await request.put('/register', {
    username: user.username,
    password: encrypt(user.password),
    email: user.email
  }).then((res) => {
    if (res.data.code === 200) {
      toast.success('注册成功')
      router.replace({
        path: "/login",
        query: {
          username: user.username,
          redirect: route.query.redirect ? route.query.redirect : '/'
        }
      })
    }
    else {
      if (res.data.code === 400) {
        toast.error('用户名已存在')
      }
      else {
        toast.error('数据库异常')
      }
    }
  }).catch((err) => {
    console.log(err)
    toast.error('注册失败')
  })
}

</script>

<template>
  <div class="grow flex flex-col space-y-4 justify-center items-center h-full">
    <h1 class="text-2xl font-bold">注册</h1>
    <label class="input input-bordered flex items-center gap-2">
      <Mail class="w-4"/>
      <input type="email" class="grow" placeholder="Email" v-model="user.email" />
    </label>
    <label class="input input-bordered flex items-center gap-2">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" /></svg>
      <input type="text" class="grow" placeholder="用户名" v-model="user.username" @keyup.enter="signup"/>
    </label>
    <label class="input input-bordered flex items-center gap-2">
      <svg v-if="!user.password" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path fill-rule="evenodd" d="M14 6a4 4 0 0 1-4.899 3.899l-1.955 1.955a.5.5 0 0 1-.353.146H5v1.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-2.293a.5.5 0 0 1 .146-.353l3.955-3.955A4 4 0 1 1 14 6Zm-4-2a.75.75 0 0 0 0 1.5.5.5 0 0 1 .5.5.75.75 0 0 0 1.5 0 2 2 0 0 0-2-2Z" clip-rule="evenodd" /></svg>
      <input :type="showPassword? 'text':'password'" class="grow" v-model="user.password" placeholder="密码" @keyup.enter="signup"/>
      <!-- 查看密码按钮 -->
      <span v-if="user.password" @click="showPassword=!showPassword">
        <EyeOff class="w-4"  v-if="showPassword"/>
        <Eye class="w-4" v-else/>
      </span>
    </label>
    <div class="text-xs text-center" v-if="user.password">
      <h4>
        密码强度：
        {{ ['很弱', '弱', '一般', '强', '很强'][zxcvbn(user.password).score] }}<span v-if="user.password.length>15"> 但是你记得住吗</span>
      </h4>
      <progress class="progress opacity-70 w-64 progress-primary" :value="(zxcvbn(user.password).score)*20" max="100" :style="{backgroundColor: ['red', 'orange', 'yellow', 'green', 'green'][zxcvbn(user.password).score]}"></progress>
    </div>
    <div class="flex flex-row justify-center items-center space-x-4">
      <button class="btn btn-accent text-accent-content px-8" @click="signup">注册</button>
    <button class="btn btn-ghost" @click="router.replace('/login')">返回登录</button>
    </div>
  </div>
</template>