<template>
	<div>
		<el-container>
			<!-- Header部分 可以考虑整点图片什么的？ -->
			<el-header> star: https://github.com/EMOAIRX/PKUinfo                                   	 contact with wechat EMOAIRX  [求转发求推广] </el-header>
			<el-main>
				<MainMenu></MainMenu>
			</el-main>
			<el-footer>Counter: {{ Math.floor(counterData / 4) }}</el-footer>
			<!-- Footer部分 后期备案等信息可以写在这里-->
			<!-- <el-footer>Footer</el-footer> -->
		</el-container>
	</div>
</template>

<script>
import { mapActions } from 'vuex'
import MainMenu from './components/MainMenu.vue';

export default {
	data() {
		return {
			counterData: 0,
		}
	},
	// 页面创建阶段先初始化活动列表
	// 范围为一个月内活动
	created(){
		let date = Date.parse(new Date().toLocaleDateString());// + 1000 * 60 * 60 * 24 * 30;
		this.asyncUpdateActivityArray(date);
		
		//请使用get方法，访问 https://pkuinfo.lcpu.dev/api.user/getCounter 获取一个值，作为counterData的初值
		this.counterData = 0;
		let url = "https://pkuinfo.lcpu.dev/api/user/getCounter";
		let xhr = new XMLHttpRequest();
		xhr.open("GET", url, true);
		//从response.data中获取数据
		xhr.onload = function () {
			let data = JSON.parse(xhr.responseText);
			this.counterData = data.data;
		}.bind(this);
		xhr.send();
	},
	components:{
		MainMenu,
	},
	methods:{
		...mapActions(["asyncUpdateActivityArray"]),
	}
}
</script>

<style lang="less" >
body {
	margin:0px;
}

html,
body,
#app {
    height: 100%;
}
</style>