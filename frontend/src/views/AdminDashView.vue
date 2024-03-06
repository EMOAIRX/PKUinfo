<script setup>
import { request } from '@/utils/request'
import { ref } from 'vue'

const pathSelect = ref("0")
const path = ref("")
const response = ref("{}")

function updatePath() {
  switch (pathSelect.value) {
    case "1":
    case "2":
      path.value = "/admin/activity"
      break
    case "3":
    case "4":
      path.value = "/admin/user"
      break
  }
}

async function fetchApi() {
  if (pathSelect.value == "1" || pathSelect.value == "3" ) {
    await request.get(path.value).then((res) => {
      response.value = JSON.stringify(res.data,null,4)
    }).catch((err) => {
      console.log(err)
    })
  } else {
    await request.delete(path.value).then((res) => {
      response.value = JSON.stringify(res.data,null,4)
    }).catch((err) => {
      console.log(err)
    })
  }
}
</script>

<template>
<div class="mx-auto flex flex-col items-center space-y-4">
  <select class="select select-bordered w-full max-w-xs" v-model="pathSelect" @change="updatePath()">
    <option value="1">获取活动</option>
    <option value="2">删除活动</option>
    <option value="3">获取用户</option>
    <option value="4">删除用户</option>
  </select>
  <div class="flex flex-row items-center space-x-4">
    <input type="text" v-model="path" class="input w-full max-w-xs" />
    <button class="btn btn-neutral" @click="fetchApi">发起请求</button>
  </div>
  <textarea class="textarea w-[50vw] h-screen overflow-x-scroll" placeholder="响应" :value="response"></textarea>
</div>
</template>