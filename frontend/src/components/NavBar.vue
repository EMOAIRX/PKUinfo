<script setup>
import { RouterLink } from 'vue-router'
import { SwatchBook } from 'lucide-vue-next';
import { useInfoStore } from '../stores/infoStore';
import { storeToRefs } from 'pinia';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';

const router = useRouter();
const toast = useToast();

const infoStore = useInfoStore();
const { loginStatus } = storeToRefs(infoStore);

function signout() {
  loginStatus.value = false;
  sessionStorage.removeItem('auth');
  sessionStorage.removeItem('token');
  // 如果是在/settings页面登出，登出后跳转到/login页面
  if (router.currentRoute.value.path === '/settings' || router.currentRoute.value.path === '/profile') {
    router.replace('/');
  }
  toast.info('Logout successfully',{
    timeout: 2000
  });
}

onMounted(() => {
  console.log('loginStatus', loginStatus.value);
});
</script>

<template>
  <nav class="navbar bg-base-300">
    <div class="flex flex-1">
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" /></svg>
        </div>
        <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
          <li><RouterLink to="/">Home</RouterLink></li>
          <li>
            <RouterLink to="/calendar">Calendar</RouterLink>
          </li>
          <li>
            <RouterLink to="/profile">Profile</RouterLink>
          </li>
          <li>
            <RouterLink to="/about">About</RouterLink>
          </li>
        </ul>
      </div>
      <div class="flex flex-1 flex-grow">
        <a class="btn btn-ghost text-2xl font-semibold">PKU Info</a>
      </div>
    </div>

    <div class="navbar-end">
      <div class="hidden lg:flex flex-row space-x-4 mr-6">
        <RouterLink class="font-semibold hover:underline underline-offset-8" to="/" replace>Home</RouterLink>
        <RouterLink class="font-semibold hover:underline underline-offset-8" to="/calendar" replace>Calendar</RouterLink>
        <RouterLink class="font-semibold hover:underline underline-offset-8" to="/profile">Profile</RouterLink>
        <RouterLink class="font-semibold hover:underline underline-offset-8" to="/about" replace>About</RouterLink>
      </div>
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn bg-base-300 border-none m-1">
          <SwatchBook />
          <p class=" hidden md:block">Theme</p>
          <svg width="12px" height="12px" class="h-2 w-2 fill-current opacity-60 inline-block" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2048 2048"><path d="M1799 349l242 241-1017 1017L7 590l242-241 775 775 775-775z"></path></svg>
        </div>
        <ul tabindex="0" class="dropdown-content z-[1] p-2 shadow-2xl bg-base-200 rounded-box">
          <li><input type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Light" value="light"/></li>
          <li><input type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Dark" value="dark"/></li>
          <li><input type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Luxury" value="luxury"/></li>
          <li><input type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Valentine" value="valentine"/></li>
        </ul>
      </div>

      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
          <div class="w-10 rounded-full">
            <img alt="Tailwind CSS Navbar component" src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
          </div>
        </div>
        <ul tabindex="0" class="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-32">
          <li><RouterLink to="/profile">Profile</RouterLink></li>
          <li v-if="loginStatus"><a @click="signout">Logout</a></li>
          <li v-else><RouterLink to="/login">Login</RouterLink></li>
        </ul>
      </div>
    </div>
  </nav>
</template>