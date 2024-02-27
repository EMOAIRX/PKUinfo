package pku.info.activity.service;

import pku.info.activity.entity.Activity;
import pku.info.common.Result;

import java.sql.Date;

public interface ActivityService {
    Result getWeekByView(Date date, int start, int size);

    Result getWeekBySubscribe(Date date, int start, int size);

    Result getDaysByView(Date date, int start, int size);

    Result getDaysBySubscribe(Date date, int start, int size);

    Result getRange(Date startDate, Date endDate, int start, int size);

    Result insertActivity(Activity activity);

    Result getSubscribedActivity();

    Result subscribe(Integer id);

    Result unsubscribe(Integer id);
}
