<script setup>
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue';

</script>

<template>
  <header>
    <NavBar />
  </header>

  <div class="grow flex flex-col">
    <RouterView />
  </div>
</template>
