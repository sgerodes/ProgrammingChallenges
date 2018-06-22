using namespace std;
#include <iostream>
std::string get_middle(std::string input)
{
  int length=input.length();
  int middle=length/2-1;
  int even=length%2;
  return input.substr (middle+even,2-even);
}