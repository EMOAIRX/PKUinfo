package pku.pkuinfo.service;

import org.springframework.stereotype.Service;
import pku.pkuinfo.pojo.Admin;
import pku.pkuinfo.utils.JwtUtils;

@Service
public class AuthenticationService {
    public String login(Admin admin){
        String username = admin.getUsername();
        String password = admin.getPassword();
        String res = JwtUtils.createToken(username,password);
        return null;
    }
}
