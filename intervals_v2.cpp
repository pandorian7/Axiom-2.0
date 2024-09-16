#include <iostream>
#include <unordered_map>

using namespace std;

int main()
{
    int n, start, end, tmp, active, prv_active, mid_active;
    unordered_map<int, int> Iopen, Iclose;

    cin >> n >> tmp;

    while (n--)
    {
        cin >> start >> end;
        Iopen[start] = Iclose[end] = 1;
    }

    active = prv_active = 0;

    for (int i = 0; i <= 1440; ++i)
    {
        prv_active = active;
        if (Iopen[i])
            active++;
        mid_active = active;
        if (Iclose[i])
            active--;

        if (active == 1 && prv_active == 0)
            cout << i << " ";
        if (active == 0 && prv_active == 1)
            cout << i << "\n";
        if (active == 0 && prv_active == 0 && mid_active == 1)
            cout << i << " " << i << "\n";
    }
}