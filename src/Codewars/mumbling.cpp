using namespace std;
class Accumul
{
public:
    static std::string accum(const std::string &s){
    string mumbled="";
    mumbled+=toupper(s.at(0));
    for(int i=1;i<s.length();++i){
      char c=s.at(i);
      mumbled+="-";
      mumbled+=toupper(c);
      for(int j=0;j<i;++j){
        mumbled+=tolower(c);
      }
    }
    return mumbled;
    }
};