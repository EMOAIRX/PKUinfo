package pku.pkuinfo.utils;

import org.springframework.util.DigestUtils;

import java.nio.charset.StandardCharsets;

public class Encryption {
    private static final String salt = "pkuinfo";

    public static String md5(String str) {
        return DigestUtils.md5DigestAsHex(str.getBytes(StandardCharsets.UTF_8));
    }

    public static String encode(String formPass) {
        String str = salt.charAt(0) + salt.charAt(1) + formPass + salt.charAt(2) + salt.charAt(3);
        return md5(str);
    }
}
