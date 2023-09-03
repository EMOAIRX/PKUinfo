package pku.pkuinfo.mapper;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Options;
import pku.pkuinfo.pojo.RecordInfo;

import java.util.List;
// This function is used to consider the issue of duplication, that is, whether the public account has appeared before.
@Mapper
public interface RecordMapper {
    public Integer insertRecord(RecordInfo info);

    public List<RecordInfo> checkActivity(RecordInfo info);
}