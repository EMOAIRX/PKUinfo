package pku.info.account.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import jakarta.annotation.Resource;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import pku.info.account.bo.Role;
import pku.info.account.dto.LoginInfo;
import pku.info.account.entity.UserAccount;
import pku.info.account.dto.RegisterInfo;
import pku.info.account.entity.UserInfo;
import pku.info.account.mapper.UserAccountMapper;
import pku.info.account.mapper.UserInfoMapper;
import pku.info.account.service.UserService;
import pku.info.common.Result;
import pku.info.secure.CiphertextGenerator;
import pku.info.secure.JWTManager;
import pku.info.secure.MD5;
import pku.info.secure.PasswordComparer;

import java.util.HashMap;
import java.util.Map;

@Service
public class UserServiceImpl implements UserService {
    @Resource
    private UserAccountMapper userAccountMapper;
    @Resource
    private UserInfoMapper userInfoMapper;
    @Override
    public Result login(LoginInfo loginInfo) {
        QueryWrapper<UserAccount> userAccountQueryMapper = new QueryWrapper<>();
        userAccountQueryMapper.eq("username",loginInfo.getUsername());
        // 未删除账号
        userAccountQueryMapper.eq("deleted",0);
        UserAccount res = userAccountMapper.selectOne(userAccountQueryMapper, true);
        if(res != null){
            String password = res.getPassword();
            String salt = res.getSalt();
            if(PasswordComparer.compare(loginInfo.getPassword(), password, salt)){
                // 登陆成功
                Map<String, Object> responseBody = new HashMap<>();
                responseBody.put("token",JWTManager.createToken(res.getUserId(), res.getUsername(), Role.USER.name()));
                return Result.success(responseBody);
            }else{
                return Result.error(400, "INCORRECT_ACCOUNT_OR_PASSWORD");
            }
        }
        return Result.error(400, "INCORRECT_ACCOUNT_OR_PASSWORD");
    }

    @Override
    @Transactional(rollbackFor = {Exception.class})
    public Result register(RegisterInfo registerInfo) {
        QueryWrapper<UserAccount> userAccountQueryMapper = new QueryWrapper<>();
        userAccountQueryMapper.eq("username",registerInfo.getUsername());

        UserAccount res = userAccountMapper.selectOne(userAccountQueryMapper, true);

        // 用户名重复
        if(res != null){
            return Result.error(400, "DUPLICATED_USERNAME");
        }
        // 用户名不重复
        // 1. 注册账号
        UserAccount userAccount = new UserAccount();
        userAccount.setUsername(registerInfo.getUsername());
        // 2. 生成随机盐
        String salt = CiphertextGenerator.getSalt();
        userAccount.setSalt(salt);
        // 3. 加密密码
        String encryptedPassword = MD5.md5(registerInfo.getPassword() + salt);
        userAccount.setPassword(encryptedPassword);
        // 4. 插入数据
        int affectedRows = userAccountMapper.insert(userAccount);

        if( affectedRows != 1 ){
            return Result.error(500, "INTERNAL_SERVER_ERROR");
        }
        // 5.获取自增id
        Integer id = userAccount.getUserId();

        // 注册用户信息
        UserInfo userInfo = new UserInfo(id, registerInfo.getUsername(), registerInfo.getEmail());
        affectedRows = userInfoMapper.insert(userInfo);

        if( affectedRows != 1 ){
            return Result.error(500, "INTERNAL_SERVER_ERROR");
        }

        return Result.success();
    }
}
