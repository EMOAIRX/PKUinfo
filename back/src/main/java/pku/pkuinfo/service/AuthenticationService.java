package pku.pkuinfo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import pku.pkuinfo.mapper.AccessMapper;
import pku.pkuinfo.pojo.Admin;
import pku.pkuinfo.utils.Encryption;
import pku.pkuinfo.utils.JwtUtils;

import java.util.List;
import java.util.Objects;

@Service
@Transactional
public class AuthenticationService {
    @Autowired
    private AccessMapper accessMapper;

    public String login(Admin admin){
        String username = admin.getUsername();
        String password = admin.getPassword();
        List<Admin> result = accessMapper.login(username);
        //System.out.println(result);
        if( result.size() == 1 ){
            String encodedPassword = result.get(0).getPassword();
            if(encodedPassword.equals(Encryption.encode(password))){
                return JwtUtils.createToken(username,password);
            }else{
                return null;
            }
        }else {
            return null;
        }
    }
}
