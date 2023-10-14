package pku.pkuinfo.controller;

import org.springframework.beans.factory.annotation.Autowired;
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
import java.util.ArrayList;
import java.util.HashMap;
// import java.io.FileWriter;
// import java.io.IOException;

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

    // 测试接口
    @RequestMapping("/api/test-string")
    public String test(){
        return "Hello, world";
    }


    // 请求路径示例：localhost:8080/api/user/activity/2023-07-10
    // 时间片大小为30天 起始日期为请求日期

    @GetMapping("/api/user/activity/{startDate}")
    public Result selectActivity(@PathVariable Date startDate){
        // this.counter++;
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


    @GetMapping("/api/user/activity/talking/{text}/{startDate}/{endDate}")
    public Result talking(@PathVariable String text, @PathVariable Date startDate, @PathVariable Date endDate){
        List<ActivityInfo> activityList = activityService.search(text, startDate, endDate);
        String appendix = "";
        Integer length = activityList.size();
        if (length > 10) {
            length = 10;
        }
        for (int i = 0; i < length; i++) {
            appendix += activityList.get(i).getDescription();
        }
        String answer = activityService.talking(text,appendix);
        return Result.success(answer);
    }


    @GetMapping("/api/user/activity_with_tags/{startDate}")
    public Result selectActivity_with_tags(@PathVariable Date startDate){
        this.counter++;
        List<ActivityInfo> activityList = activityService.select(startDate);
        List<String> tags = new ArrayList<>();
        for (ActivityInfo activity : activityList) {
            Calendar cal = Calendar.getInstance();
            cal.setTime(activity.getStartDate());
            cal.add(Calendar.DATE, 1);
            activity.setStartDate(new Date(cal.getTimeInMillis()));
            cal.setTime(activity.getEndDate());
            cal.add(Calendar.DATE, 1);
            activity.setEndDate(new Date(cal.getTimeInMillis()));
            tags.add(activityService.query_tag(activity));
        }
        return Result.success(
            new HashMap<String, Object>(){{
                put("activityList", activityList);
                put("tags", tags);
            }}
        );
    }
    @GetMapping("/api/user/activity_with_tags/{startDate}/{endDate}")
    public Result selectActivity_with_tags_2(@PathVariable Date startDate, @PathVariable Date endDate){
        this.counter++;
        List<ActivityInfo> activityList = activityService.select(startDate, endDate);
        List<String> tags = new ArrayList<>();
        for (ActivityInfo activity : activityList) {
            Calendar cal = Calendar.getInstance();
            cal.setTime(activity.getStartDate());
            cal.add(Calendar.DATE, 1);
            activity.setStartDate(new Date(cal.getTimeInMillis()));
            cal.setTime(activity.getEndDate());
            cal.add(Calendar.DATE, 1);
            activity.setEndDate(new Date(cal.getTimeInMillis()));
            tags.add(activityService.query_tag(activity));
        }
        return Result.success(
            new HashMap<String, Object>(){{
                put("activityList", activityList);
                put("tags", tags);
            }}
        );
    }

    // 三个参数 text , startDate , endDate
    @GetMapping("/api/user/activity/search/{text}/{startDate}/{endDate}")
    public Result searchActivity(@PathVariable String text, @PathVariable Date startDate, @PathVariable Date endDate){
        List<ActivityInfo> activityList = activityService.search(text, startDate, endDate);
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

    @GetMapping("/api/user/activity/search_tag/{text}/{startDate}/{endDate}")
    public Result searchActivity_tag(@PathVariable String text, @PathVariable Date startDate, @PathVariable Date endDate){
        List<ActivityInfo> activityList = activityService.search_tag(text, startDate, endDate);
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


    @GetMapping("/api/user/addCounter")
    public Result addCounter(){
        counter++;
        return Result.success(counter);
    }

    @GetMapping("/api/user/getCounter")
    public Result getCounter(){
        return Result.success(counter);
    }

    @PostMapping("/api/user/feedback/activity")
    public Result insertFeedbackActivity(@RequestBody ActivityFeedbackInfo feedbackInfo){
        Boolean res = feedbackService.insert(feedbackInfo);
        return Result.success();
    }

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
    // @PostMapping("/api/user/submit_ui/link")
    // public Result UIprocessActivityLink(@RequestBody Link url){
    //     System.out.println("接收到链接: " + url);
    //     try {
    //         FileWriter writer = new FileWriter("received.txt", true);
    //         writer.write(url + "\n");
    //         writer.close();
    //     } catch (IOException e) {
    //         e.printStackTrace();
    //     }
    //     return Result.success();
    // }

    // @PostMapping("/api/user/query_submited")
    // public Result UIprocessActivityLink(@RequestBody Link url){
    //     System.out.println("接收到链接: " + url);
    //     try {
    //         FileWriter writer = new FileWriter("received.txt", true);
    //         writer.write(url + "\n");
    //         writer.close();
    //     } catch (IOException e) {
    //         e.printStackTrace();
    //     }
    //     return Result.success();
    // }

}
