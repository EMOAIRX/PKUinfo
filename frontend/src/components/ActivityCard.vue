<script setup>
import { ref } from 'vue';
import { request } from '@/utils/request';

const { activity } = defineProps(['activity'])
const isShow = ref(false)

async function viewMore() {
  isShow.value = true
  request.put(`/view/${activity.id}`)
    .catch(err => {
      console.log('err', err);
    });
}

</script>

<template>
<div class="card w-full border-neutral border-2 relative bg-gradient-to-br from-base-200 to-accent/10 shadow-lg">
  <div class="absolute glass opacity-30 w-full h-full z-0 rounded-2xl"></div>
  <div class="card-body py-6 px-6 items-center text-center z-10">
    <div class="w-full flex justify-between items-center">
      <h2 class="card-title">{{ activity.title }}</h2>
      <span class="badge badge-accent">{{ activity.type }}</span>
    </div>
    <div class="w-full grid grid-cols-3">
      <p class="justify-self-start">简介：</p>
      <p class=" col-span-2 justify-self-start">{{ activity.description }}</p>
    </div>
      <div v-if="isShow" class="w-full grid grid-cols-3">
        <p class="justify-self-start" v-if="activity.college">举办单位：</p>
        <p class="col-span-2 justify-self-start" v-if="activity.college">{{ activity.college }}</p>
        <p class="justify-self-start" v-if="activity.address">活动地点：</p>
        <p class="col-span-2 justify-self-start" v-if="activity.address">{{ activity.address }}</p>
        <p class="justify-self-start">活动时间：</p>
        <p class="col-span-2 justify-self-start">{{ activity.startDate + ' ' + activity.startTime }} <span v-if="activity.endDate">- {{ activity.endDate + ' ' + activity.endTime }}</span></p>
        <p class="justify-self-start" v-if="activity.info">活动信息：</p>
        <p class="col-span-2 justify-self-start" v-if="activity.info">{{ activity.info }}</p>
        <p class="justify-self-start" v-if="activity.link">推送链接：</p>
        <a class="col-span-2 justify-self-start" :href="activity.link" target="_blank" v-if="activity.link">{{ activity.link }}</a>
      </div>
    <div class="flex flex-row w-full justify-between">
      <div class="self-start flex flex-col items-start text-sm">
      <span v-if="activity.view > 0">浏览量：{{ activity.view }}</span>
      <span v-if="activity.subscribe > 0">订阅数：{{ activity.subscribe }}</span>
    </div>
    <div class="self-end" v-if="isShow">
      <span class="text-info" @click="isShow=false">Hide More</span>
    </div>
    <div class="self-end" v-else>
      <span class="text-info" @click="viewMore">Show More</span>
    </div>
    </div>
  </div>
</div>
</template>