<template>
    <div>
        <!-- 条件选择栏部分 -->
        <el-row :gutter="20">
            <!-- 1. 日期选择器 -->
            <el-col :offset="0" :span="4">
                <el-date-picker
                    v-model="pickerTime"
                    type="daterange"
                    unlink-panels
                    range-separator="至"
                    start-placeholder="开始日期"
                    end-placeholder="结束日期"
                    :picker-options="pickerOptions"
                    :default-time="['00:00:00', '00:00:00']"
                    @change="selectDateRange">
                </el-date-picker>
            </el-col>
            
            <!-- 2. 条件选择器 -->
            <el-col :span="4" :offset="16">
                <el-select
                    v-model="selectedValues"
                    multiple
                    collapse-tags
                    placeholder="请选择">
                    <el-option
                        v-for="item in selectionOptions"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>
            </el-col>
            <!-- 可以添加额外的column -->
        </el-row>
        <!-- 列表部分 -->
        <el-table
        :data="currentListPage"
        style="width: 100%"
        v-loading="activityListLoading">
            <el-table-column type="expand">
                <template slot-scope="props">
                    <el-descriptions title="活动信息" :column="2" :colon="false">
                        <template slot="extra">
                            <el-button type="primary" icon="el-icon-edit" size="mini" @click="feedbackHandler(props.row)">反馈</el-button>
                        </template>
                        <el-descriptions-item label="活动名称">{{ props.row.title }}</el-descriptions-item>
                        <!-- 占位？ -->
                        <el-descriptions-item label="">{{  }}</el-descriptions-item>
                        <el-descriptions-item label="活动日期">{{ props.row.startDate }}</el-descriptions-item>
                        <el-descriptions-item label="活动时间">{{ props.row.startTime + "-" + props.row.endTime }}</el-descriptions-item>
                        <el-descriptions-item label="活动地点">{{ props.row.address }}</el-descriptions-item>
                        <el-descriptions-item label="举办学院">{{ props.row.college }}</el-descriptions-item>
                        <el-descriptions-item label="活动信息">{{ props.row.description }}</el-descriptions-item>
                    </el-descriptions>
                </template>
            </el-table-column>
            <el-table-column
                label="活动名称"
                prop="title">
            </el-table-column>
            <el-table-column
                label="活动日期">
                <template slot-scope="{row}">
                    {{ row.startDate + " " + row.startTime + "-" + row.endTime }}
                </template>
            </el-table-column>
            <el-table-column
                label="活动信息">
                <template slot-scope="{row}">
                    {{ row.description }}
                </template>
            </el-table-column>
        </el-table>
        <!-- 分页部分 -->
        <el-row :gutter="20">
            <el-col :offset="16" :span="8">
                <!-- @current-change="handleCurrentChange"未用上-->
                <el-pagination
                    :current-page.sync="currentPage"
                    :page-size="10"
                    layout="total, prev, pager, next, jumper"
                    :total="totalInfoCount"
                    :hide-on-single-page="true">
                </el-pagination>
            </el-col>
        </el-row>
        <!-- 对话框 用于获取反馈 -->
        <FeedbackDialog :visible="dialogTableVisible" :info="feedbackInfo" @update="dialogTableVisible=$event"></FeedbackDialog>
    </div>
</template>

<script>
import { mapState } from 'vuex';
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';
import FeedbackDialog from './FeedbackDialog.vue';

