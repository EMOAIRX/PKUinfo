package pku.info.activity.entity;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@TableName("t_activity_subscription")
public class Subscription {
    @TableField("activity_id")
    private Integer activityId;

    @TableField("user_id")
    private Integer userId;
}
