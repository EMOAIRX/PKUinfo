package pku.info.activity.mapper;

import com.baomidou.mybatisplus.core.conditions.Wrapper;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.baomidou.mybatisplus.core.toolkit.Constants;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import pku.info.activity.entity.Activity;

import java.util.Date;
import java.util.List;

@Mapper
public interface ActivityMapper extends BaseMapper<Activity> {
    List<Activity> getWeekActivity(@Param(Constants.WRAPPER) Wrapper wrapper);

    Integer getActivityCount(Date startDate, Date endDate);

    List<Activity> getSubscribedActivity(Integer id, Date now);
}
