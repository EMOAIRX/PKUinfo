package pku.pkuinfo.mapper;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Options;
import pku.pkuinfo.pojo.ActivityInfo;
import pku.pkuinfo.pojo.WeekActivityInfo;

import java.sql.Date;
import java.util.List;

@Mapper
public interface ActivityMapper {
    public Integer insertActivity(ActivityInfo info);

    public Integer deleteActivity(Integer id);

    public List<ActivityInfo> selectActivity(Date startDate,Date endDate);

    public List<WeekActivityInfo> selectWeekActivity(Date startDate,Date endDate);
}
