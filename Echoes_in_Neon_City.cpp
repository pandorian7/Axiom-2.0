#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

vector<string> extend(string str, int jump)
{
    vector<string> ret;
    int tail = str.back() - '0';
    int next, prv;
    next = tail + jump;
    prv = tail - jump;
    if (prv >= 0)
        ret.push_back(str + (char)(prv + '0'));
    if (next < 10)
        ret.push_back(str + (char)(next + '0'));
    return ret;
}

int main()
{
    queue<string> q;
    size_t n, m;
    cin >> n >> m;
    vector<string> res;

    for (int i = 1; i <= 9; i++)
        q.push(to_string(i));

    while (!q.empty())
    {
        if (q.front().size() < n)
        {
            for (auto s : extend(q.front(), m))
            {
                q.push(s);
            }
        }
        else
            res.push_back(q.front());

        q.pop();
    }

    if (!res.empty())
    {
        for (size_t i = 0; i < res.size() - 1; i++)
            cout << res.at(i) << ", ";
        cout << res.back();
    }
    else
        cout << -1;
}