export default {
    name: 'FrontActivityList',
    
    data() {
        return {
            // 日期选择器部分
            pickerOptions: {
                // 控制可选范围
                disabledDate(time) {
                    // 暂定截止时间最大为三个月
                    return (time.getTime() < new Date(new Date().toLocaleDateString()) || time.getTime() > new Date(Date.parse(new Date().toLocaleDateString()) + 1000*60*60*24*90 ));
                },
                // 快捷导航部分
                shortcuts: [{
                    text: '最近一周',
                    onClick(picker) {
                        let start = new Date(new Date().toLocaleDateString());
                        let end = new Date(new Date().toLocaleDateString());
                        end.setTime(end.getTime() + 3600 * 1000 * 24 * 7);
                        picker.$emit('pick', [start, end]);
                    }
                }, {
                    text: '最近一个月',
                    onClick(picker) {
                        let start = new Date(new Date().toLocaleDateString());
                        let end = new Date(new Date().toLocaleDateString());
                        end.setTime(end.getTime() + 3600 * 1000 * 24 * 30);
                        picker.$emit('pick', [start, end]);
                    }
                }, {
                    text: '最近三个月',
                    onClick(picker) {
                        let start = new Date(new Date().toLocaleDateString());
                        let end = new Date(new Date().toLocaleDateString());
                        end.setTime(end.getTime() + 3600 * 1000 * 24 * 90);
                        picker.$emit('pick', [start, end]);
                    }
                }],
            },
            // 多选选项
            selectionOptions: [{
                value: '西风骑士团',
                label: '西风骑士团'
            }, {
                value: 'B',
                label: 'B'
            }, {
                value: 'C',
                label: 'C'
            }, {
                value: 'D',
                label: 'D'
            }, {
                value: 'E',
                label: 'E'
            }],
            // 当前已选选项
            selectedValues: [],
            // 当前页码
            currentPage:1,
            // 当前选择日期
            pickerTime:[new Date(new Date().toLocaleDateString()),new Date(Date.parse(new Date().toLocaleDateString())+1000*60*60*24*30)],
            // Drawer是否可见
            dialogTableVisible:false,
            // 反馈信息
            feedbackInfo:null,
        };
    },
    
    mounted() {
        // Deprecated
        // this.$watch(
        //     ()=>{
        //         return this.activityArray;
        //     },
        //     (newVal)=>{
        //         let flatArray =[];
        //         newVal.forEach((item) => {
        //             if (item != null) {
        //                 flatArray = [...flatArray, ...item];
        //             }
        //         })
        //         this.activityList = flatArray;
        //     },{
        //         deep:true,
        //         immediate:true,
        //     }
        // )
    },
    
    methods: {
        ...mapActions(["asyncUpdateActivityArray"]),
        // handleCurrenyChange暂时无用
        // handleCurrentChange(val) {
        //     console.log(`当前页: ${val}`);
        // },
        async selectDateRange(){
            let limitedRange = this.dateLimit;
            if(this.pickerTime==null || undefined){
                return;
            }

            if(this.pickerTime[1].getTime()>limitedRange){   
                this.asyncUpdateActivityArray(this.pickerTime[1]);
            }else{
                return;
            }
        },
        feedbackHandler(info){
            this.dialogTableVisible = true;
            this.feedbackInfo = info;
        },
    },
    
    computed:{
        ...mapState(["activityListLoading"]),
        ...mapGetters(["dateLimit","nextIndex","flattedArray"]),
        totalInfoCount(){
            if(this.currentActivityList==null || undefined){
                return 0;
            }
            return this.currentActivityList.length;
        },
        // 页面内部的列表数据，根据选择器改变的
        currentActivityList(){
            if(this.pickerTime == null || this.flattedArray == null || this.flattedArray == undefined){
                return [];
            }else{
                let invalidDateArray = this.flattedArray.some((item)=>{
                    return item!=null;
                })

                if(!invalidDateArray){
                    return [];
                }
            }
            // 数组展开
            let activityList = this.flattedArray;

            // 日期选择
            let begin = this.pickerTime[0];
            let end = this.pickerTime[1];
            let result = activityList.filter(currentValue=>{
                return Date.parse(currentValue.startDate) >= begin && Date.parse(currentValue.startDate)<= end;
            });

            // 复选框选择
            // demo版本 暂未插入选择字段
            if(this.selectedValues.length===0){
                return result;
            }
            return result.filter(currentValue=>{
                return this.selectedValues.includes(currentValue.college);
            })
        },
        // 分页展示的数据，根据页面内部列表改变
        currentListPage(){
            return this.currentActivityList.slice((this.currentPage - 1)*10,this.currentPage*10);
        }
    },

    components:{
        FeedbackDialog,
    }
};
</script>

<style lang="less" scoped>
.demo-table-expand {
    font-size: 0;
}
.demo-table-expand label {
    width: 90px;
    color: #869fc2;
}
.demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
}

/deep/ .el-descriptions{
    padding-left:25px;
    padding-right:25px;
}
</style>