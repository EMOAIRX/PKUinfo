package pku.info.secure;

public class PasswordComparer {
    public static boolean compare(String plainText, String encryptedText, String salt){
        String encryptedPassword = MD5.md5(plainText+salt);
        return encryptedPassword.equals(encryptedText);
    }
}
