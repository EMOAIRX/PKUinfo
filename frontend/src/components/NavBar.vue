<script setup>
import { RouterLink } from 'vue-router'
import { SwatchBook } from 'lucide-vue-next';
import { useInfoStore } from '../stores/infoStore';
import { storeToRefs } from 'pinia';
import { onMounted,ref } from 'vue';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';

const router = useRouter();
const toast = useToast();

const infoStore = useInfoStore();
const { loginStatus } = storeToRefs(infoStore);
const navdropdown = ref(null);
const avatardropdown = ref(null);

function signout() {
  loginStatus.value = false;
  sessionStorage.removeItem('auth');
  sessionStorage.removeItem('token');
  sessionStorage.removeItem('admin')
  if (localStorage.getItem('auth')) {
    localStorage.removeItem('auth');
  }
  if (router.currentRoute.value.path === '/profile') {
    router.replace('/');
  }
  toast.info('注销成功',{
    timeout: 2000
  });
}

// 将当前路由导航高亮
function activeClass(route) {
  return router.currentRoute.value.path === route ? 'active' : '';
}

function closeDropdown() {
  navdropdown.value.removeAttribute('open');
}
function closeavatar() {
  avatardropdown.value.removeAttribute('open');
}

onMounted(() => {
  // console.log('loginStatus', loginStatus.value);
  // 当dropdown打开时，点击其他地方关闭dropdown
  document.addEventListener('click', (e) => {
    if (navdropdown.value && !navdropdown.value.contains(e.target)) {
      closeDropdown();
    }
    if (avatardropdown.value && !avatardropdown.value.contains(e.target)) {
      closeavatar();
    }
  });
});
</script>

<template>
  <nav class="navbar bg-base-300">
    <div class="flex flex-1">
      <details ref="navdropdown" class="dropdown">
        <summary class="btn btn-ghost lg:hidden">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" /></svg>
        </summary>
        <ul class="menu dropdown-content z-[1] p-2 shadow bg-base-200 rounded-sm mt-3 w-28" @click="closeDropdown">
          <li>
            <RouterLink to="/">活动列表</RouterLink></li>
          <li>
            <RouterLink to="/calendar" >活动日历</RouterLink>
          </li>
          <li>
            <RouterLink to="/profile" replace>订阅活动</RouterLink>
          </li>
          <li>
            <RouterLink to="/about" replace>关于</RouterLink>
          </li>
        </ul>
      </details>
      <div class="flex flex-1 flex-grow">
        <a class="btn btn-ghost text-2xl font-semibold" id="mainTitle">PKU Info</a>
      </div>
    </div>

    <div class="navbar-end">
      <div class="hidden lg:flex flex-row space-x-4 mr-6">
        <RouterLink class="font-semibold hover:underline underline-offset-8" :class="activeClass('/')" to="/" replace>活动列表</RouterLink>
        <RouterLink class="font-semibold hover:underline underline-offset-8" :class="activeClass('/calendar')" to="/calendar" replace>活动日历</RouterLink>
        <RouterLink class="font-semibold hover:underline underline-offset-8" :class="activeClass('/profile')" to="/profile">订阅活动</RouterLink>
        <RouterLink class="font-semibold hover:underline underline-offset-8" :class="activeClass('/about')" to="/about" replace>关于</RouterLink>
      </div>
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn bg-base-300 border-none m-1">
          <SwatchBook />
          <p class=" hidden md:block">主题</p>
          <svg width="12px" height="12px" class="h-2 w-2 fill-current opacity-60 inline-block" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2048 2048"><path d="M1799 349l242 241-1017 1017L7 590l242-241 775 775 775-775z"></path></svg>
        </div>
        <ul tabindex="0" class="dropdown-content z-[1] p-2 shadow-2xl bg-base-200 rounded-box">
          <li><input type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Light" value="light"/></li>
          <li><input type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Dark" value="dark"/></li>
          <li><input type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Luxury" value="luxury"/></li>
          <li><input type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Valentine" value="valentine"/></li>
        </ul>
      </div>

      <details ref="avatardropdown" class="dropdown dropdown-end">
        <summary class="btn btn-ghost btn-circle avatar" :class="loginStatus ? 'online':'offline'">
          <div class="w-8 rounded-full" >
            <img alt="avatar" src="/favicon.png" />
          </div>
        </summary>
        <ul class="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-200 rounded-sm w-32" @click="closeavatar">
          <li><RouterLink to="/profile">订阅活动</RouterLink></li>
          <li v-if="loginStatus"><a @click="signout">注销</a></li>
          <li v-else><RouterLink to="/login">登录</RouterLink></li>
        </ul>
      </details>
    </div>
  </nav>
</template>

<style scoped>
a.active {
  color:  oklch(var(--p));
  scale: 1.05;
}
</style>