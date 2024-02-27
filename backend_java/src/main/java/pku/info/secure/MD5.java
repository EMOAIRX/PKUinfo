package pku.info.secure;

import org.springframework.util.DigestUtils;

import java.nio.charset.StandardCharsets;

public class MD5 {
    public static String md5(String str) {
        return DigestUtils.md5DigestAsHex(str.getBytes(StandardCharsets.UTF_8));
    }
}
