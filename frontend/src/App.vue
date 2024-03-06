<script setup>
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue';
import { ArrowBigUpDash } from 'lucide-vue-next';
import { onMounted } from 'vue';
import { clickEffect } from './utils/firework';

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

onMounted(() => {
  // 当滑动距离大于100时显示返回顶部按钮
  window.onscroll = function () {
    let scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    if (scrollTop > 150) {
      document.querySelector('#backTop').style.display = 'block';
    } else {
      document.querySelector('#backTop').style.display = 'none';
    }
  }
  clickEffect();
});
</script>

<template>
  <header>
    <NavBar />
  </header>

  <div class="grow flex flex-col ">
    <RouterView />
    <!-- backtotop button  -->
    <div class="hidden fixed bottom-4 lg:bottom-12 right-4 cursor-pointer z-50" id="backTop">
      <button class="btn btn-circle btn-accent bg-opacity-70" @click="scrollToTop">
        <ArrowBigUpDash />
      </button>
    </div>
  </div>
</template>
