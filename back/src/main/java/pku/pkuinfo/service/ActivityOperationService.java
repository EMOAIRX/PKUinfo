package pku.pkuinfo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pku.pkuinfo.mapper.ActivityMapper;
import pku.pkuinfo.pojo.ActivityInfo;

import java.sql.Date;
import java.util.List;

@Service
public class ActivityOperationService {

    @Autowired
    private ActivityMapper activityMapper;

    private final long ONE_DAY = 1000 * 60 * 60 * 24;

    public Boolean insert(ActivityInfo info){
        Integer res = activityMapper.insertActivity(info);
        return (res != null);
    }

    public List<ActivityInfo> select(Date startDate){
        Date endDate = new Date(startDate.getTime() + ONE_DAY * 30);
        return activityMapper.selectActivity(startDate,endDate);
    }
}
