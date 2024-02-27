package pku.info.account.controller;

import jakarta.annotation.Resource;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.web.bind.annotation.*;
import pku.info.account.dto.LoginInfo;
import pku.info.account.dto.RegisterInfo;
import pku.info.account.service.AdminService;
import pku.info.common.Result;

@RestController
@CrossOrigin(origins = "*")
public class AdminController {
    @Resource
    private AdminService adminService;

    @PostMapping("/admin/login")
    public Result login(@RequestBody LoginInfo loginInfo){
        return adminService.login(loginInfo);
    }

    @PutMapping("/admin/register")
    public Result register(@RequestBody RegisterInfo registerInfo){
        return adminService.register(registerInfo);
    }

    @DeleteMapping("/admin/user/{id}")
    public Result deleteAccount(@PathVariable Integer id){
        return adminService.deleteAccount(id);
    }

    @DeleteMapping("/admin/activity/{id}")
    @CacheEvict(value = "activity", allEntries = true)
    public Result deleteActivity(@PathVariable Integer id){
        return adminService.deleteActivity(id);
    }

    @GetMapping("/admin/activity")
    public Result getActivity(){
        return adminService.getActivity();
    }

    @GetMapping("/admin/user")
    public Result getAccount(){
        return adminService.getAccount();
    }
}
