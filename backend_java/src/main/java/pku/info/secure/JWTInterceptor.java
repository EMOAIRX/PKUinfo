package pku.info.secure;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;
import com.auth0.jwt.interfaces.Claim;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.servlet.HandlerInterceptor;
import pku.info.account.bo.Role;
import pku.info.account.bo.UserIdentification;
import pku.info.common.Conf;
import pku.info.common.Result;

import java.util.Map;

public class JWTInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        String auth = request.getHeader("authorization");
        // 未携带Token
        if(auth == null){
            response.getWriter().write(JSON.toJSONString(Result.error(401, "NO_AUTHENTICATION_TOKEN"), SerializerFeature.WriteMapNullValue));
            return false;
        }
        String JWTToken = auth.replace("Bearer ", "");

        Map<String, Claim> claims = JWTManager.verifyToken(JWTToken);
        // 非法的Token
        if(claims == null){
            response.getWriter().write(JSON.toJSONString(Result.error(401, "ILLEGAL_AUTHENTICATION_TOKEN"), SerializerFeature.WriteMapNullValue));
            return false;
        }
        UserIdentification userIdentification = new UserIdentification();
        userIdentification.setId(Integer.parseInt(claims.get("id").toString()));
        userIdentification.setRole(Role.valueOf(claims.get("role").asString()));
        request.setAttribute(Conf.RequestHeaderAttr, userIdentification);
        return true;
    }
}
