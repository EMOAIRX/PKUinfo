<script setup>
const { activity } = defineProps(['activity']);
import { map } from './constant'

const getFormatTime = (activity) => {
  let time = '';
  if (activity.startDate) {
    time = activity.startDate;
    if (activity.startTime) {
      time += ' ' + activity.startTime;
    }
    if (activity.endDate) {
      time += ' - ' + activity.endDate;
      if (activity.endTime) {
        time += ' ' + activity.endTime;
      }
    }
  }
  return time;
}
</script>

<template>
  <!-- 遍历对象 -->
  <div class="w-full grid grid-cols-3">
    <p class=" justify-self-start font-semibold" >活动时间</p>
    <p class=" justify-self-start col-span-2" >{{ getFormatTime(activity) }}</p>
  </div>
  <div class="w-full grid grid-cols-3" v-for="(value, key) in activity" :key="key">
    <p class=" justify-self-start font-semibold" v-if="key in map">{{ map[key] }}</p>
    <p class=" justify-self-start col-span-2" v-if="key in map">{{ value }}</p>
  </div>
</template>