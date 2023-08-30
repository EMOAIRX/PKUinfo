import Vue from 'vue'
import Vuex from 'vuex'
import request from '@/utils/request'

Vue.use(Vuex);

const ONEDAY = 1000 * 60 * 60 * 24;

export default new Vuex.Store({
	state: {
		// activityList的loading标识符
		activityListLoading: true,
		// 当日日期
		standardLocalDate: Date.parse(new Date().toLocaleDateString()),
		// 每份为30天
		activityArray: [null, null, null, null, null, null],
		// 毫秒数
		standardMaxDate: Date.parse(new Date().toLocaleDateString()) + ONEDAY * 90,
	},
	getters: {
		// 当前数据范围
		dateLimit(state, getters) {
			let index = getters.nextIndex;
			if (index == 0) {
				return state.standardLocalDate - 1;
			}
			return state.standardLocalDate + index * ONEDAY * 30;
		},
		nextIndex(state) {
			return state.activityArray.indexOf(null);
		},
		flattedArray(state) {
			let flatArray = [];
			state.activityArray.forEach((item) => {
				if (item != null) {
					flatArray = [...flatArray, ...item];
				}
			})
			// console.log("FlatArray: ", flatArray);
			return flatArray;
		}
	},
	mutations: {
		// 更新活动数组
		updateActivityArray(state, instruction) {
			state.activityArray[instruction.index] = instruction.res;

			state.activityArray = JSON.parse(JSON.stringify(state.activityArray));
			// console.log(state.activityArray);
			// console.log("更新活动数组Index: ", instruction.index, " 数据: ", instruction.res, "数据量", instruction.res.length);
		},
		setActivityLoadingMark(state, newMark) {
			state.activityListLoading = newMark;
		},
	},
	actions: {
		async asyncUpdateActivityArray(store, date) {
			let requestDate = date;

			if (requestDate > store.getters.dateLimit) {
				store.commit('setActivityLoadingMark', true);

				let offset = Math.ceil((date - store.state.standardLocalDate) / (30 * ONEDAY));

				for (let index = store.getters.nextIndex; index < offset; ++index) {
					if (store.state.activityArray[index] != null) {
						continue;
					}
					// 日期格式YYYY/M/D
					let targetStartDate = (new Date(store.state.standardLocalDate + index * 30 * ONEDAY)).toLocaleDateString();
					console.log(index, targetStartDate);

					// 日期格式化
					// convert 8-30-2023 to 2023/08/30
					let targetStartDateStrArr = targetStartDate.split('/');
					let targetStartDateStr = targetStartDateStrArr[2] + '-' + targetStartDateStrArr[0] + '-' + targetStartDateStrArr[1];
					if (targetStartDateStrArr[1].length < 2) {
						targetStartDateStrArr[1] = '0' + targetStartDateStrArr[1];
					}
					if (targetStartDateStrArr[2].length < 2) {
						targetStartDateStrArr[2] = '0' + targetStartDateStrArr[2];
					}
					console.log(targetStartDateStr);

					let res = await request.get('/user/activity/' + targetStartDateStr);
					console.log(res);
					let ins = {
						res: res.data.data,
						index: index
					}
					store.commit("updateActivityArray", ins);
				}
				store.commit('setActivityLoadingMark', false);

				// console.log("asyncUpdateActivityArray Finished");
			}
		}
	}
})
