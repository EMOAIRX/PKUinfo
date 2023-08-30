package pku.pkuinfo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import pku.pkuinfo.pojo.ActivityFeedbackInfo;
import pku.pkuinfo.pojo.ActivityInfo;
import pku.pkuinfo.pojo.Link;
import pku.pkuinfo.service.ActivityOperationService;
import pku.pkuinfo.service.ActivityProcessService;
import pku.pkuinfo.service.FeedbackOperationService;
import pku.pkuinfo.utils.Result;

import java.sql.Date;
import java.util.List;

@CrossOrigin(origins = "*")
@RestController
public class UserController {

    @Autowired
    private ActivityOperationService activityService;

    @Autowired
    private FeedbackOperationService feedbackService;

    @Autowired
    private ActivityProcessService activityProcessService;

    // 测试接口
    @RequestMapping("/api/test-string")
    public String test(){
        return "Hello, world";
    }


    // 请求路径示例：localhost:8080/api/user/activity/2023-07-10
    // 时间片大小为30天 起始日期为请求日期
    @GetMapping("/api/user/activity/{startDate}")
    public Result selectActivity(@PathVariable Date startDate){
        // System.out.println(startDate);
        List<ActivityInfo> activityList = activityService.select(startDate);
        return Result.success(activityList);
    }

    @PostMapping("/api/user/feedback/activity")
    public Result insertFeedbackActivity(@RequestBody ActivityFeedbackInfo feedbackInfo){
        Boolean res = feedbackService.insert(feedbackInfo);
        return Result.success();
    }

    @PostMapping("/api/user/submit/link")
    public Result processActivityLink(@RequestBody Link url){
        Boolean res = activityProcessService.processActivityLink(url);
        System.out.println("返回结果: " + res);
        return Result.auto(res,"发送成功","链接错误",null);
    }
}
