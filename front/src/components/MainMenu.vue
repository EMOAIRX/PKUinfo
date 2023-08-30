<template>
    <div>
        <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane name="first">
                <span slot="label"><i class="el-icon-document"></i> 活动概览</span>
                <ActivityList></ActivityList>
            </el-tab-pane>
            <el-tab-pane name="second">
                <span slot="label"><i class="el-icon-date"></i> 活动日历</span>
                <Calendar></Calendar>
            </el-tab-pane>
            <el-tab-pane name="third">
                <span slot="label"><i class="el-icon-upload"></i> 链接上传</span>
                <LinkSubmit></LinkSubmit>
            </el-tab-pane>
            <!-- 后续可以添加别的选项卡 -->
            <!-- <el-tab-pane label="角色管理" name="third">角色管理</el-tab-pane> -->
            <!-- <el-tab-pane label="定时任务补偿" name="fourth">定时任务补偿</el-tab-pane> -->
        </el-tabs>
    </div>
</template>

<script>
import ActivityList from './ActivityList.vue';
import Calendar from './Calendar.vue';
import LinkSubmit from './LinkSubmit.vue';

export default {
    name: 'FrontMainMenu',
    
    data() {
        return {
            activeName: 'first'
        };
    },
    
    mounted() {
        
    },
    
    methods: {
        // 暂时还没啥用
        handleClick(tab, event) {
            tab;
            event;
            // console.log(tab , event);
        }
    },

    components:{
        ActivityList,
        Calendar,
        LinkSubmit,
    }
};
</script>

<style lang="less" scoped>

</style>