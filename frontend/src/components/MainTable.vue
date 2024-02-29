<script setup>
import { request } from '@/utils/request';
import { onMounted, ref, watch } from 'vue';
import { useInfoStore } from '@/stores/infoStore';
import { storeToRefs } from 'pinia';
import { useToast } from 'vue-toastification';
import ActivityDetail from './ActivityDetail.vue';

const toast = useToast();
const infoStore = useInfoStore();
const { loginStatus } = storeToRefs(infoStore);

const sortBySub = ref(false);
const size = ref(20);
const Activities = ref([]);
const page = ref(1);
const selectedActivity = ref({});
const today = new Date().toISOString().split('T')[0];
let totalPage = 0;

const fetchActivities = async () => {
  if (sortBySub.value) {
    const res = await request.get(`/activity/week/subscribe/${today}/${page.value}/${size.value}`).then(res => res.data.data).catch(err => {
      console.log('err', err);
    });
    Activities.value = res.records;
  } else {
    const res = await request.get(`/activity/week/view/${today}/${page.value}/${size.value}`).then(res => res.data.data).catch(err => {
      console.log('err', err);
    });
    Activities.value = res.records;
    totalPage = res.pages;
  }
}

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

function selectChanged(e) {
  if (e.target.value === '按订阅量') {
    sortBySub.value = true;
  } else {
    sortBySub.value = false;
  }
}

function chooseActivity(activity) {
  selectedActivity.value = activity;
  request.put(`/view/${activity.id}`)
    .catch(err => {
      console.log('err', err);
    });
}
function subscribe(id) {
  request.put(`/auth/subscribe/${id}`)
    .then(() => {
      toast.success('订阅成功');
    })
    .catch(err => {
      console.log('err', err);
    });
}

onMounted(() => {
  fetchActivities();
})
watch(page, () => {
  fetchActivities();
})
watch(sortBySub, () => {
  fetchActivities();
})
</script>

<template>
<div class="flex flex-col space-y-2 lg:flex-row justify-between mx-4 lg:mx-10 mt-10">
  <label class="input input-bordered w-full lg:w-72 flex items-center gap-2">
    <input type="text" class="grow" placeholder="Search" />
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path fill-rule="evenodd" d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z" clip-rule="evenodd" /></svg>
  </label>
  <select class="select" @change="selectChanged">
    <option disabled selected>排序方式（默认按浏览量）</option>
    <option>按浏览量</option>
    <option>按订阅量</option>
  </select>
</div>

<dialog id="detail" class="modal">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Hello!</h3>
    <p class="py-4">{{ JSON.stringify(selectedActivity) }}</p>
    <div class="modal-action">
      <button v-if="loginStatus" class="btn btn-primary" @click="subscribe(selectedActivity.id)">订阅</button>
      <form method="dialog">
        <button class="btn">Close</button>
      </form>
    </div>
  </div>
  <form method="dialog" class="modal-backdrop">
    <button>close</button>
  </form>
</dialog>

<div class="hidden lg:block mx-10 my-6 overflow-x-auto">
  <table class="table table-zebra xl:table-lg">
    <thead>
      <tr>
        <th>活动名称</th>
        <th>活动日期</th>
        <th>活动信息</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="activity in Activities" :key="activity.id">
        <td class=" cursor-pointer" onclick="detail.showModal()" @click="chooseActivity(activity)">{{ activity.title }}</td>
        <td>{{ getFormatTime(activity) }}</td>
        <td>{{ activity.description }}</td>
      </tr>
    </tbody>
  </table>
  <div class="join" v-if="totalPage > 1">
    <button v-for="index in totalPage" :key="index" @click="page = index" :class="page === index ? 'btn btn-active join-item' : 'btn join-item'">{{ index }}</button>
  </div>
</div>

<div class="flex lg:hidden flex-col items-center mx-4 my-10 space-y-2">
  <div v-for="activity in Activities" :key="activity.id" class="flex flex-col items-center w-full ">
    <div class="flex flex-row justify-between w-full">
      <div class="grow self-start text-xl font-bold">{{ activity.title }}</div>
      <button v-if="loginStatus" class="btn btn-sm btn-primary self-end ml-2" @click="subscribe(selectedActivity.id)">订阅</button>
    </div>
    <div tabindex="0" class="collapse"> 
      <div class="collapse-title text-sm font-medium" @click="chooseActivity(activity)">
        详情
      </div>
      <div class="collapse-content"> 
        <ActivityDetail :activity="activity" />
      </div>
    </div>
  </div>
</div>
</template>