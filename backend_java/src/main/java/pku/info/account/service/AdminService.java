package pku.info.account.service;

import pku.info.account.dto.LoginInfo;
import pku.info.account.dto.RegisterInfo;
import pku.info.common.Result;

public interface AdminService {
    Result login(LoginInfo loginInfo);

    Result register(RegisterInfo registerInfo);

    Result deleteAccount(Integer id);

    Result deleteActivity(Integer id);

    Result getAccount();

    Result getActivity();
}
