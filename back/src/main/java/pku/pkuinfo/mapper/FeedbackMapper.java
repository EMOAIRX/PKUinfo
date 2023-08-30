package pku.pkuinfo.mapper;

import org.apache.ibatis.annotations.Mapper;
import pku.pkuinfo.pojo.ActivityFeedbackInfo;

import java.util.List;

@Mapper
public interface FeedbackMapper {
    public Integer insertActivityFeedback(ActivityFeedbackInfo info);

    public List<ActivityFeedbackInfo> selectActivityFeedback();
}
