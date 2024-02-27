package pku.info.activity.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import jakarta.annotation.Resource;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;
import pku.info.account.bo.UserIdentification;
import pku.info.activity.entity.Activity;
import pku.info.activity.entity.Subscription;
import pku.info.activity.mapper.ActivityMapper;
import pku.info.activity.mapper.SubscribeMapper;
import pku.info.activity.service.ActivityService;
import pku.info.common.Conf;
import pku.info.common.Result;

import java.sql.Date;
import java.util.HashMap;
import java.util.Map;

@Service
public class ActivityServiceImpl implements ActivityService {
    @Resource
    private ActivityMapper activityMapper;
    @Resource
    private SubscribeMapper subscribeMapper;
    private final long DAY = 1000 * 3600 * 24;
    @Override
    @Cacheable(value = "activity", key = "{#root.methodName+'-'+#startDate+'-p'+#start+'-s'+#size}")
    public Result getWeekByView(Date startDate, int start, int size) {
        // 截止时间
        Date endDate = new Date(startDate.getTime() + DAY * 6);
        return selectRange(startDate, endDate, start, size, "view", false);
    }
    @Override
    @Cacheable(value = "activity", key = "{#root.methodName+'-'+#startDate+'-p'+#start+'-s'+#size}")
    public Result getWeekBySubscribe(Date startDate, int start, int size) {
        // 截止时间
        Date endDate = new Date(startDate.getTime() + DAY * 6);
        return selectRange(startDate, endDate, start, size, "subscribe", false);
    }
    @Override
    @Cacheable(value = "activity", key = "{#root.methodName+'-'+#startDate+'-p'+#start+'-s'+#size}")
    public Result getDaysByView(Date startDate, int start, int size) {
        // 截止时间
        Date endDate = new Date(startDate.getTime() + DAY * 2);
        return selectRange(startDate, endDate, start, size, "view", false);
    }
    @Override
    @Cacheable(value = "activity", key = "{#root.methodName+'-'+#startDate+'-p'+#start+'-s'+#size}")
    public Result getDaysBySubscribe(Date startDate, int start, int size) {
        // 截止时间
        Date endDate = new Date(startDate.getTime() + DAY * 2);
        return selectRange(startDate, endDate, start, size, "subscribe", false);
    }
    @Override
    @Cacheable(value = "activity", key = "{#root.methodName+'-'+#startDate+'-'+#endDate+'-p'+#start+'-s'+#size}")
    public Result getRange(Date startDate, Date endDate, int start, int size) {
        return selectRange(startDate, endDate, start, size);
    }
    @Override
    @CacheEvict(value = "activity", allEntries = true)
    public Result insertActivity(Activity activity) {
        int res = activityMapper.insert(activity);
        if(res == 1){
            return Result.success();
        }else{
            return Result.error(500,"CANNOT_INSERT_ACTIVITY");
        }
    }
    @Override
    public Result getSubscribedActivity() {
        return Result.success(activityMapper.getSubscribedActivity(getUserId(),new Date(new java.util.Date().getTime())));
    }
    private Result selectRange(Date startDate, Date endDate, int start, int size){
        IPage<Activity> page = new Page<>(start, size);
        QueryWrapper<Activity> activityQueryWrapper = new QueryWrapper<>();
        activityQueryWrapper.between("start_date",startDate, endDate);
        return Result.success(activityMapper.selectPage(page, activityQueryWrapper));
    }
    @Override
    public Result subscribe(Integer activityId) {
        Integer userId = getUserId();
        if(userId == -1){
            return Result.error(403, "UNAUTHORIZED");
        }else{
            boolean isSubscribed = isSubscribed(activityId, userId);
            if(!isSubscribed){
                // 创建记录
                Subscription subscription = new Subscription();
                subscription.setUserId(userId);
                subscription.setActivityId(activityId);
                subscribeMapper.insert(subscription);
            }
            return Result.success();
        }
    }
    @Override
    public Result unsubscribe(Integer activityId) {
        Integer userId = getUserId();
        if(userId == -1){
            return Result.error(403, "UNAUTHORIZED");
        }else{
            boolean isSubscribed = isSubscribed(activityId, userId);
            if(!isSubscribed){
                return Result.error(400, "NO_SUBSCRIBED_RECORD_FOUND");
            }
            QueryWrapper<Subscription> subscriptionQueryWrapper = new QueryWrapper<>();
            subscriptionQueryWrapper.eq("activity_id", activityId);
            subscriptionQueryWrapper.eq("user_id", userId);
            subscribeMapper.delete(subscriptionQueryWrapper);
            return Result.success();
        }
    }
    private boolean isSubscribed(Integer activityId, Integer userId){
        QueryWrapper<Subscription> subscriptionQueryWrapper = new QueryWrapper<>();
        subscriptionQueryWrapper.eq("activity_id",activityId);
        subscriptionQueryWrapper.eq("user_id",userId);
        Subscription subscription = subscribeMapper.selectOne(subscriptionQueryWrapper);
        return subscription != null;
    }
    private Result selectRange(Date startDate, Date endDate, int start, int size, String col, boolean asc){
        IPage<Activity> page = new Page<>(start, size);
        QueryWrapper<Activity> activityQueryWrapper = new QueryWrapper<>();
        activityQueryWrapper.between("start_date",startDate, endDate);
        activityQueryWrapper.orderBy(true, asc, col);
        return Result.success(activityMapper.selectPage(page, activityQueryWrapper));
    }
    private Integer getUserId(){
        ServletRequestAttributes sra = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
        if (sra != null) {
            // 获取用户信息
            HttpServletRequest request = sra.getRequest();
            UserIdentification attr = (UserIdentification)request.getAttribute(Conf.RequestHeaderAttr);
            return attr.getId();
        }else{
            return -1;
        }
    }
}
