#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main()
{
    int n, m;
    string id, op;
    unordered_map<string, bool> map;

    cin >> n;

    while (n--)
    {
        cin >> id;
        map[id] = true;
    }

    cin >> m;

    while (m--)
    {
        cin >> op;

        if (op != "Q")
            cin >> id;
        switch (op[0])
        {
        case 'I':
            map[id] = true;
            break;

        case 'D':
            map.erase(id);
            break;
        case 'Q':
            cout << map.size() << '\n';
            break;
        case 'F':
            cout << map[id] << '\n';
            break;
        }
    }
}