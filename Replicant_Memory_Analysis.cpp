#include <iostream>
#include <map>
#include <vector>

using namespace std;

int min(int a, int b)
{
    return a > b ? b : a;
}

int main()
{
    int n, tmp;
    cin >> n;

    map<int, int> A, B;
    vector<int> out;

    for (int i = n; i--;)
    {
        cin >> tmp;
        A[tmp]++;
    }

    for (int i = n; i--;)
    {
        cin >> tmp;
        B[tmp]++;
    }

    for (auto it = A.begin(); it != A.end(); it++)
    {
        for (int i = min(it->second, B[it->first]); i--;)
        {
            out.push_back(it->first);
        }
    }

    cout << "[";

    for (size_t i = 0; i < out.size(); i++)
    {
        cout << out[i];
        if (i != out.size() - 1)
            cout << ", ";
    }

    cout << "]";
}
