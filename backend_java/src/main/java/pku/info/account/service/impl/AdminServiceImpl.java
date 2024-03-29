package pku.info.account.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import jakarta.annotation.Resource;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import pku.info.account.bo.Role;
import pku.info.account.dto.LoginInfo;
import pku.info.account.dto.RegisterInfo;
import pku.info.account.entity.AdminAccount;
import pku.info.account.entity.UserAccount;
import pku.info.account.mapper.AdminAccountMapper;
import pku.info.account.mapper.UserAccountMapper;
import pku.info.account.service.AdminService;
import pku.info.activity.entity.Activity;
import pku.info.activity.mapper.ActivityMapper;
import pku.info.common.Result;
import pku.info.secure.CiphertextGenerator;
import pku.info.secure.JWTManager;
import pku.info.secure.MD5;
import pku.info.secure.PasswordComparer;

import java.sql.Date;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
@Service
public class AdminServiceImpl implements AdminService {
    @Resource
    private AdminAccountMapper adminAccountMapper;
    @Resource
    private UserAccountMapper userAccountMapper;
    @Resource
    private ActivityMapper activityMapper;
    @Override
    public Result login(LoginInfo loginInfo) {
        QueryWrapper<AdminAccount> adminAccountQueryWrapper = new QueryWrapper<>();
        adminAccountQueryWrapper.eq("username",loginInfo.getUsername());
        AdminAccount adminAccount = adminAccountMapper.selectOne(adminAccountQueryWrapper);
        if(adminAccount == null){
            return Result.error(400,"INCORRECT_ACCOUNT_OR_PASSWORD");
        }else{
            String salt = adminAccount.getSalt();
            String password = adminAccount.getPassword();
            if(PasswordComparer.compare(loginInfo.getPassword(), password, salt)) {
                // 登陆成功
                Map<String, Object> responseBody = new HashMap<>();
                responseBody.put("token", JWTManager.createPerpetuateToken(adminAccount.getUserId(), Role.ADMIN.name()));
                return Result.success(responseBody);
            }else{
                return Result.error(400,"INCORRECT_ACCOUNT_OR_PASSWORD");
            }
        }
    }

    @Override
    @Transactional(rollbackFor = {Exception.class})
    public Result register(RegisterInfo registerInfo) {
        QueryWrapper<AdminAccount> adminAccountQueryWrapper = new QueryWrapper<>();
        adminAccountQueryWrapper.eq("username",registerInfo.getUsername());
        AdminAccount adminAccount = adminAccountMapper.selectOne(adminAccountQueryWrapper);
        if(adminAccount == null){
            // 注册账号
            AdminAccount newAccount = new AdminAccount();
            newAccount.setUsername(registerInfo.getUsername());
            // 随机盐
            String salt = CiphertextGenerator.getSalt();
            String encryptedPassword = MD5.md5(registerInfo.getPassword() + salt);
            newAccount.setSalt(salt);
            newAccount.setPassword(encryptedPassword);
            int affectedRows = adminAccountMapper.insert(newAccount);
            if(affectedRows != 1){
                return Result.error(500,"INTERNAL_SERVER_ERROR");
            }
            return Result.success();
        }else{
            return Result.error(400,"DUPLICATED_USERNAME");
        }
    }

    @Override
    @Transactional(rollbackFor = {Exception.class})
    public Result deleteAccount(Integer id) {
        int res = userAccountMapper.deleteById(id);
        if(res != 1){
            return Result.error(400,"UNABLE_TO_DELETE");
        }else{
            return Result.success();
        }
    }

    @Override
    public Result getAccount() {
        QueryWrapper<UserAccount> userAccountQueryWrapper = new QueryWrapper<>();
        userAccountQueryWrapper.eq("deleted",0);
        userAccountQueryWrapper.select("user_id", "username");
        List<UserAccount> items = userAccountMapper.selectList(userAccountQueryWrapper);
        List<Map<String,String>> list = new ArrayList<>();
        for(UserAccount item:items){
            Map<String,String> account = new HashMap<>();
            account.put("userId",item.getUserId().toString());
            account.put("username",item.getUsername());
            list.add(account);
        }
        return Result.success(list);
    }

    @Override
    public Result getActivity() {
        QueryWrapper<Activity> activityQueryWrapper = new QueryWrapper<>();
        Date date = new Date(new java.util.Date().getTime());
        activityQueryWrapper.ge("start_date",date);
        List<Activity> res = activityMapper.selectList(activityQueryWrapper);
        return Result.success(res);
    }
}
