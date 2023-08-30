<template>
    <div>
        <el-calendar v-loading="activityListLoading" ref="calendar">
            <template
                slot="dateCell"
                slot-scope="{data}">
                <!-- date 属性暂时没用上 &&  ref="cell"似乎用不了 -->
                <div class="cell" v-if="isInRange(data.day)" @click="dateClickHandler(data)">
                    <p :class="data.isSelected ? 'is-selected' : ''" class="cell-title">
                        <!-- 取决于后端传过来的数据格式 date以/作为分隔 data.day以-作为分隔 -->
                        {{ data.day.split('-').slice(2).join('-') }} 
                    </p>
                    <span v-if="getActivityCount(data.day)!=0" :class="data.isSelected ? 'is-selected' : ''" class="cell-content"> 
                        {{ getActivityContent(data.day) }} 
                        {{ getActivityCount(data.day)==1?"":"等" }}
                    </span>
                    <span v-if="getActivityCount(data.day)!=0" :class="data.isSelected ? 'is-selected' : ''" class="cell-content">
                        {{ "共计 " + getActivityCount(data.day) + " 个活动" }}
                    </span>
                    <span v-else class="cell-content" :class="data.isSelected ? 'is-selected' : ''">
                        今日暂无活动
                    </span>
                </div>
                <div class="forbid cell" v-else @click="dateClickHandler(data)">
                    <p :class="data.isSelected ? 'is-selected' : ''" class="cell-title">
                        <!-- 取决于后端传过来的数据格式 date以/作为分隔 data.day以-作为分隔 -->
                        {{ data.day.split('-').slice(2).join('-') }} 
                    </p>
                    <span class="cell-content">
                        不在时间范围内
                    </span>
                </div>
            </template>
        </el-calendar>
        <el-drawer
            :title="drawerDateTitle"
            :visible.sync="drawer"
            :with-header="false"
            size="45%">
            <span class="drawer-header">
                <!-- {{ drawerDate.split('-').slice(1).join('-') }} -->
                {{ drawerDateTitle }}
            </span>
            <!-- 时间线组件 -->
            <el-timeline :reverse="true" v-if="this.dateObject[drawerDate]!=undefined">
                <el-timeline-item
                    v-for="(activity, index) in this.dateObject[drawerDate]"
                    :key="index"
                    :timestamp="activity.startDate + ' ' + activity.startTime + '-' + activity.endTime"
                    placement="top">
                    <!-- 活动内容组件 -->
                    <el-collapse>
                        <el-collapse-item :title="activity.title">
                            <el-row :gutter="20" v-for="(value,key,innerIndex) in activity"
                            :key="innerIndex">
                                <el-col :span="8">
                                    <p>{{ key }}</p>
                                </el-col>
                                <el-col :span="16">
                                    <p>{{ value }}</p>
                                </el-col>
                            </el-row>
                        </el-collapse-item>
                    </el-collapse>
                </el-timeline-item>
            </el-timeline>
            <div v-else class="drawer-content">
                <div v-if="isInRange(drawerDate)">
                    今日暂无活动
                </div>
                <div v-else>
                    不在统计范围内
                </div>
            </div>
        </el-drawer>
    </div>
</template>

<script>
import { mapState } from 'vuex';
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';

