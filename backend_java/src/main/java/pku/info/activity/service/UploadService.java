package pku.info.activity.service;

import pku.info.account.dto.Link;
import pku.info.common.Result;

public interface UploadService {
    public Result uploadLink(Link link);

    public Result uploadOfficialAccount(String account);
}
