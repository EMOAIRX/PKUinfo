package pku.info.activity.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Mapper;
import pku.info.activity.entity.Activity;
import pku.info.activity.vo.ActivityWithSubscribeInfo;

import java.util.Date;
import java.util.List;

@Mapper
public interface ActivityMapper extends BaseMapper<Activity> {
    Integer getActivityCount(Date startDate, Date endDate);

    Integer getSubscribeActivityCount(Date startDate, Date endDate, Integer id, String tag);

    List<ActivityWithSubscribeInfo> getSubscribedActivityInfo(Date startDate, Date endDate, Integer id, Integer start, Integer size, String tag, String type);

    List<Activity> getSubscribedActivity(Integer id, Date now);
}
