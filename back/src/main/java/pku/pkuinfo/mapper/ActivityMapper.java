package pku.pkuinfo.mapper;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Options;
import pku.pkuinfo.pojo.ActivityInfo;

import java.sql.Date;
import java.util.List;

@Mapper
public interface ActivityMapper {
    public Integer insertActivity(ActivityInfo info);

    public List<ActivityInfo> selectActivity(Date startDate,Date endDate);
}
