package pku.pkuinfo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import pku.pkuinfo.mapper.RecordMapper;
import pku.pkuinfo.pojo.RecordInfo;

import java.util.List;

@Service
@Transactional
public class RecordOperationService {

    @Autowired
    private RecordMapper recordMapper;

    public Boolean insert(RecordInfo info){
        Integer res = recordMapper.insertRecord(info);
        return (res != null);
    }

    public Boolean check(RecordInfo info){
        List<RecordInfo> result = recordMapper.checkActivity(info);
        if (result.size() == 0)
            return false;
        else
            return true;
    }
}
