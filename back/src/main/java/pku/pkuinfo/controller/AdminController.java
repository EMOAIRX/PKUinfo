package pku.pkuinfo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import pku.pkuinfo.pojo.ActivityFeedbackInfo;
import pku.pkuinfo.pojo.ActivityInfo;
import pku.pkuinfo.pojo.RecordInfo;
import pku.pkuinfo.service.ActivityOperationService;
import pku.pkuinfo.service.FeedbackOperationService;
import pku.pkuinfo.service.RecordOperationService;
import pku.pkuinfo.utils.Result;
import java.util.List;

@CrossOrigin(origins = "*")
@RestController
public class AdminController {
    @Autowired
    private ActivityOperationService activityService;

    @Autowired
    private FeedbackOperationService feedbackService;

    @Autowired
    private RecordOperationService recordService;

    @PostMapping ("/api/admin/activity")
    public Result insertActivityInformation(@RequestBody ActivityInfo info){
        // 对象数据
        Boolean res = activityService.insert(info);
        if(res){
            return Result.success();
        }else{
            return Result.error("插入失败");
        }
    }

    @GetMapping("/api/admin/activityfeedback")
    public List<ActivityFeedbackInfo> selectActivityFeedbackInformation(){
        return feedbackService.select();
    }

    // 接收URL请求 转发至Python端
    @PostMapping("/api/admin/activityurl/{targeturl}")
    public Result urlTransmit(@PathVariable String targeturl){
        System.out.println(targeturl);
        return Result.success();
    }

    @PostMapping("/api/admin/record")
    public Result insertActivityRecod(@RequestBody RecordInfo info){
        // 对象数据
        Boolean res = recordService.insert(info);
        if(res){
            return Result.success();
        }else{
            return Result.error("插入失败");
        }
    }

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
}
