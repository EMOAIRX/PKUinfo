package pku.info.activity.controller;

import jakarta.annotation.Resource;
import org.springframework.web.bind.annotation.*;
import pku.info.account.dto.Link;
import pku.info.activity.service.impl.UploadServiceImpl;
import pku.info.common.Result;

@CrossOrigin
@RestController
public class UploadController {
    @Resource
    private UploadServiceImpl uploadService;

    @PostMapping("/auth/officalaccount/{account}")
    public Result uploadOfficialAccount(@PathVariable String account){
        return uploadService.uploadOfficialAccount(account);
    }

    @PostMapping("/auth/link")
    public Result uploadLink(@RequestBody Link link){
        return uploadService.uploadLink(link);
    }
}
