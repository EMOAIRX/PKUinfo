<template>
    <div class="inputBar">
        <el-input
            placeholder="请输入文章链接"
            prefix-icon="el-icon-upload"
            v-model="link"
            class="inputArea">
        </el-input>
        <el-button type="primary" class="submitButton" @click="submitHandler">提交</el-button>
    </div>
</template>

<script>
import request from '@/utils/request';

export default {
    name: 'FrontLinkSubmit',

    data() {
        return {
            link:""
        };
    },
    methods:{
        async submitHandler(){
            let requestBody = this.link;
            const config = {
                headers: {
                    'Content-Type': 'application/json'
                }
            }
            let res = await request.post("/user/submit/link",requestBody,config);
            if(res.data.code==1){
                console.log("成功");
            }else{
                console.log("失败");
            }
        }
    },
    mounted() {
        
    },
};
</script>

<style lang="less" scoped>
/deep/ .inputArea {
    display: inline-block;
    width: 600px;
}

.submitButton {
    margin-left: 20px;
    display: inline-block;
}

.inputBar {
    width: 100%;
    margin-top:120px;
    margin-bottom:120px;
    margin-left:calc(50% - 345px);
}

</style>