#include <iostream>
#include <array>
#include <algorithm>

using namespace std;

int main()
{
    array<int, 1441> intervals{};
    int n, tmp, start, end;

    cin >> n >> tmp;

    while (n--)
    {
        cin >> start >> end;
        if (start > end)
            return -1;
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