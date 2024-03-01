package pku.info.activity.vo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.sql.Date;
import java.sql.Time;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ActivityWithSubscribeInfo {
    private Integer id;

    private String title;

    private String address;

    private Date startDate;

    private Date endDate;

    private Time startTime;

    private Time endTime;

    private String description;

    private String college;

    private String link;

    private String info;

    private Integer view;

    private Integer subscribe;

    private String tags;

    private Boolean isSubscribed;
}
