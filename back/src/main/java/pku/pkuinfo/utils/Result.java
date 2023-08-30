package pku.pkuinfo.utils;
public class Result {
    private Integer code ;//1 成功 , 0 失败
    private String message; //提示信息
    private Object data; //数据 date

    public Result() {
    }
    public Result(Integer code, String message, Object data) {
        this.code = code;
        this.message = message;
        this.data = data;
    }
    public Integer getCode() {
        return code;
    }
    public void setCode(Integer code) {
        this.code = code;
    }
    public String getMsg() {
        return message;
    }
    public void setMsg(String message) {
        this.message = message;
    }
    public Object getData() {
        return data;
    }
    public void setData(Object data) {
        this.data = data;
    }

    public static Result success(Object data){
        return success("success", data);
    }
    public static Result success(){
        return success("success");
    }
    public static Result success(String msg, Object data){
        return new Result(1, msg, data);
    }
    public static Result success(String msg){
        return new Result(1, msg, null);
    }
    public static Result error(String msg){
        return new Result(0, msg, null);
    }

    public static Result auto(Boolean code,String success,String fail,Object data){
        if(code){
            return success(success,data);
        }else{
            return error(fail);
        }
    }

    @Override
    public String toString() {
        return "Result{" +
                "code=" + code +
                ", message='" + message + '\'' +
                ", data=" + data +
                '}';
    }
}
