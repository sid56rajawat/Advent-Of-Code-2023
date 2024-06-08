#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

int findCalibrationValue(string s)
{
    int calibrationValue = 0;
    for (int ptr = 0; ptr < s.length(); ptr++)
    {
        char c = s[ptr];
        if (c >= '0' && c <= '9')
        {
            calibrationValue = 10 * (int)(c - '0');
            break;
        }
    }
    for (int ptr = s.length() - 1; ptr >= 0; ptr--)
    {
        char c = s[ptr];
        if (c >= '0' && c <= '9')
        {
            calibrationValue += (int)(c - '0');
            break;
        }
    }
    return calibrationValue;
}

string parseString(string &s, unordered_map<string, string> &numberStrings)
{
    string ans = "";
    // go from left
    // check if current place is digit do no transformation
    // check if substr of i+3,i+4 or i+5 is in nums yes then transform
    // push to ans
    for (int i = 0; i < s.length(); i++)
    {
        if (numberStrings.find(s.substr(i, 3)) != numberStrings.end())
        {
            ans += numberStrings[s.substr(i, 3)];
        }
        if (numberStrings.find(s.substr(i, 4)) != numberStrings.end())
        {
            ans += numberStrings[s.substr(i, 4)];
        }
        if (numberStrings.find(s.substr(i, 5)) != numberStrings.end())
        {
            ans += numberStrings[s.substr(i, 5)];
        }
        ans += s[i];
    }
    return ans;
}

int main()
{
    string s;
    unordered_map<string, string> numsVal;
    numsVal["one"] = "1";
    numsVal["two"] = "2";
    numsVal["three"] = "3";
    numsVal["four"] = "4";
    numsVal["five"] = "5";
    numsVal["six"] = "6";
    numsVal["seven"] = "7";
    numsVal["eight"] = "8";
    numsVal["nine"] = "9";

    int sum = 0;
    while (s != "end")
    {
        cin >> s;
        string parsed = parseString(s, numsVal);
        sum += findCalibrationValue(parsed);
    }
    cout << sum << endl;
    return 0;
}