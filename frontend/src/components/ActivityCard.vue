<script setup>
import { ref } from 'vue';
import { request } from '@/utils/request';
import { getFormatTime,getTagList } from './constant';

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
<div class="card w-full border-neutral border-2 relative bg-gradient-to-br from-base-100 to-base-200 shadow-lg">
  <div class="card-body py-6 px-6 items-center text-center z-10">
    <div class="w-full flex flex-col space-y-2 items-start">
      <h2 class="card-title text-start hyphens-auto">{{ activity.title }}</h2>
      <div v-if="activity.tags" class="flex flex-row items-center space-x-2">
        <span v-for="tag in getTagList(activity.tags)" :key="tag" class="badge badge-sm badge-outline badge-primary">{{ tag }}</span>
      </div>
    </div>

    <div v-if="!isShow" class="w-full flex flex-col items-start">
      <p class="justify-self-start text-start">活动详情：</p>
      <p class="text-start col-span-2 justify-self-start text-sm text-base-content/80 line-clamp-3">{{ activity.description }}</p>
    </div>

    <div v-if="isShow" class="w-full grid grid-cols-3">
      <div class="col-span-3 my-1 justify-self-start text-start text-sm">
        <h2 class="text-start text-base" >活动详情：</h2>
        <p class="text-base-content/80">{{ activity.description }}</p>
      </div>
      <p class="justify-self-start">举办单位：</p>
      <p class="col-span-2 text-start justify-self-start">{{ activity.college }}</p>
      <p class="justify-self-start" v-if="activity.address">活动地点：</p>
      <p class="col-span-2 text-start justify-self-start" v-if="activity.address">{{ activity.address }}</p>
      <p class="justify-self-start">活动时间：</p>
      <p class="col-span-2 text-start justify-self-start">{{ getFormatTime(activity) }}</p>
      <p class="justify-self-start" v-if="activity.info">活动信息：</p>
      <p class="col-span-2 justify-self-start" v-if="activity.info">{{ activity.info }}</p>
      <p class="justify-self-start" v-if="activity.link">推送链接：</p>
      <a class="col-span-2 justify-self-start text-wrap text-info" :href="activity.link" target="_blank" v-if="activity.link">访问链接</a>
    </div>

    <div class="flex flex-row w-full justify-between">
      <div class="self-start flex flex-col items-start text-sm">
      <span v-if="activity.view > 0">浏览量：{{ activity.view }}</span>
      <span v-if="activity.subscribe > 0">订阅数：{{ activity.subscribe }}</span>
    </div>
    <div class="self-end" v-if="isShow">
      <span class="text-info" @click="isShow=false">收起详情</span>
    </div>
    <div class="self-end" v-else>
      <span class="text-info" @click="viewMore">查看详情</span>
    </div>
    </div>
  </div>
</div>
</template>