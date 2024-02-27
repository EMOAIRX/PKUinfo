package pku.info.activity.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.format.annotation.DateTimeFormat;

import java.sql.Date;
import java.sql.Time;

@Data
@AllArgsConstructor
@NoArgsConstructor
@TableName("t_activity_info")
public class Activity {
    @TableId(value = "id", type = IdType.AUTO)
    private Integer id;

    @TableField(value = "title")
    private String title;

    @TableField(value = "address")
    private String address;

    @TableField(value = "start_date")
    private Date startDate;

    @TableField(value = "end_date")
    private Date endDate;

    @TableField(value = "start_time")
    private Time startTime;

    @TableField(value = "end_time")
    private Time endTime;

    @TableField(value = "description")
    private String description;

    @TableField(value = "college")
    private String college;

    @TableField(value = "account_link")
    private String link;

    @TableField(value = "extra_info")
    private String info;

    @TableField(value = "view")
    private Integer view;

    @TableField(value = "subscribe")
    private Integer subscribe;

    @TableField(value = "type")
    private String type;
}
