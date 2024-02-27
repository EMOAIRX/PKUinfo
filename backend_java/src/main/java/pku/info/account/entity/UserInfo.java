package pku.info.account.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.experimental.Accessors;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Accessors(chain = true)
@TableName("t_user_info")
public class UserInfo {
    @TableId(value = "user_id", type = IdType.INPUT)
    private Integer userId;

    @TableField("user_nickname")
    private String nickname;

    @TableField("email")
    private String email;
}
