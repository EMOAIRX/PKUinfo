package pku.info.account.service;

import pku.info.account.dto.LoginInfo;
import pku.info.account.dto.RegisterInfo;
import pku.info.common.Result;

public interface UserService {
    public Result login(LoginInfo loginInfo);

    public Result register(RegisterInfo registerInfo);
}
