<script setup>
import { request } from '@/utils/request';
import { onMounted,ref, watch } from 'vue';
import { useToast } from 'vue-toastification';

const toast = useToast();

const props = defineProps({
  date: {
    type: String,
    required: true
  }
});
const emit = defineEmits(['changeDate']);
const records = ref([]);
const loading = ref(false);

// /activity/{startDate}/{endDate}/{start}/{size}
const fetchActivities = async () => {
  records.value = [{id:1,title: "加载中..."}];
  loading.value = true;
  const start = 1;
  const size = 1000;
  const res = await request.get(`/activity/${props.date}/${props.date}/${start}/${size}`).then(res => res.data.data).catch(err => {
    toast.error('获取活动列表失败');
    console.log('err', err);
  });
  records.value = res.records;
  loading.value = false;
}

onMounted(() => {
  // 如果屏幕宽度大于1024px,请求数据
  if (window.innerWidth > 1024) {
    fetchActivities();
  }
})

watch(() => props.date, () => {
  fetchActivities();
},{
  immediate: true,
  deep: true
})
</script>

<template>
  <div class="flex flex-col items-center w-full">
    <div v-for="activity in records.slice(0, 3)" :key="activity.id" class="w-full bg-base-200 border-l-4 mx-1 px-1 py-1 border-secondary/80">
      <h3>{{ activity.title }}</h3>
    </div>
    <div v-if="records.length >3" class="w-full mx-1 px-1 py-1 ">
      <h3>...</h3>
    </div>
    <div v-if="records.length == 0" class="w-full px-1 py-1">
      <h3>暂无活动</h3>
    </div>
    <div v-if="records.length && !loading" class="w-full px-1 py-1">
      <label for="detailinfo" class="text-sm cursor-pointer" @click="emit('changeDate')">查看更多</label>
    </div> 
  </div>
</template>