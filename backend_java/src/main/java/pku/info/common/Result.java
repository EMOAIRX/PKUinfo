package pku.info.common;

import lombok.Data;

@Data
public class Result {
    private Integer code ;//状态响应码
    private String message; //相应信息
    private Object data; //数据

    public Result() {}
    public Result(Integer code, String message, Object data) {
        this.code = code;
        this.message = message;
        this.data = data;
    }

    public static Result success(Object data){
        return success("success", data);
    }
    public static Result success(){
        return success("success", null);
    }
    public static Result success(String msg, Object data){
        return new Result(200, msg, data);
    }
    public static Result error(Integer code, String msg){
        return new Result(code, msg, null);
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
