package pku.info.activity.controller;

import jakarta.annotation.Resource;
import org.springframework.web.bind.annotation.*;
import pku.info.activity.entity.Activity;
import pku.info.activity.service.ActivityService;
import pku.info.common.Conf;
import pku.info.common.Result;

import java.sql.Date;

@RestController
@CrossOrigin(origins = "*")
public class ActivityController {
    @Resource
    private ActivityService activityService;

    // 获取活动
    @GetMapping("/activity/week/view/{startDate}/{start}/{size}")
    public Result getWeekActivityByViewWithSize(@PathVariable Date startDate, @PathVariable int start, @PathVariable int size) {
        return activityService.getWeekByView(startDate, start, size);
    }

    @GetMapping("/activity/week/view/{startDate}/{start}")
    public Result getWeekActivityByView(@PathVariable Date startDate, @PathVariable int start) {
        return activityService.getWeekByView(startDate, start, Conf.PageSize);
    }

    @GetMapping("/activity/week/subscribe/{startDate}/{start}/{size}")
    public Result getWeekActivityBySubscribeWithSize(@PathVariable Date startDate, @PathVariable int start, @PathVariable int size) {
        return activityService.getWeekBySubscribe(startDate, start, size);
    }

    @GetMapping("/activity/week/subscribe/{startDate}/{start}")
    public Result getWeekActivityBySubscribe(@PathVariable Date startDate, @PathVariable int start) {
        return activityService.getWeekBySubscribe(startDate, start, Conf.PageSize);
    }

    @GetMapping("/activity/days/view/{startDate}/{start}/{size}")
    public Result getDaysActivityByViewWithSize(@PathVariable Date startDate, @PathVariable int start, @PathVariable int size) {
        return activityService.getDaysByView(startDate, start, size);
    }

    @GetMapping("/activity/days/view/{startDate}/{start}")
    public Result getDaysActivityByView(@PathVariable Date startDate, @PathVariable int start) {
        return activityService.getDaysByView(startDate, start, Conf.PageSize);
    }

    @GetMapping("/activity/days/subscribe/{startDate}/{start}/{size}")
    public Result getDaysActivityBySubscribeWithSize(@PathVariable Date startDate, @PathVariable int start, @PathVariable int size) {
        return activityService.getDaysBySubscribe(startDate, start, size);
    }

    @GetMapping("/activity/days/subscribe/{startDate}/{start}")
    public Result getDaysActivityBySubscribe(@PathVariable Date startDate, @PathVariable int start) {
        return activityService.getDaysBySubscribe(startDate, start, Conf.PageSize);
    }

    // TODO
    @GetMapping("/activity/{startDate}/{endDate}/{start}/{size}")
    public Result getRangeActivityWithSize(@PathVariable Date startDate, @PathVariable Date endDate, @PathVariable int start, @PathVariable int size) {
        return activityService.getRange(startDate, endDate, start, size);
    }

    @GetMapping("/activity/{startDate}/{endDate}/{start}")
    public Result getRangeActivity(@PathVariable Date startDate, @PathVariable Date endDate, @PathVariable int start) {
        return activityService.getRange(startDate, endDate, start, Conf.PageSize);
    }

    // 新增活动
    @PutMapping ("/activity")
    public Result insertActivity(@RequestBody Activity activity){
        return activityService.insertActivity(activity);
    }

    // 浏览和订阅
    @GetMapping("/auth/activity/subscribed")
    public Result getSubscribedActivity(){
        return activityService.getSubscribedActivity();
    }

    @PutMapping("/auth/subscribe/{id}")
    public Result subscribe(@PathVariable Integer id){
        return activityService.subscribe(id);
    }

    @DeleteMapping("/auth/subscribe/{id}")
    public Result unsubscribe(@PathVariable Integer id){
        return activityService.unsubscribe(id);
    }
}
