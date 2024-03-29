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
public class ActivityFetchController {
    @Resource
    private ActivityService activityService;

    @GetMapping("/activity/week/view/{startDate}/{start}/{size}/{tag}")
    public Result getWeekActivityListWithSizeByView(@PathVariable Date startDate,
                                          @PathVariable int start,
                                          @PathVariable int size,
                                          @PathVariable int tag){
        return activityService.getRangeByInt(startDate, 6, start, size, tag, "view");
    }

    @GetMapping("/activity/week/view/{startDate}/{start}/{tag}")
    public Result getWeekActivityListByView(
                                  @PathVariable Date startDate,
                                  @PathVariable int start,
                                  @PathVariable int tag){
        return getWeekActivityListWithSizeByView(startDate, start, Conf.PageSize, tag);
    }

    @GetMapping("/activity/week/subscribe/{startDate}/{start}/{size}/{tag}")
    public Result getWeekActivityListWithSizeBySubscribe(@PathVariable Date startDate,
                                          @PathVariable int start,
                                          @PathVariable int size,
                                          @PathVariable int tag){
        return activityService.getRangeByInt(startDate, 6, start, size, tag, "subscribe");
    }

    @GetMapping("/activity/week/subscribe/{startDate}/{start}/{tag}")
    public Result getWeekActivityListBySubscribe(
            @PathVariable Date startDate,
            @PathVariable int start,
            @PathVariable int tag){
        return getWeekActivityListWithSizeBySubscribe(startDate, start, Conf.PageSize, tag);
    }

    @GetMapping("/activity/days/view/{startDate}/{start}/{size}/{tag}")
    public Result getDaysActivityListWithSizeByView(@PathVariable Date startDate,
                                          @PathVariable int start,
                                          @PathVariable int size,
                                          @PathVariable int tag){
        return activityService.getRangeByInt(startDate, 2, start, size, tag, "view");
    }

    @GetMapping("/activity/days/view/{startDate}/{start}/{tag}")
    public Result getDaysActivityListByView(
            @PathVariable Date startDate,
            @PathVariable int start,
            @PathVariable int tag){
        return getDaysActivityListWithSizeByView(startDate, start, Conf.PageSize, tag);
    }

    @GetMapping("/activity/days/subscribe/{startDate}/{start}/{size}/{tag}")
    public Result getDaysActivityListWithSizeBySubscribe(@PathVariable Date startDate,
                                  @PathVariable int start,
                                  @PathVariable int size,
                                  @PathVariable int tag){
        return activityService.getRangeByInt(startDate, 2, start, size, tag, "subscribe");
    }

    @GetMapping("/activity/days/subscribe/{startDate}/{start}/{tag}")
    public Result getDaysActivityListBySubscribe(
            @PathVariable Date startDate,
            @PathVariable int start,
            @PathVariable int tag){
        return getDaysActivityListWithSizeBySubscribe(startDate, start, Conf.PageSize, tag);
    }

    @GetMapping("/activity/{startDate}/{endDate}/{start}/{size}/{tag}")
    public Result getRangeActivityWithSize(@PathVariable Date startDate,
                                           @PathVariable Date endDate,
                                           @PathVariable int start,
                                           @PathVariable int size,
                                           @PathVariable int tag) {
        return activityService.getRangeByDate(startDate, endDate, start, size, tag, null);
    }

    @GetMapping("/activity/{startDate}/{endDate}/{start}/{tag}")
    public Result getRangeActivity(@PathVariable Date startDate,
                                   @PathVariable Date endDate,
                                   @PathVariable int start,
                                   @PathVariable int tag) {
        return getRangeActivityWithSize(startDate, endDate, start, Conf.PageSize, tag);
    }

    @GetMapping("/activity/week/default/{startDate}/{start}/{size}/{tag}")
    public Result getWeekActivityListWithSizeByDefault(@PathVariable Date startDate,
                                                       @PathVariable int start,
                                                       @PathVariable int size,
                                                       @PathVariable int tag){
        return activityService.getRangeByIntWithOrder(startDate, 6, start, size, tag, "start_date", false);
    }

    @GetMapping("/activity/week/default/{startDate}/{start}/{tag}")
    public Result getWeekActivityListByDefault(@PathVariable Date startDate,
                                               @PathVariable int start,
                                               @PathVariable int tag){
        return getWeekActivityListWithSizeByDefault(startDate, start, Conf.PageSize, tag);
    }

    @GetMapping("/auth/activity/week/default/{startDate}/{start}/{size}/{tag}")
    public Result getWeekActivityListWithSubscribeInfoWithSizeByDefault(@PathVariable Date startDate,
                                                                        @PathVariable int start,
                                                                        @PathVariable int size,
                                                                        @PathVariable int tag){
        return activityService.getRangeByIntWithSubscribeInfo(startDate, 6,start,size,tag,"start_date",false);
    }

