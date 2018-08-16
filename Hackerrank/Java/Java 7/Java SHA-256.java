import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Scanner.*;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import javax.xml.bind.DatatypeConverter;

public class Solution {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String data = sc.nextLine();
        sc.close();
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] b = digest.digest(data.getBytes("UTF-8"));
            String hash = DatatypeConverter.printHexBinary(b);
            System.out.print(hash.toLowerCase());
        } catch (Exception ex) {
            ex.printStackTrace();
        }

    }
}