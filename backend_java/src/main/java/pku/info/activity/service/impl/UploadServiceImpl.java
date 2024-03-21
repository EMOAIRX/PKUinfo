package pku.info.activity.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import jakarta.annotation.Resource;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import pku.info.account.dto.Link;
import pku.info.activity.entity.ActivityActiveLink;
import pku.info.activity.entity.ActivityLink;
import pku.info.activity.entity.OfficialAccount;
import pku.info.activity.mapper.ActivityLinkActiveMapper;
import pku.info.activity.mapper.ActivityLinkMapper;
import pku.info.activity.mapper.OfficialAccountMapper;
import pku.info.activity.service.UploadService;
import pku.info.common.Result;

@Service
public class UploadServiceImpl implements UploadService {
    @Resource
    private ActivityLinkMapper activityLinkMapper;

    @Resource
    private ActivityLinkActiveMapper activityLinkActiveMapper;

    @Resource
    private OfficialAccountMapper officialAccountMapper;

    @Override
    @Transactional
    public Result uploadLink(Link link) {
        // 查重
        QueryWrapper<ActivityLink> activityLinkQueryWrapper = new QueryWrapper<>();
        activityLinkQueryWrapper.eq("link",link.getLink());
        ActivityLink res = activityLinkMapper.selectOne(activityLinkQueryWrapper);
        if(res == null){
            // 插入到两个表中
            ActivityLink activityLink = new ActivityLink();
            activityLink.setLink(link.getLink());
            int count = activityLinkMapper.insert(activityLink);
            if(count == 1){
                ActivityActiveLink activityActiveLink = new ActivityActiveLink();
                activityActiveLink.setLink(link.getLink());
                count = activityLinkActiveMapper.insert(activityActiveLink);
                if(count == 1){
                    return Result.success();
                }else{
                    return Result.error(500, "UNABLE_TO_INSERT");
                }
            }else{
                return Result.error(500, "UNABLE_TO_INSERT");
            }
        }else{
            return Result.error(400, "DUPLICATE_KEY");
        }
    }

    @Override
    public Result uploadOfficialAccount(String account) {
        // 查重
        QueryWrapper<OfficialAccount> officialAccountQueryWrapper = new QueryWrapper<>();
        officialAccountQueryWrapper.eq("name",account);
        OfficialAccount officialAccount = officialAccountMapper.selectOne(officialAccountQueryWrapper);
        if(officialAccount == null){
            // 插入数据
            OfficialAccount ins = new OfficialAccount();
            ins.setName(account);
            int res = officialAccountMapper.insert(ins);
            if(res == 1){
                return Result.success();
            }else {
                return Result.error(500,"UNABLE_TO_INSERT");
            }
        }else{
            return Result.error(400,"DUPLICATE_NAME");
        }
    }
}