    @GetMapping("/auth/activity/week/default/{startDate}/{start}/{tag}")
    public Result getWeekActivityListWithSubscribeInfoByDefault(@PathVariable Date startDate,
                                                                @PathVariable int start,
                                                                @PathVariable int size,
                                                                @PathVariable int tag){
        return getWeekActivityListWithSubscribeInfoWithSizeByDefault(startDate, start, Conf.PageSize, tag);
    }

    // 登录用户获取活动信息
    @GetMapping("/auth/activity/week/view/{startDate}/{start}/{size}/{tag}")
    public Result getWeekActivityListWithSubscribeInfoWithSizeByView(@PathVariable Date startDate,
                                                           @PathVariable int tag,
                                                           @PathVariable int start,
                                                           @PathVariable int size){
        return activityService.getRangeByIntWithSubscribeInfo(startDate, 6, start, size, tag, "view", true);
    }

    @GetMapping("/auth/activity/week/view/{startDate}/{start}/{tag}")
    public Result getWeekActivityListWithSubscribeInfoByView(@PathVariable Date startDate,
                                                   @PathVariable int tag,
                                                   @PathVariable int start){
        return getWeekActivityListWithSubscribeInfoWithSizeByView(startDate, tag, start, Conf.PageSize);
    }

    @GetMapping("/auth/activity/week/subscribe/{startDate}/{start}/{size}/{tag}")
    public Result getWeekActivityListWithSubscribeInfoWithSizeBySubscribe(@PathVariable Date startDate,
                                                           @PathVariable int tag,
                                                           @PathVariable int start,
                                                           @PathVariable int size){
        return activityService.getRangeByIntWithSubscribeInfo(startDate, 6, start, size, tag, "subscribe", true);
    }

    @GetMapping("/auth/activity/week/subscribe/{startDate}/{start}/{tag}")
    public Result getWeekActivityListWithSubscribeInfoBySubscribe(@PathVariable Date startDate,
                                                   @PathVariable int tag,
                                                   @PathVariable int start){
        return getWeekActivityListWithSubscribeInfoWithSizeBySubscribe(startDate, tag, start, Conf.PageSize);
    }

    @GetMapping("/auth/activity/days/view/{startDate}/{start}/{size}/{tag}")
    public Result getDaysActivityListWithSubscribeInfoWithSizeByView(@PathVariable Date startDate,
                                                           @PathVariable int tag,
                                                           @PathVariable int start,
                                                           @PathVariable int size){
        return activityService.getRangeByIntWithSubscribeInfo(startDate, 2, start, size, tag, "view", true);
    }

    @GetMapping("/auth/activity/days/view/{startDate}/{start}/{tag}")
    public Result getDaysActivityListWithSubscribeInfoByView(
                                                   @PathVariable Date startDate,
                                                   @PathVariable int tag,
                                                   @PathVariable int start){
        return getDaysActivityListWithSubscribeInfoWithSizeByView(startDate, tag, start, Conf.PageSize);
    }

    @GetMapping("/auth/activity/days/subscribe/{startDate}/{start}/{size}/{tag}")
    public Result getDaysActivityListWithSubscribeInfoWithSizeBySubscribe(@PathVariable Date startDate,
                                                           @PathVariable int tag,
                                                           @PathVariable int start,
                                                           @PathVariable int size){
        return activityService.getRangeByIntWithSubscribeInfo(startDate, 2, start, size, tag, "subscribe", true);
    }

    @GetMapping("/auth/activity/days/subscribe/{startDate}/{start}/{tag}")
    public Result getDaysActivityListWithSubscribeInfoBySubscribe(@PathVariable Date startDate,
                                                   @PathVariable int tag,
                                                   @PathVariable int start){
        return getDaysActivityListWithSubscribeInfoWithSizeBySubscribe(startDate, tag, start, Conf.PageSize);
    }

    @GetMapping("/auth/activity/{startDate}/{endDate}/{start}/{size}/{tag}")
    public Result getRangeActivityWithSubscribeInfoWithSize(@PathVariable Date startDate,
                                           @PathVariable Date endDate,
                                           @PathVariable int start,
                                           @PathVariable int size,
                                           @PathVariable int tag) {
        return activityService.getRangeByDateWithSubscribeInfo(startDate, endDate, start, size, tag, null, true);
    }

    @GetMapping("/auth/activity/{startDate}/{endDate}/{start}/{tag}")
    public Result getRangeActivityWithSubscribeInfo(@PathVariable Date startDate,
                                   @PathVariable Date endDate,
                                   @PathVariable int start,
                                   @PathVariable int tag) {
        return getRangeActivityWithSubscribeInfoWithSize(startDate, endDate, start, Conf.PageSize, tag);
    }

    // 获取订阅活动
    @GetMapping("/auth/activity/subscribed")
    public Result getSubscribedActivity(){
        return activityService.getSubscribedActivity();
    }

}
