<script setup>
const { activity } = defineProps(['activity']);
import { map,getFormatTime } from './constant'
import { useToast } from 'vue-toastification';
const toast = useToast();

function gotourl(url) {
  if (url){
    window.open(url);
  } else {
    toast.warning('链接为空');
  }
}
</script>

<template>
  <!-- 遍历对象 -->
<div class="space-y-2 text-sm">
  <div class="w-full grid grid-cols-4">
    <p class=" justify-self-start font-semibold" >活动时间</p>
    <p class=" justify-self-start col-span-3" >{{ getFormatTime(activity) }}</p>
  </div>
  <p class="font-semibold" >活动描述：<span class="font-normal text-[12px]">{{ activity["description"] }}</span></p>
  <div class="w-full grid grid-cols-4" v-for="(value, key) in map" :key="key">
    <p class=" justify-self-start font-semibold" v-if="activity[key]">{{ value }}</p>
    <p class=" justify-self-start col-span-3 text-wrap" v-if="activity[key]">{{ activity[key] }}</p>
  </div>
  <div class="w-full grid grid-cols-4">
    <p class=" justify-self-start font-semibold" >推送链接</p>
    <!-- 访问链接 -->
    <p class=" justify-self-start cursor-pointer col-span-3 text-wrap text-info" @click="gotourl(activity['link'])" >访问链接</p>
  </div>
</div>
</template>