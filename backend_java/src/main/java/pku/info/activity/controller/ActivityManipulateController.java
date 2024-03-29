package pku.info.activity.controller;

import jakarta.annotation.Resource;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.web.bind.annotation.*;
import pku.info.account.service.AdminService;
import pku.info.activity.entity.Activity;
import pku.info.activity.service.ActivityService;
import pku.info.common.Result;

@RestController
@CrossOrigin(origins = "*")
public class ActivityManipulateController {
    @Resource
    private ActivityService activityService;

    @Resource
    private AdminService adminService;

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

    // 新增活动
    @PutMapping ("/activity")
    public Result insertActivity(@RequestBody Activity activity){
        // 输出activity
        System.out.println(activity);
        return activityService.insertActivity(activity);
    }

    // 删除活动
    @DeleteMapping("/admin/activity/{id}")
    @CacheEvict(value = "activity", allEntries = true)
    public Result deleteActivity(@PathVariable Integer id){
        return activityService.deleteActivity(id);
    }

    // 修改活动信息
    @PutMapping("/admin/activity")
    public Result modifyActivity(@RequestBody Activity activity){
        return activityService.modifyActivity(activity);
    }
}
