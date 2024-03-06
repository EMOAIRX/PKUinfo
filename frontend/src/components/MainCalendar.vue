<script setup>
import { computed, onMounted, ref,watch } from 'vue';
import { ChevronRight, ChevronLeft } from 'lucide-vue-next';
import moment from 'moment';
import { request } from '@/utils/request';
import { useToast } from 'vue-toastification';
import CalendarBadge from './CalendarBadge.vue';
import ActivityCard from './ActivityCard.vue';
import ActivityDetail from './ActivityDetail.vue';
import { useInfoStore } from '@/stores/infoStore';
import { checkDate,getTagList } from './constant';
import { storeToRefs } from 'pinia';
const infoStore = useInfoStore();
const { loginStatus,ansTime } = storeToRefs(infoStore);

const toast = useToast();

const today = moment().startOf('day');
const weekdays = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"];
const colStartClasses = [
  "",
  "col-start-2",
  "col-start-3",
  "col-start-4",
  "col-start-5",
  "col-start-6",
  "col-start-7",
];

const firstDayOfMonth = ref(moment().startOf('month'));
const currentMonth = ref(moment(today).format("MMMM-yyyy"));
const selectedDate = ref(today);
const records = ref([]);
const loading = ref(false);

async function chooseActivity(activity) {
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

const allDaysInMonth = ()=> {
  let start = moment(firstDayOfMonth.value).startOf('week')
  let end = moment(moment(firstDayOfMonth.value).endOf('month')).endOf('week')
  var days = [];
  var day = start;
  while (day <= end) {
    days.push(day.toDate());
    day = day.clone().add(1, 'd');
  }
  return days
}

const fetchActivities = async () => {
  records.value = [];
  const startDate = moment(selectedDate.value).startOf('day').format('YYYY-MM-DD');
  const endDate = moment(selectedDate.value).endOf('day').format('YYYY-MM-DD');
  const start = 1;
  const size = 1000;
  loading.value = true;
  const res = await request.get(`/activity/${startDate}/${endDate}/${start}/${size}/0`).then(res => res.data.data).catch(err => {
    toast.error('获取活动列表失败');
    console.log('err', err);
  });
  records.value = res.records;
  loading.value = false;
}

watch(selectedDate, () => {
  fetchActivities();
})
onMounted(() => {
  fetchActivities();
})

const avgTime = computed(() => {
  return (ansTime.value.reduce((a, b) => a + b, 0) / ansTime.value.length).toFixed(2);
})

const isToday = (date) => {
  return moment(date).isSame(moment(), 'day');
}

const isDifferentMonth = (date) => {
  return moment(date).month() != moment(firstDayOfMonth.value).month() 
}

const getPrevMonth = () => {
  const firstDayOfPrevMonth = moment(firstDayOfMonth.value).add(-1, 'M').startOf('month');
  firstDayOfMonth.value = firstDayOfPrevMonth;
  currentMonth.value = moment(firstDayOfPrevMonth).format("MMM-yyyy");
};

const getCurrentMonth = () => {
  const firstDayOfCurrMonth = moment().startOf('month');
  firstDayOfMonth.value = firstDayOfCurrMonth;
  currentMonth.value = moment(firstDayOfCurrMonth).format("MMM-yyyy");
};

const getNextMonth = () => {
  const firstDayOfNextMonth = moment(firstDayOfMonth.value).add(1, 'M').startOf('month');
  firstDayOfMonth.value = firstDayOfNextMonth;
  currentMonth.value = moment(firstDayOfNextMonth).format("MMM-yyyy");
};

const changeDate = (date) => {
  selectedDate.value = date;
}
</script>

<template>
  <!-- 活动列表对话框 -->
  <input type="checkbox" id="detailinfo" class="modal-toggle" />
  <div class="modal" role="dialog">
    <div class="modal-box">
      <h3 class="text-xl font-semibold">{{ moment(selectedDate).format('YYYY-MM-DD') }}</h3>
      <span v-if="loading" class="loading loading-infinity loading-lg"></span>
      <div class="flex flex-col space-y-0 pt-10">
        <div v-for="activity in records" :key="activity.id" class="flex flex-col items-center w-full">
        <div class="flex flex-row justify-between w-full ml-4 mb-[-8px]">
          <div class="flex flex-col space-y-2">
            <div class="grow self-start text-lg font-semibold">{{ activity.title }}</div>
            <div v-if="activity.tags" class="flex flex-row space-x-2 shrink-0 ">
              <span v-for="tag in getTagList(activity.tags)" :key="tag" class="badge badge-outline badge-primary">{{ tag }}</span>
            </div>
          </div>
          <div class="flex flex-row space-x-2 items-center shrink-0 ml-1">
            <button v-if="loginStatus && checkDate(activity.startDate)" class="btn btn-sm btn-primary btn-outline" @click="subscribe(activity.id)">订阅</button>
          </div>
        </div>
        <div tabindex="0" class="collapse"> 
          <div class="collapse-title text-base font-medium text-primary" @click="chooseActivity(activity)">
            查看详情
          </div>
          <div class="collapse-content mt-[-8px] mb-6"> 
            <ActivityDetail :activity="activity" />
          </div>
        </div>
      </div>
      </div>
    </div>
    <label class="modal-backdrop" for="detailinfo">关闭</label>
  </div>

<!-- 网站测速 -->
<div class="w-full flex flex-row space-x-4 lg:space-x-10 justify-center items-center mt-2 text-xs">
  <p class=" text-base-content/80">已请求{{ ansTime.length }}次</p>
  <!-- 平均，保留到小数点后1位 -->
  <p class="text-base-content/80">平均{{ avgTime }}ms</p>
  <!-- 改变颜色，表示网络状况 -->
  <p class="text-base-content/80" :class="{'text-success': avgTime < 1000, 'text-warning': avgTime > 1000 && avgTime < 2000,'text-error': avgTime > 2000}">{{ avgTime < 1000 ? '网络良好' : (avgTime < 2000 ? '网络较差' : '网络很差') }}</p>
</div>

  <!-- 主日历 -->
<div class="w-full bg-base-100 p-4 lg:pt-0 rounded-lg">
  <div class="flex  justify-between gap-0 sm:gap-4">
    <p class="font-semibold text-2xl w-32 lg:w-56">
      {{moment(firstDayOfMonth).format("MM").toString()}}
      <span class="font-normal text-base pl-2">{{ moment(firstDayOfMonth).format("YYYY").toString() }}</span>
    </p>

    <div class="flex flex-row items-center">
      <button class="btn btn-square btn-sm btn-ghost"  @click="getPrevMonth">
        <ChevronLeft class="w-4 h-4" />
      </button>
      <button class="btn btn-sm btn-ghost normal-case" @click="getCurrentMonth">
      回到当月</button>
      <button class="btn btn-square btn-sm btn-ghost" @click="getNextMonth">
        <ChevronRight class="w-4 h-4" />
      </button>
    </div>
  </div>        
  
  <div class="my-4 divider" />

  <div class="grid grid-cols-7 gap-6 sm:gap-12 place-items-center">
    <div class="text-xs capitalize" v-for="day in weekdays" :key="day">{{day}}</div>
  </div>
        
  <div class="grid grid-col auto-rows-auto mt-1 place-items-center items-stretch">
    <div v-for="(day, idx) in allDaysInMonth()" :key="idx" :class="colStartClasses[moment(day).day().toString()] + ' border border-solid border-base-content/50 w-full h-16 lg:h-auto'">
      <p class="flex items-center justify-center h-8 w-8 rounded-full mx-auto lg:mx-1 font-semibold mt-1 text-sm cursor-pointer "
      :class="{'bg-primary text-primary-content': isToday(day), 'text-base-content/50': isDifferentMonth(day),'bg-accent text-accent-content': moment(day).isSame(selectedDate, 'day')}"
      @click="selectedDate = day">
        {{ moment(day).format('D') }}
      </p>
        <CalendarBadge :date="moment(day).format('YYYY-MM-DD')"  @change-date="changeDate(day)" />
    </div>
  </div>

  <!-- 小屏日历卡片 -->
  <div class="flex flex-col lg:hidden items-center py-10 space-y-2">
    <span v-if="loading" class="loading loading-dots loading-lg"></span>
    <div v-for="record in records" :key="record.id">
      <ActivityCard :activity="record" />
    </div>
  </div>
  <div class="lg:hidden" v-if="records.length == 0 && !loading">
    <h3 class="text-center text-2xl font-semibold mt-2">暂无活动</h3>
  </div>

</div>
</template>