package pku.info.activity.controller;

import jakarta.annotation.Resource;
import org.springframework.web.bind.annotation.*;
import pku.info.activity.entity.Activity;
import pku.info.activity.service.ActivityService;
import pku.info.common.Conf;
import pku.info.common.ConstantMapper;
import pku.info.common.Result;

import java.sql.Date;

@RestController
@CrossOrigin(origins = "*")
public class ActivityController {
    @Resource
    private ActivityService activityService;

    @GetMapping("/activity/{period}/{type}/{startDate}/{tag}/{start}/{size}")
    public Result getActivityList(@PathVariable Date startDate,
                                  @PathVariable int start,
                                  @PathVariable int size,
                                  @PathVariable int tag,
                                  @PathVariable String period,
                                  @PathVariable String type){
        // 查看是week还是days
        Integer delay = ConstantMapper.translatePeriod(period);
        if(delay != null){
            if("view".equals(type) || "subscribe".equals(type)){
                return activityService.getRangeByInt(startDate, delay, start, size, tag, type);
            }
        }
        return Result.error(400, "BAD_REQUEST");
    }

    @GetMapping("/activity/{period}/{type}/{startDate}/{tag}/{start}/")
    public Result getActivityList(@PathVariable Date startDate,
                                  @PathVariable int start,
                                  @PathVariable int tag,
                                  @PathVariable String period,
                                  @PathVariable String type){
        return getActivityList(startDate, start, Conf.PageSize, tag, period, type);
    }

    // 获取活动
    //@GetMapping("/activity/week/view/{startDate}/{tag}/{start}/{size}")
    //public Result getWeekActivityByViewWithSize(@PathVariable Date startDate, @PathVariable int start, @PathVariable int size, @PathVariable int tag) {
    //    return activityService.getWeekByView(startDate, start, size, tag);
    //}
    //
    //@GetMapping("/activity/week/view/{startDate}/{tag}/{start}")
    //public Result getWeekActivityByView(@PathVariable Date startDate, @PathVariable int start, @PathVariable int tag) {
    //    return activityService.getWeekByView(startDate, start, Conf.PageSize, tag);
    //}
    //
    //@GetMapping("/activity/week/subscribe/{startDate}/{tag}/{start}/{size}")
    //public Result getWeekActivityBySubscribeWithSize(@PathVariable Date startDate, @PathVariable int start, @PathVariable int size, @PathVariable int tag) {
    //    return activityService.getWeekBySubscribe(startDate, start, size, tag);
    //}
    //
    //@GetMapping("/activity/week/subscribe/{startDate}/{tag}/{start}")
    //public Result getWeekActivityBySubscribe(@PathVariable Date startDate, @PathVariable int start, @PathVariable int tag) {
    //    return activityService.getWeekBySubscribe(startDate, start, Conf.PageSize, tag);
    //}
    //
    //@GetMapping("/activity/days/view/{startDate}/{tag}/{start}/{size}")
    //public Result getDaysActivityByViewWithSize(@PathVariable Date startDate, @PathVariable int start, @PathVariable int size, @PathVariable int tag) {
    //    return activityService.getDaysByView(startDate, start, size, tag);
    //}
    //
    //@GetMapping("/activity/days/view/{startDate}/{tag}/{start}")
    //public Result getDaysActivityByView(@PathVariable Date startDate, @PathVariable int start, @PathVariable int tag) {
    //    return activityService.getDaysByView(startDate, start, Conf.PageSize, tag);
    //}
    //
    //@GetMapping("/activity/days/subscribe/{startDate}/{tag}/{start}/{size}")
    //public Result getDaysActivityBySubscribeWithSize(@PathVariable Date startDate, @PathVariable int start, @PathVariable int size, @PathVariable int tag) {
    //    return activityService.getDaysBySubscribe(startDate, start, size, tag);
    //}
    //
    //@GetMapping("/activity/days/subscribe/{startDate}/{tag}/{start}")
    //public Result getDaysActivityBySubscribe(@PathVariable Date startDate, @PathVariable int start, @PathVariable int tag) {
    //    return activityService.getDaysBySubscribe(startDate, start, Conf.PageSize, tag);
    //}

    @GetMapping("/activity/{startDate}/{endDate}/{tag}/{start}/{size}")
    public Result getRangeActivityWithSize(@PathVariable Date startDate,
                                           @PathVariable Date endDate,
                                           @PathVariable int start,
                                           @PathVariable int size,
                                           @PathVariable int tag) {
        return activityService.getRangeByDate(startDate, endDate, start, size, tag, null);
    }

    @GetMapping("/activity/{startDate}/{endDate}/{tag}/{start}")
    public Result getRangeActivity(@PathVariable Date startDate,
                                   @PathVariable Date endDate,
                                   @PathVariable int start,
                                   @PathVariable int tag) {
        return getRangeActivityWithSize(startDate, endDate, start, Conf.PageSize, tag);
    }

    // 登录用户获取活动信息
    @GetMapping("/auth/activity/{period}/{type}/{startDate}/{tag}/{start}/{size}")
    public Result getActivityListWithSubscribeInfoWithSize(@PathVariable String period,
                                                           @PathVariable String type,
                                                           @PathVariable Date startDate,
                                                           @PathVariable int tag,
                                                           @PathVariable int start,
                                                           @PathVariable int size){
        Integer delay = ConstantMapper.translatePeriod(period);
        if(delay != null){
            if("view".equals(type) || "subscribe".equals(type)){
                return activityService.getRangeByIntWithSubscribeInfo(startDate, delay, start, size, tag, type);
            }
        }
        return Result.error(400, "BAD_REQUEST");
    }

    @GetMapping("/auth/activity/{period}/{type}/{startDate}/{tag}/{start}")
    public Result getActivityListWithSubscribeInfo(@PathVariable String period,
                                                   @PathVariable String type,
                                                   @PathVariable Date startDate,
                                                   @PathVariable int tag,
                                                   @PathVariable int start){
        return getActivityListWithSubscribeInfoWithSize(period, type, startDate, tag, start, Conf.PageSize);
    }

    // 新增活动
    @PutMapping ("/activity")
    public Result insertActivity(@RequestBody Activity activity){
        // 输出activity
        System.out.println(activity);
        return activityService.insertActivity(activity);
    }

    // 获取订阅活动
    @GetMapping("/auth/activity/subscribed")
    public Result getSubscribedActivity(){
        return activityService.getSubscribedActivity();
    }

    // 订阅
    @PutMapping("/auth/subscribe/{id}")
    public Result subscribe(@PathVariable Integer id){
        return activityService.subscribe(id);
    }

    // 取消订阅
    @DeleteMapping("/auth/subscribe/{id}")
    public Result unsubscribe(@PathVariable Integer id){
        return activityService.unsubscribe(id);
    }
}
