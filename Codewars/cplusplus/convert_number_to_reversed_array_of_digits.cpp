#include <vector>
using namespace std;
vector<int> digitize(unsigned long n)
{
  vector <int> reversed;
  while (true)
    {
    reversed.push_back(n%10);
    n /= 10;
    if(n == 0)
        return reversed;
    }
}