export default {
    name: 'FrontCalendar',

    data() {
        return {
            drawer:false,
            drawerDate:"",
            activityList:[],
        };
    },
    mounted() {
        // 更新后台数据
        // 监听当前页面最大选择日期是否已经加载，未加载的情况进行加载
        this.$watch(
            ()=>{
                return this.$refs.calendar.$children[1].rows[5][6];
            },
            (newVal)=>{
                if(newVal.type=='next'){
                    let nextMonth = this.$refs.calendar.$children[1].nextMonthDatePrefix;
                    let day = newVal.text.toString().length<2?'0'+newVal.text:newVal.text;
                    // console.log(nextMonth+'-'+day);

                    let targetTimeRange = Date.parse(nextMonth+'-'+day);
                    let currentTimeLimit = this.dateLimit;

                    // console.log(targetTimeRange,currentTimeLimit);
                    if(targetTimeRange > currentTimeLimit && targetTimeRange < this.standardMaxDate){
                        console.log("Calandar-immediate");
                        this.asyncUpdateActivityArray(targetTimeRange);
                    }else if(targetTimeRange<currentTimeLimit){
                        console.log("日历信息范围已经在列表中");
                    }else{
                        console.log("日期超出信息范围无法加载");
                    }
                }
            },{
                deep:true,
                immediate:true,
            }
        )
    },

    created(){

    },

    methods: {
        ...mapActions(["asyncUpdateActivityArray"]),
        // 计算当前日期活动数目
        getActivityCount(date){
            if(this.dateObject[date]==null||undefined){
                return 0;
            }
            return this.dateObject[date].length;
        },
        getActivityContent(date){
            if(this.dateObject[date]==null||undefined){
                return "";
            }
            return this.dateObject[date][0]["title"];
        },
        isInRange(date){
            let begin = this.standardLocalDate;
            let end = this.dateLimit;
            date = Date.parse(date);
            if(date < begin || date > end){
                return false;
            }else{
                return true;
            }
        },
        dateClickHandler(data){
            if(data.type=='prev-month'||data.type=='next-month'){
                return;
            }
            let date = data.day;
            this.drawerDate = date;
            this.drawer = true;
        }
    },

    computed:{
        ...mapState(["activityListLoading","standardMaxDate","standardLocalDate"]),
        ...mapGetters(["dateLimit","nextIndex","flattedArray"]),
        dateObject(){
            let obj = new Object();
            if(this.flattedArray==null||undefined){
                return obj;
            }
            for(let i=0;i<this.flattedArray.length;++i){
                if(obj[this.flattedArray[i].startDate] == null || undefined ){
                    obj[this.flattedArray[i].startDate] = [];
                    obj[this.flattedArray[i].startDate].push(this.flattedArray[i]);
                }else{
                    obj[this.flattedArray[i].startDate].push(this.flattedArray[i]);
                }
            }
            return obj;
        },
        drawerDateTitle(){
            if(this.drawerDate==""){
                return "";
            }
            let dateStringArray = new Date(this.drawerDate).toLocaleDateString().split('/');
            return dateStringArray[1]+"月"+dateStringArray[2]+"日活动信息";
        }
    },
};
</script>

<style lang="less" scoped>
.is-selected {
    color: #1989FA;
}

/deep/ .el-calendar-day:hover {
    background-color:transparent !important;
}

/deep/ td:hover {
    background-color: #F2F8FE !important;
}

/deep/.el-calendar {
    td {
        height:100%;
    }
    .el-calendar__body {

        .next,
        .prev {
            color: #C0C4CC;

            .forbid {
                color: #C0C4CC;
            }
        }
        .el-calendar-day{
            display: block;
            // width: 100%;
            min-height: 85px;
            height: 100%;
            padding:0px;

            .cell {
                display: block;
                width: 100%;
                height: 100%;

                p {
                    margin:0px;
                }

                .cell-title {
                    padding-top:8px;
                    padding-left:8px;
                    padding-bottom: 12px;

                    font-size: 18px;
                }

                .cell-content {
                    padding-bottom:8px;
                    padding-left:8px;

                    font-size: 14px;

                    display: block;
                }
            }
        }
    }
}

.forbid {
    color:rgb(79, 79, 79);
}

/deep/ .drawer-header{
    display: block;
    font-size: 20px;

    padding-top:18px;
    padding-left:18px;
    padding-bottom: 18px;
}

/deep/ .drawer-content {
    div {
        padding-top:12px;
        margin-left:18px;
    }
}
</style>