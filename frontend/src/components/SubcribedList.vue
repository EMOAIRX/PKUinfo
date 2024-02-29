<script setup>
import { request } from '@/utils/request';
import ActivityDetail from './ActivityDetail.vue';
import { onMounted, ref } from 'vue';
import { useToast } from 'vue-toastification';
const toast = useToast();

const SubcribedList = ref([]);

const getSubscribed = async () => {
  const res = await request.get('/auth/activity/subscribed').then(res => res.data.data).catch(err => {
    console.log('err', err);
  });
  SubcribedList.value = res;
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
  <div v-for="activity in SubcribedList" :key="activity.id" class="flex flex-col items-center mx-4 my-10">
    <div class="flex flex-row justify-between w-full">
      <div class="grow self-start text-xl font-bold">{{ activity.title }}</div>
      <button class="btn btn-sm btn-primary self-end ml-2" @click="unsubscribe(activity.id)">取消订阅</button>
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
  <div v-if="SubcribedList.length === 0" class="flex justify-center items-center h-64">
    <p class="text-2xl font-bold">暂无订阅活动</p>
  </div>
</template>