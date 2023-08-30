<template>
    <div>
        <el-dialog title="信息反馈" 
            :visible.sync="dialogTableVisible" 
            center
            :destroy-on-close="true"
            @close="clearFeedbackData()">
            <el-form label-position="right" 
                label-width="120px" 
                :rules="formRules"
                :model="formData"
                ref="dataForm">
                <el-form-item label="活动名称">
                    <el-input :value="info==null?'':info.title" :disabled="true"></el-input>
                </el-form-item>
                <el-form-item label="反馈类型" prop="selection">
                    <el-select v-model="formData.selection" placeholder="请选择">
                        <el-option
                            v-for="item in selectOptions"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="反馈信息" prop="inputText">
                    <el-input type="textarea" v-model="formData.inputText"></el-input>
                </el-form-item>
                <el-form-item label="验证码" prop="validationCode">
                    <el-input v-model="formData.validationCode"></el-input>
                </el-form-item>
                <el-form-item>
                    <VerificationCode @update:changeCode="getCode"></VerificationCode>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <!-- @click="clearFeedbackData()"  -->
                <el-button 
                    size="mini"
                    @click="clearFeedbackData()">
                    取 消</el-button>
                <!-- @click="dialogTableVisible = false"  -->
                <el-button type="primary" 
                    @click="submitForm('dataForm')"
                    size="mini">
                    确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import VerificationCode from './VerificationCode.vue';
import request from '@/utils/request';

export default {
    name: 'PkuinfoFeedbackDialog',
    props:{
        visible:{
            require:true,
            type:Boolean,
        },
        info:{
            require:true,
            type:null||Object,
        }
    },
    computed:{
        dialogTableVisible:{
            get(){
                return this.visible;
            },
            set(val){
                this.$emit("update",val);
            }
        }
    },
    data() {
        return {
            verificationCode:"",
            selectOptions:[{
                    value: '信息错误',
                    label: '信息错误'
                }, {
                    value: '其他',
                    label: '其他'
                },
            ],
            formRules:{
                selection:[
                    { required: true, message: '请选择反馈类型', trigger: 'change' }
                ],
                inputText:[
                    { required: true, message: '请填写相关信息', trigger: 'blur' }
                ],
                validationCode:[
                    { validator: this.codeValidation, trigger: 'blur' }
                ],
            },
            formData:{
                inputText:"",
                validationCode:"",
                selection:"",
            },
        };
    },
    mounted() {
        
    },
    methods: {
        getCode(val) {
            this.verificationCode = val;
            // console.log(val);
        },
        // 传ref
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    // alert('submit!');
                    this.feedbackSubmitHandler();
                } else {
                    return false;
                }
            });
        },
        codeValidation(rule, value, callback){
            if (value === '') {
                callback(new Error('请输入验证码'));
            } else if (this.verificationCode !== value) {
                callback(new Error('验证码错误!'));
            } else {
                callback();
            }
        },
        async feedbackSubmitHandler(){

            const data = {
                "targetActivityId": this.info.id,
                "type": this.formData.selection,
                "description":this.formData.inputText
            }
            const config = {
                headers: {
                    'Content-Type': 'application/json'
                }
            }
            // 先生成数据对象再clear
            this.clearFeedbackData();

            let res = await request.post("/user/feedback/activity", data, config);
            // 检查返回值 做相应提示
            console.log(res);
        },
        clearFeedbackData(){
            console.log("clearFeedbackData()执行")
            this.dialogTableVisible = false;
            for(let key in this.formData){
                this.formData[key] = "";
            }
        }
    },
    components:{
        VerificationCode,
    }
};
</script>

<style lang="less" scoped>
/deep/ .el-dialog {
    .el-dialog__body {
        padding-top:18px;
        padding-bottom: 12px;
    }
}
</style>