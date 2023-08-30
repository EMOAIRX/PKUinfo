<template>
	<div>
		<el-container>
			<!-- Header部分 可以考虑整点图片什么的？ -->
			<el-header>Header</el-header>
			<el-main>
				<MainMenu></MainMenu>
			</el-main>
			<!-- Footer部分 后期备案等信息可以写在这里-->
			<el-footer>Footer</el-footer>
		</el-container>
	</div>
</template>

<script>
import { mapActions } from 'vuex'
import MainMenu from './components/MainMenu.vue';

export default {
	// 页面创建阶段先初始化活动列表
	// 范围为一个月内活动
	created(){
		let date = Date.parse(new Date().toLocaleDateString()) + 1000 * 60 * 60 * 24 * 30;
		this.asyncUpdateActivityArray(date);
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
