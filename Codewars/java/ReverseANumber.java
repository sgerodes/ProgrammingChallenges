package Codewars.java;

public class ReverseANumber {

    public static int reverse(int number) {
        String string_number = int_to_str(number);
        boolean sign = number < 0;
        if (sign) {string_number=cutoff_sign(string_number);}
        return string_to_int(sign(sign) + reverse_string(string_number));
    }

    public static String int_to_str(int num){
        return Integer.toString(num);
    }
    public static int string_to_int(String str){
        return Integer.parseInt(str);
    }
    public static String cutoff_sign(String str){
        return str.substring(1);
    }
    public static String reverse_string(String str){
        return new StringBuilder(str).reverse().toString();
    }
    public static String sign(boolean sign){
        return sign ? "-" : "" ;
    }
}