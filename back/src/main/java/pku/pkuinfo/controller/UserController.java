package pku.pkuinfo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.web.bind.annotation.*;
import pku.pkuinfo.pojo.ActivityFeedbackInfo;
import pku.pkuinfo.pojo.ActivityInfo;
import pku.pkuinfo.pojo.WeekActivityInfo;
import pku.pkuinfo.pojo.Link;
import pku.pkuinfo.service.ActivityOperationService;
import pku.pkuinfo.service.ActivityProcessService;
import pku.pkuinfo.service.FeedbackOperationService;
import pku.pkuinfo.utils.Result;
import java.util.Calendar;

import java.sql.Date;
import java.util.List;

@CrossOrigin(origins = "*")
@RestController
public class UserController {
    private static int counter = 0;
    @Autowired
    private ActivityOperationService activityService;

    @Autowired
    private FeedbackOperationService feedbackService;

    @Autowired
    private ActivityProcessService activityProcessService;

    /**
     * 测试接口
     * @return Hello, world
     */
    @RequestMapping("/api/test-string")
    public String test(){
        return "Hello, world";
    }

    /**
     * 请求路径示例：localhost:8080/api/user/activity/2023-07-10
     * 时间片大小为30天 起始日期为请求日期
     * @param startDate 起始日期
     * @return result
     */
    @GetMapping("/api/user/activity/{startDate}")
    public Result selectActivity(@PathVariable Date startDate){
        this.counter++;
        List<ActivityInfo> activityList = activityService.select(startDate);
        for (ActivityInfo activity : activityList) {
            Calendar cal = Calendar.getInstance();
            cal.setTime(activity.getStartDate());
            cal.add(Calendar.DATE, 1);
            activity.setStartDate(new Date(cal.getTimeInMillis()));
            cal.setTime(activity.getEndDate());
            cal.add(Calendar.DATE, 1);
            activity.setEndDate(new Date(cal.getTimeInMillis()));
        }
        return Result.success(activityList);
    }

    /**
     * 增加计数
     * @return success
     */
    @GetMapping("/api/user/addCounter")
    public Result addCounter(){
        counter++;
        return Result.success(counter);
    }

    /**
     * 获取计数
     * @return result
     */
    @GetMapping("/api/user/getCounter")
    public Result getCounter(){
        return Result.success(counter);
    }

    /**
     * 请求路径示例：localhost:8080/api/user/activity/week
     * @return result
     */
    @GetMapping("/api/user/activity/week")
    public Result selectWeekActivity(){
        Calendar calendar = Calendar.getInstance();
        Date startDate = new Date(calendar.getTimeInMillis());
        List<WeekActivityInfo> activityList = activityService.weekselect(startDate);
        return Result.success(activityList);
    }

    /**
     * 添加反馈信息
     * @param feedbackInfo 反馈信息
     * @return result
     */
    @PostMapping("/api/user/feedback/activity")
    public Result insertFeedbackActivity(@RequestBody ActivityFeedbackInfo feedbackInfo){
        Boolean res = feedbackService.insert(feedbackInfo);
        return Result.success();
    }

    /**
     * 添加活动链接
     * @param url 目标URL
     * @return result
     */
    @PostMapping("/api/user/submit/link")
    public Result processActivityLink(@RequestBody Link url){
        System.out.println("接收到链接: " + url);
        new Thread(() -> {
            Boolean res = activityProcessService.processActivityLink(url);
            System.out.println("处理结果: " + res);
        }).start();
        System.out.println("是否接受链接成功 " + url);
        return Result.success();
    }

}
