package pku.pkuinfo.mapper;

import org.apache.ibatis.annotations.Mapper;
import pku.pkuinfo.pojo.Admin;

import java.util.List;

@Mapper
public interface AccessMapper {
    public List<Admin> login(String username);
}

