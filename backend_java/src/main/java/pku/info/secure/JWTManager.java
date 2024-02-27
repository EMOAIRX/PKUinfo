package pku.info.secure;

import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTVerifier;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.interfaces.Claim;
import com.auth0.jwt.interfaces.DecodedJWT;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;

import static pku.info.common.Conf.JWTCipherText;

public class JWTManager {
    /**
     * 一小时单位
     */
    private static final long HOUR = 3600L * 1000;
    /**
     * 过期时间
     **/
    private static final long EXPIRATION = HOUR * 3; //单位为秒

    /**
     * 生成用户token,设置token超时时间
     */
    public static String createToken(Integer id, String account, String role) {
        // 过期时间
        Date expireDate = new Date(System.currentTimeMillis() + EXPIRATION);
        Map<String, Object> map = new HashMap<>();
        map.put("alg", "HS256");
        map.put("typ", "JWT");
        return JWT.create()
                .withHeader(map) // 添加头部
                .withClaim("id", id)
                .withClaim("account", account)
                .withClaim("role", role)
                .withExpiresAt(expireDate) // 超时设置,设置过期的日期
                .withIssuedAt(new Date()) // 签发时间
                .sign(Algorithm.HMAC256(JWTCipherText));
    }

    public static String createPerpetuateToken(Integer id, String role){
        Map<String, Object> map = new HashMap<>();
        map.put("alg", "HS256");
        map.put("typ", "JWT");
        return JWT.create()
                .withHeader(map) // 添加头部
                .withClaim("id", id)
                .withClaim("role", role)
                .withIssuedAt(new Date()) // 签发时间
                .sign(Algorithm.HMAC256(JWTCipherText));
    }

    /**
     * 验证JWT
     * @param token jwtToken
     * @return null || Claims
     */
    public static Map<String, Claim> verifyToken(String token) {
        DecodedJWT jwt;
        try {
            JWTVerifier verifier = JWT.require(Algorithm.HMAC256(JWTCipherText)).build();
            jwt = verifier.verify(token);
        } catch (Exception e) {
            return null;
        }
        return jwt.getClaims();
    }
}
