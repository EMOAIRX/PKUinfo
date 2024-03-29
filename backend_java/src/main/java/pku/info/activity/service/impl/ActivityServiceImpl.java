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
import pku.info.activity.vo.ActivityWithSubscribeInfo;
import pku.info.common.Conf;
import pku.info.common.ConstantMapper;
import pku.info.common.Result;

import java.sql.Date;
import java.util.List;

@Service
public class ActivityServiceImpl implements ActivityService {
    @Resource
    private ActivityMapper activityMapper;
    @Resource
    private SubscribeMapper subscribeMapper;
    //@Override
    //@Cacheable(value = "activity", key = "{#root.methodName+'_'+#startDate+'_p'+#start+'_s'+#size+'_t'+#tag}")
    //public Result getWeekByView(Date startDate, int start, int size, int tag) {
    //    return selectRange(startDate, setDate(startDate, 6), start, size, "view", false, tag);
    //}
    //@Override
    //@Cacheable(value = "activity", key = "{#root.methodName+'_'+#startDate+'_p'+#start+'_s'+#size+'_t'+#tag}")
    //public Result getWeekBySubscribe(Date startDate, int start, int size, int tag) {
    //    // 截止时间
    //    Date endDate = new Date(startDate.getTime() + DAY * 6);
    //    return selectRange(startDate, setDate(startDate, 6), start, size, "subscribe", false, tag);
    //}
    //@Override
    //@Cacheable(value = "activity", key = "{#root.methodName+'_'+#startDate+'_p'+#start+'_s'+#size+'_t'+#tag}")
    //public Result getDaysByView(Date startDate, int start, int size, int tag) {
    //    return selectRange(startDate, setDate(startDate, 2), start, size, "view", false, tag);
    //}
    //@Override
    //@Cacheable(value = "activity", key = "{#root.methodName+'_'+#startDate+'_p'+#start+'_s'+#size+'_t'+#tag}")
    //public Result getDaysBySubscribe(Date startDate, int start, int size, int tag) {
    //    return selectRange(startDate, setDate(startDate, 2), start, size, "subscribe", false, tag);
    //}
    @Override
    @Cacheable(value = "activity", key = "{#root.methodName+'_'+#startDate+'_'+#endDate+'_p'+#start+'_s'+#size+'_t'+#tag+#type}")
    public Result getRangeByDate(Date startDate, Date endDate, int start, int size, int tag, String type) {
        return selectRange(startDate, endDate, start, size, type, true, tag);
    }
    @Override
    @Cacheable(value = "activity", key = "{#root.methodName+'_'+#startDate+'_'+#delay+'_p'+#start+'_s'+#size+'_t'+#tag+#type}")
    public Result getRangeByInt(Date startDate, int delay, int start, int size, int tag, String type) {
        return selectRange(startDate, setDate(startDate, delay), start, size, type, true, tag);
    }

    @Override
    public Result getRangeByIntWithOrder(Date startDate, int delay, int start, int size, int tag, String type, Boolean desc) {
        return selectRange(startDate, setDate(startDate, delay), start, size, type, desc, tag);
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
        List<Activity> list = activityMapper.getSubscribedActivity(getUserId(),new Date(new java.util.Date().getTime()));
        System.out.println(list);
        return Result.success(list);
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

    @Override
    public Result getRangeByIntWithSubscribeInfo(Date startDate, Integer delay, int start, int size, int tag, String type, Boolean desc) {
        Date endDate = setDate(startDate, delay);
        return getRangeByDateWithSubscribeInfo(startDate, endDate, start, size, tag, type, desc);
    }

    @Override
    public Result getRangeByDateWithSubscribeInfo(Date startDate, Date endDate, int start, int size, int tag, String type, Boolean desc) {
        Integer userId = getUserId();
        if(userId == -1){
            return Result.error(403, "UNAUTHORIZED");
        }else{
            String tagName = ConstantMapper.translateTag(tag);
            int count = activityMapper.getSubscribeActivityCount(startDate, endDate, userId, tagName);
            pku.info.activity.vo.Page page = new pku.info.activity.vo.Page();
            page.setTotal(count);
            page.setCurrent(start);
            page.setSize(size);
            page.setPages((int) Math.ceil((double) count / (double) size));
            // 是否需要查数据
            if((start - 1) * size >= count){
                page.setRecords(new Object[]{});
                return Result.success(page);
            }
            Integer startIndex = (start - 1) * size;
            List<ActivityWithSubscribeInfo> activityList = activityMapper.getSubscribedActivityInfo(startDate, endDate, userId, startIndex, size, tagName, type, desc);
            page.setRecords(activityList.toArray());
            return Result.success(page);
        }
    }

    private boolean isSubscribed(Integer activityId, Integer userId){
        QueryWrapper<Subscription> subscriptionQueryWrapper = new QueryWrapper<>();
        subscriptionQueryWrapper.eq("activity_id",activityId);
        subscriptionQueryWrapper.eq("user_id",userId);
        Subscription subscription = subscribeMapper.selectOne(subscriptionQueryWrapper);
        return subscription != null;
    }
    private Result selectRange(Date startDate, Date endDate, int start, int size, String col, boolean desc, int tag){
        IPage<Activity> page = new Page<>(start, size);
        QueryWrapper<Activity> activityQueryWrapper = new QueryWrapper<>();
        activityQueryWrapper.between("start_date",startDate, endDate);
        // 获取对应标签
        String tagName = ConstantMapper.translateTag(tag);
        if(tagName != null){
            activityQueryWrapper.like("type", tagName);
        }
        activityQueryWrapper.orderBy((col != null), !desc, col);
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
    private Date setDate(Date startDate, Integer delay){
        long DAY = 1000 * 3600 * 24;
        return new Date(startDate.getTime() + DAY * delay);
    }



    @Override
    @CacheEvict(value = "activity", allEntries = true)
    public Result deleteActivity(Integer id) {
        int res = activityMapper.deleteById(id);
        if(res != 1){
            return Result.error(400,"UNABLE_TO_DELETE");
        }else{
            return Result.success();
        }
    }

    @Override
    @CacheEvict(value = "activity", allEntries = true)
    public Result modifyActivity(Activity activity) {
        if(activityMapper.updateById(activity) == 1){
            return Result.success();
        }else{
            return Result.error(500,"UNABLE_TO_UPDATE_ACTIVITY");
        }
    }
}
