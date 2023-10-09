package pku.pkuinfo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import pku.pkuinfo.mapper.ActivityMapper;
import pku.pkuinfo.pojo.ActivityInfo;
import pku.pkuinfo.pojo.WeekActivityInfo;

import java.sql.Date;
import java.util.List;

@Service
@Transactional
public class ActivityOperationService {

    @Autowired
    private ActivityMapper activityMapper;

    private final long ONE_DAY = 1000 * 60 * 60 * 24;

    public Integer insert(ActivityInfo info){
        return activityMapper.insertActivity(info);
    }

    public Integer delete(Integer id){
        return activityMapper.deleteActivity(id);
    }

    /*
     * 开启Redis缓存
     * */
    @Cacheable(value = "activity", key = "#startDate")
    public List<ActivityInfo> select(Date startDate){
        Date endDate = new Date(startDate.getTime() + ONE_DAY * 30);
        return activityMapper.selectActivity(startDate,endDate);
    }

    /*
    * 开启Redis缓存
    * */
    @Cacheable(value = "activity_week", key = "#startDate")
    public List<WeekActivityInfo> weekselect(Date startDate){
        Date endDate = new Date(startDate.getTime() + ONE_DAY * 7);
        return activityMapper.selectWeekActivity(startDate, endDate);
    }
}
