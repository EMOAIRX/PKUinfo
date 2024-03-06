<script setup>
import { request } from '@/utils/request';
import ActivityDetail from './ActivityDetail.vue';
import { onMounted, ref } from 'vue';
import { useToast } from 'vue-toastification';
const toast = useToast();

const SubcribedList = ref([]);
const loading = ref(false);

const getSubscribed = async () => {
  loading.value = true;
  const res = await request.get('/auth/activity/subscribed').then(res => res.data.data).catch(err => {
    console.log('err', err);
  });
  SubcribedList.value = res;
  loading.value = false;
}

// DELETE /auth/subscribe/{activityId}
const unsubscribe = async (activityId) => {
  await request.delete(`/auth/subscribe/${activityId}`).then(() => {
    getSubscribed();
    toast.success('取消订阅成功');
  }).catch(err => {
    console.log('err', err);
  });
}

onMounted(() => {
  getSubscribed();
})
</script>

<template>
<div class="flex flex-col items-center mx-auto px-4 max-w-screen-sm my-10">
  <div v-for="activity in SubcribedList" :key="activity.id" class="flex flex-col items-center">
    <p class=" self-start text-xs lg:text-sm">{{ activity.startDate }}</p>
    <div class="flex flex-row justify-between w-full">
      <div class="grow self-start text-lg font-bold">{{ activity.title }}</div>
      <button class="btn btn-xs lg:btn-sm btn-primary self-end ml-2" @click="unsubscribe(activity.id)">取消订阅</button>
    </div>
    <div tabindex="0" class="collapse"> 
      <div class="collapse-title text-sm font-medium">
        详情
      </div>
      <div class="collapse-content"> 
        <ActivityDetail :activity="activity" />
      </div>
    </div>
  </div>
  <div v-if="SubcribedList.length === 0 && !loading" class="flex justify-center items-center h-64">
    <p class="text-xl font-bold">暂无订阅活动</p>
  </div>
</div>
</template>