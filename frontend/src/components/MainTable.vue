<script setup>
import { request } from '@/utils/request';
import { onMounted, ref, watch } from 'vue';
import { useInfoStore } from '@/stores/infoStore';
import { storeToRefs } from 'pinia';
import { useToast } from 'vue-toastification';
import { tag_list,getFormatTime,getTagList } from './constant';
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
const tag = ref(0);
const loading = ref(false);
let totalPage = ref(0);

const fetchActivities = async () => {
  loading.value = true;
  Activities.value = [];
  if (sortBySub.value) {
    const res = await request.get(`/activity/week/subscribe/${today}/${page.value}/${size.value}/${tag.value}`).then(res => res.data.data).catch(err => {
      console.log('err', err);
    });
    Activities.value = res.records;
    totalPage.value = res.pages;
  } else {
    const res = await request.get(`/activity/week/view/${today}/${page.value}/${size.value}/${tag.value}`).then(res => res.data.data).catch(err => {
      console.log('err', err);
    });
    Activities.value = res.records;
    totalPage.value = res.pages;
  }
  loading.value = false;
}

function selectChanged(e) {
  if (e.target.value === '按订阅量') {
    sortBySub.value = true;
  } else {
    sortBySub.value = false;
  }
}

async function chooseActivity(activity) {
  selectedActivity.value = activity;
  await request.put(`/view/${activity.id}`)
    .catch(err => {
      console.log('err', err);
    });
}
async function subscribe(id) {
  await request.put(`/auth/subscribe/${id}`)
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
watch(tag, () => {
  fetchActivities();
})
</script>

<template>
<!-- 头部选择框 -->
<div class="mx-auto mt-2">
  <p class="text-xs text-base-content/80 ">显示未来七天内的活动</p>
</div>
<div class="flex flex-col space-y-2 lg:flex-row justify-between mx-4 lg:mx-10 mt-2">
  <label class="input input-bordered w-full lg:w-72 flex items-center gap-2">
    <input type="text" class="grow" placeholder="Search" />
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path fill-rule="evenodd" d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z" clip-rule="evenodd" /></svg>
  </label>
  <div class="flex flex-row w-full flex-wrap space-x-4 lg:justify-end">
    <select class="select select-sm lg:select-md select-bordered" @change="selectChanged">
      <option disabled selected>排序方式（默认按浏览量）</option>
      <option>按浏览量</option>
      <option>按订阅量</option>
    </select>
    <select class="select select-sm lg:select-md select-bordered" v-model="tag">
      <option disabled selected value="0">标签</option>
      <option v-for="(item,index) in tag_list" :key="index" :value="index">{{ item }}</option>
    </select>
  </div>
</div>

<!-- 大屏，详情对话框 -->
<dialog id="detail" class="modal">
  <div class="modal-box">
    <h3 class="font-bold text-xl">{{ selectedActivity.title }}</h3>
    <div v-if="selectedActivity.tags" class="flex flex-row space-x-2 shrink-0 mt-2">
      <span v-for="tag in getTagList(selectedActivity.tags)" :key="tag" class="badge badge-outline badge-primary">{{ tag }}</span>
    </div>
    <div class="pt-4">
      <ActivityDetail :activity="selectedActivity" />
    </div>
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

<!-- 大屏，表格 -->
<div class="hidden lg:flex flex-col items-center mx-10 mb-10 overflow-x-auto">
  <table class="table table-zebra xl:table-lg">
    <thead>
      <tr>
        <th>活动名称</th>
        <th>活动标签</th>
        <th>活动日期</th>
        <th>活动信息</th>
      </tr>
    </thead>
    <tbody>
      <tr v-if="loading">
        <td colspan="3" class="text-center">
          <span class="loading loading-dots loading-lg"></span>
        </td>
      </tr>
      <tr v-for="activity in Activities" :key="activity.id">
        <td class=" cursor-pointer font-semibold" onclick="detail.showModal()" @click="chooseActivity(activity)">{{ activity.title }}</td>
        <td class="text-sm space-y-1">
          <div v-if="activity.tags">
            <span v-for="tag in getTagList(activity.tags)" :key="tag" class="badge badge-sm badge-outline badge-primary">{{ tag }}</span>
          </div>
        </td>
        <td class="text-sm text-base-content/80">{{ getFormatTime(activity) }}</td>
        <td class="text-sm">{{ activity.description }}</td>
      </tr>
    </tbody>
  </table>
  <div class="join mt-4" v-if="totalPage > 1">
    <button v-for="index in totalPage" :key="index" @click="page = index" :class="page === index ? 'btn btn-active join-item' : 'btn join-item'">{{ index }}</button>
  </div>
</div>

<!-- 小屏，列表 -->
<div class="flex lg:hidden flex-col items-center my-10 space-y-2">
  <span v-if="loading" class="loading loading-infinity loading-lg"></span>
  <div v-for="activity in Activities" :key="activity.id" class="flex flex-col items-center w-full ">
    <div class="flex flex-row justify-between items-center w-full pl-4 pr-2">
      <div class="flex flex-col space-y-2">
        <div class="self-start hyphens-auto text-lg font-bold">{{ activity.title }}</div>
        <div v-if="activity.tags" class="flex flex-row space-x-2 shrink-0">
          <span v-for="tag in getTagList(activity.tags)" :key="tag" class="badge badge-sm badge-outline badge-primary">{{ tag }}</span>
        </div>
      </div>
      <div class="flex flex-row items-center shrink-0 ml-1">
        <button v-if="loginStatus" class="btn btn-xs btn-primary" @click="subscribe(activity.id)">订阅</button>
      </div>
    </div>
    <div tabindex="0" class="collapse"> 
      <div class="collapse-title text-sm text-info font-medium px-4 mt-[-8px]" @click="chooseActivity(activity)">
        查看详情
      </div>
      <div class="collapse-content mt-[-8px] mb-3"> 
        <ActivityDetail :activity="activity" />
      </div>
    </div>
  </div>
  <div class="join" v-if="totalPage > 1">
    <button v-for="index in totalPage" :key="index" @click="page = index" :class="page === index ? 'btn btn-active join-item btn-sm' : 'btn join-item btn-sm'">{{ index }}</button>
  </div>
</div>
</template>