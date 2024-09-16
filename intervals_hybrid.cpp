#include <iostream>
#include <array>
#include <algorithm>
#include <unordered_map>
#include <cstdlib>
#include <time.h>
#include <unistd.h>

using namespace std;

void main1()
{
    array<int, 1441> intervals{};
    int n, tmp, start, end;

    cin >> n >> tmp;

    while (n--)
    {
        cin >> start >> end;
        for (int i = start; i <= end; i++)
        {
            intervals[i] = 1;
        }
    }

    array<int, 1441>::iterator head, start_, end_, first, last;

    first = head = intervals.begin();
    last = intervals.end();

    while (true)
    {
        start_ = find(head, last, 1);
        if (start_ == last)
            break;
        end_ = find(start_, last, 0);
        cout << start_ - first << " " << end_ - first - 1 << endl;
        head = end_;
    }
}

void main2()
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

int main()
{
    srand(time(0) * getpid());
    int choice = rand() % 2;
    if (choice == 0)
        main1();
    else
        main2();
}