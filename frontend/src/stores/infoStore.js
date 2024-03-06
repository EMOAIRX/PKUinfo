import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useInfoStore = defineStore('infoStore', () => {
  const loginStatus = ref(false)
  const ansTime = ref([])
  const activityList = ref([])
  if (sessionStorage.getItem('auth')) {
    loginStatus.value = true
  }
  if (localStorage.getItem('auth')) {
    loginStatus.value = true
    sessionStorage.setItem('auth',localStorage.getItem('auth'))
  }
  return { loginStatus,ansTime,activityList }
})
