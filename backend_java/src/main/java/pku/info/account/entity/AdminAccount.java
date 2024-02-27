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
@TableName("t_admin_account")
public class AdminAccount {
    @TableId(value = "id", type = IdType.AUTO)
    private Integer userId;

    @TableField("username")
    private String username;

    @TableField("password")
    private String password;

    @TableField("salt")
    private String salt;
}
