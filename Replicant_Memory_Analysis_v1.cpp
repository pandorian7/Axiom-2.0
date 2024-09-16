#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main()
{
    int n, tmp;
    cin >> n;

    unordered_map<int, int> A(n), B(n);
    vector<int> Av, out;

    for (int i = n; i--;)
    {
        cin >> tmp;
        A[tmp]++;
        Av.push_back(tmp);
    }

    for (int i = n; i--;)
    {
        cin >> tmp;
        B[tmp]++;
    }

    for (auto val : Av)
    {
        if (A[val] && B[val])
        {
            out.push_back(val);
        }
        A[val]--;
        B[val]--;
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