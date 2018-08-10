#include <string>
class Solution {
public:
    string intToRoman(int num) {
        string mapI[]={"","I","II","III","IV","V","VI","VII","VIII","IX"};
        string mapX[]={"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
        string mapC[]={"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
        string mapM[]={"", "M", "MM", "MMM"};
        return mapM[num/1000] + mapC[(num%1000)/100] + mapX[(num%100)/10] + mapI[num%10];
    }
};