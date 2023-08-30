<template>
    <div class="canvas-box">
        <canvas
            id="cont-canvas"
            :width="contentWidth"
            :height="contentHeight" 
            @click="changeCode">
        </canvas>
    </div>
</template>

<script>
export default {
    name: "IdentifyCode",
    data() {
        return {
            identifyCode: "",
        };
    },
    props: {
        identifyCodes: {
            //验证码从该字段中抽取生成
            type: String,
            default: "0123456789qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM",
        },
        fontSizeMin: {
            // 字体最小值
            type: Number,
            default: 25,
        },
        fontSizeMax: {
            // 字体最大值
            type: Number,
            default: 35,
        },
        backgroundColorMin: {
            // 验证码图片背景色最小值
            type: Number,
            default: 200,
            //   default: 1000
        },
        backgroundColorMax: {
            // 验证码图片背景色最大值
            type: Number,
            default: 220,
            //   default: 1000
        },
        dotColorMin: {
            // 背景干扰点最小值
            type: Number,
            default: 60,
        },
        dotColorMax: {
            // 背景干扰点最大值
            type: Number,
            default: 120,
        },
        contentWidth: {
            //容器宽度
            type: Number,
            default: 120,
        },
        contentHeight: {
            //容器高度
            type: Number,
            default: 48,
        },
    },
    watch: {
        identifyCode() {
            this.drawPic();
        },
    },
    mounted() {
        this.drawPic();
        this.makeCode(this.identifyCodes, 4);
    },
    methods: {
        // 生成一个随机数
        randomNum(min, max) {
            return Math.floor(Math.random() * (max - min) + min);
        },
        // 生成一个随机的颜色
        randomColor(min, max) {
            let r = this.randomNum(min, max);
            let g = this.randomNum(min, max);
            let b = this.randomNum(min, max);
            return "rgb(" + r + "," + g + "," + b + ")";
        },
        drawPic() {
            let canvas = document.getElementById("cont-canvas");
            let ctx = canvas.getContext("2d");
            ctx.textBaseline = "bottom";
            // 绘制背景
            ctx.fillStyle = this.randomColor(
            this.backgroundColorMin,
            this.backgroundColorMax
            );
            ctx.fillRect(0, 0, this.contentWidth, this.contentHeight);
            // 绘制文字
            for (let i = 0; i < this.identifyCode.length; i++) {
                this.drawText(ctx, this.identifyCode[i], i);
            }
            this.drawLine(ctx);
            this.drawDot(ctx);
        },
        drawText(ctx, txt, i) {
            ctx.fillStyle = this.randomColor(50, 160); //随机生成字体颜色
            ctx.font =
            this.randomNum(this.fontSizeMin, this.fontSizeMax) + "px SimHei"; //随机生成字体大小
            let x = (i + 1) * (this.contentWidth / (this.identifyCode.length + 1));
            let y = this.randomNum(this.fontSizeMax, this.contentHeight - 5);
            var deg = this.randomNum(-30, 30);
            // 修改坐标原点和旋转角度
            ctx.translate(x, y);
            ctx.rotate((deg * Math.PI) / 180);
            ctx.fillText(txt, 0, 0);
            // 恢复坐标原点和旋转角度
            ctx.rotate((-deg * Math.PI) / 180);
            ctx.translate(-x, -y);
        },
        drawLine(ctx) {
            // 绘制干扰线
            for (let i = 0; i < 4; i++) {
                ctx.strokeStyle = this.randomColor(100, 200);
                ctx.beginPath();
                ctx.moveTo(
                this.randomNum(0, this.contentWidth),
                this.randomNum(0, this.contentHeight)
                );
                ctx.lineTo(
                this.randomNum(0, this.contentWidth),
                this.randomNum(0, this.contentHeight)
                );
                ctx.stroke();
            }
        },
        drawDot(ctx) {
            // 绘制干扰点
            for (let i = 0; i < 30; i++) {
                ctx.fillStyle = this.randomColor(0, 255);
                ctx.beginPath();
                ctx.arc(
                this.randomNum(0, this.contentWidth),
                this.randomNum(0, this.contentHeight),
                1,
                0,
                2 * Math.PI
                );
                ctx.fill();
            }
        },
        /*切换验证码start*/
        changeCode() {
            this.drawPic();
            this.identifyCode = "";
            this.makeCode(this.identifyCodes, 4);
        },
        makeCode(e, n) {
            for (let i = 0; i < n; i++) {
                this.identifyCode += e[this.randomNum(0, e.length)];
            }
            // console.log("code = ", this.identifyCode);
            this.$emit("update:changeCode", this.identifyCode);
        }
        /*切换验证码end*/
    },
};
</script>

<style scoped></style>