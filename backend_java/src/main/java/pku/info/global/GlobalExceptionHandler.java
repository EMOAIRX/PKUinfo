package pku.info.global;

import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.web.HttpRequestMethodNotSupportedException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import pku.info.common.Result;

import java.sql.SQLIntegrityConstraintViolationException;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(SQLIntegrityConstraintViolationException.class)
    public Result SQLIntegrityConstraintViolationException(Exception e){
        e.printStackTrace();//打印堆栈中的异常信息
        return Result.error(400, "UNVALIDATED_INPUT");
    }

    @ExceptionHandler(DataIntegrityViolationException.class)
    public Result DataIntegrityViolationException(Exception e){
        e.printStackTrace();//打印堆栈中的异常信息
        return Result.error(400,"UNVALIDATED_INPUT");
    }

    @ExceptionHandler(HttpRequestMethodNotSupportedException.class)
    public Result UnsupportedRequestMethodException(Exception e){
        return Result.error(405,e.getMessage());
    }

    // 其他类型异常
    @ExceptionHandler(Exception.class) //指定能够处理的异常类型
    public Result BaseException(Exception e){
        e.printStackTrace();//打印堆栈中的异常信息
        return Result.error(500, "INTERNAL_SERVER_ERROR");
    }
}