package pku.pkuinfo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pku.pkuinfo.mapper.FeedbackMapper;
import pku.pkuinfo.pojo.ActivityFeedbackInfo;

import java.util.List;

@Service
public class FeedbackOperationService {

    @Autowired
    private FeedbackMapper feedbackMapper;

    public Boolean insert(ActivityFeedbackInfo info){
        Integer res = feedbackMapper.insertActivityFeedback(info);
        // System.out.println("FeedbackInsertionCount: " + res);
        return (res==1);
    }

    public List<ActivityFeedbackInfo> select(){
        return feedbackMapper.selectActivityFeedback();
    }
}
