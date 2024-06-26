package pku.pkuinfo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import pku.pkuinfo.pojo.ActivityFeedbackInfo;
import pku.pkuinfo.pojo.ActivityInfo;
import pku.pkuinfo.pojo.Admin;
import pku.pkuinfo.pojo.RecordInfo;
import pku.pkuinfo.service.ActivityOperationService;
import pku.pkuinfo.service.AuthenticationService;
import pku.pkuinfo.service.FeedbackOperationService;
import pku.pkuinfo.service.RecordOperationService;
import pku.pkuinfo.utils.Result;

import java.util.List;
import java.util.Map;

//TODO 管理员端的鉴权 √
//TODO 缓存 √
//TODO 管理员端的功能
@CrossOrigin(origins = "*")
@RestController
public class AdminController {
    @Autowired
    private ActivityOperationService activityService;

    @Autowired
    private FeedbackOperationService feedbackService;

    @Autowired
    private RecordOperationService recordService;

    @Autowired
    private AuthenticationService authenticationService;

    /**
     * 添加指定活动
     * @param info 活动信息
     * @return result
     */
    @PostMapping ("/api/admin/activity")
    public Result insertActivityInformation(@RequestBody ActivityInfo info){
        // 对象数据
        Integer affected = activityService.insert(info);
        if(affected==1){
            return Result.success("插入成功");
        }else if(affected<1){
            return Result.error("插入失败");
        }else{
            return Result.error("Fatal Error咯");
        }
    }

    /**
     * 删除指定活动
     * 有一说一这里不符合Restful接口风格，主要是配合WebFilter
     * @param id 活动信息对应的ID
     * @return result
     */
    @DeleteMapping("api/admin/activity/delete/{id}")
    public Result deleteActivityInformation(@PathVariable Integer id){
        Integer affected = activityService.delete(id);
        if(affected==1){
            return Result.success("删除成功");
        }else if(affected<1){
            return Result.error("删除失败");
        }else{
            return Result.error("Fatal Error咯");
        }
    }

    //@GetMapping("/api/admin/activityfeedback")
    //public List<ActivityFeedbackInfo> selectActivityFeedbackInformation(){
    //    return feedbackService.select();
    //}

    /**
     * 获取反馈列表
     * 未对列表内容长度做检查，可能为空
     * @return 反馈列表
     */
    @GetMapping("/api/admin/activityfeedback")
    public Result selectActivityFeedbackInformation(){
        return Result.success("获取成功",feedbackService.select());
    }

    /**
     * 接收URL请求 转发至Python端
     * @param targeturl 目标URL
     * @return 成功
     */
    @PostMapping("/api/admin/activityurl/{targeturl}")
    public Result urlTransmit(@PathVariable String targeturl){
        System.out.println(targeturl);
        return Result.success();
    }

    /**
     *
     * @param info 记录数据
     * @return result
     */
    @PostMapping("/api/admin/record")
    public Result insertActivityRecord(@RequestBody RecordInfo info){
        // 对象数据
        Boolean res = recordService.insert(info);
        if(res){
            return Result.success();
        }else{
            return Result.error("插入失败");
        }
    }

    /**
     *
     * @param info 记录数据
     * @return result
     */
    @PostMapping("/api/admin/check")
    public Result checkActivityRecord(@RequestBody RecordInfo info){
        // 对象数据
        Boolean res = recordService.check(info);
        if(res){
            return Result.success("数据已存在");
        }else{
            //这边最好别用 error，最好还是success。
            return Result.error("数据未重复");
        }
    }

    /**
     * 登录接口
     * @param admin 管理员账户与密码
     * @return result 成功会返回一个token
     */
    @PostMapping("/api/admin/login")
    public Result login(@RequestBody Admin admin){
        String res = authenticationService.login(admin);
        if(res!= null && !res.equals("")){
            return Result.success("登陆成功", Map.of("token",res));
        }else{
            return Result.error("账号或密码错误");
        }
    }
}
