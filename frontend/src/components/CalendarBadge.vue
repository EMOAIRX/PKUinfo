<script setup>
import { request } from '@/utils/request';
import { ref, watch } from 'vue';
import { useToast } from 'vue-toastification';
import { useInfoStore } from '@/stores/infoStore';
import { storeToRefs } from 'pinia';

const toast = useToast();
const infoStore = useInfoStore();
const { ansTime,activityList } = storeToRefs(infoStore);

const props = defineProps({
  date: {
    type: String,
    required: true
  }
});
const emit = defineEmits(['changeDate']);
const records = ref([]);
const loading = ref(false);
const tot = ref(0);

// /activity/{startDate}/{endDate}/{start}/{size}
const fetchActivities = async () => {
  // 缓存
  let find = activityList.value.find(item => item.date == props.date);
  if (find) {
    records.value = find.records;
    tot.value = find.tot;
    return;
  }
  records.value = [];
  loading.value = true;
  tot.value = 0;
  const start = 1;
  const size = 3;
  let nowTime = new Date().getTime();
  const res = await request.get(`/activity/${props.date}/${props.date}/${start}/${size}/0`).then(res => res.data.data).catch(err => {
    toast.error('获取活动列表失败');
    console.log('err', err);
  });
  let endTime = new Date().getTime();
  ansTime.value.push(endTime - nowTime);
  activityList.value.push({
    date: props.date,
    records: res.records,
    tot: res.total
  });
  records.value = res.records;
  tot.value = res.total;
  loading.value = false;
}

watch(() => props.date, () => {
  fetchActivities();
},{
  immediate: true,
  deep: true
})
</script>

<template>
  <div class="flex-col items-center w-full h-full pb-12 mb-[-36px] mt-2 lg:flex hidden">
    <span v-if="loading" class="loading loading-dots loading-md"></span>
    <div v-for="activity in records " :key="activity.id" class="w-full grow space-y-0">
      <h3 class="text-xs border-l-4 mx-1 px-1 border-primary/60 ">{{ activity.title }}</h3>
    </div>
    <div v-if="records.length == 0 && !loading" class="w-full px-1 py-1">
      <h3>暂无活动</h3>
    </div>
    <div v-if="records.length && !loading" class="w-full px-1 py-1">
      <label for="detailinfo" class="text-sm cursor-pointer text-info font-semibold" @click="emit('changeDate')">等{{ tot }}项活动</label>
    </div> 
  </div>
  <div class=" lg:hidden h-[25px] w-full text-center bg-base-200">
    <span v-if="loading" class="loading loading-ball loading-sm"></span>
    <span v-if="tot> 0" class="font-extrabold text-primary">{{ tot }}</span>
    <span v-if="tot==0 && !loading" class="text-xs text-base-content/60">暂无</span>
  </div>
</template>