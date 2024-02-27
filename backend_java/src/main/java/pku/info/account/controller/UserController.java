package pku.info.account.controller;

import jakarta.annotation.Resource;
import org.springframework.web.bind.annotation.*;
import pku.info.account.dto.LoginInfo;
import pku.info.account.dto.RegisterInfo;
import pku.info.account.service.UserService;
import pku.info.common.Result;

@RestController
public class UserController {
    @Resource
    private UserService userService;

    @PostMapping("/login")
    public Result login(@RequestBody LoginInfo loginInfo){
        return userService.login(loginInfo);
    }

    @PutMapping("/register")
    public Result register(@RequestBody RegisterInfo registerInfo){
        return userService.register(registerInfo);
    }
}
