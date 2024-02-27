package pku.info.account.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class RegisterInfo {
    // 用户名
    private String username;
    // 密码
    private String password;
    // 邮箱
    private String email = "";
}
