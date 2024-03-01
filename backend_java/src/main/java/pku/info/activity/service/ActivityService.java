package pku.info.activity.service;

import pku.info.activity.entity.Activity;
import pku.info.common.Result;

import java.sql.Date;

public interface ActivityService {
    //Result getWeekByView(Date date, int start, int size, int tag);
    //
    //Result getWeekBySubscribe(Date date, int start, int size, int tag);
    //
    //Result getDaysByView(Date date, int start, int size, int tag);
    //
    //Result getDaysBySubscribe(Date date, int start, int size, int tag);

    Result getRangeByDate(Date startDate, Date endDate, int start, int size, int tag, String type);

    Result getRangeByInt(Date startDate, int delay, int start, int size, int tag, String type);

    Result insertActivity(Activity activity);

    Result getSubscribedActivity();

    Result subscribe(Integer id);

    Result unsubscribe(Integer id);

    Result getRangeByIntWithSubscribeInfo(Date startDate, Integer delay, int start, int size, int tag, String type);

    Result getRangeByDateWithSubscribeInfo(Date startDate, Date endDate, int start, int size, int tag, String type);
}
