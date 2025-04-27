#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);



/*
 * Complete the 'groupSort' function below.
 *
 * The function is expected to return a 2D_INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

vector<vector<int>> groupSort(vector<int> arr) {
    map<int,int>cnter;
    for (auto e:arr){
        cnter[e]+=1;//(3,2) (1,2) (2,1)
    }
   //for (auto e:cnter){
        
    //    printf("%d,%d\n",e.first,e.second);
    //}
    vector<pair<int,int>>reverse_cnter;
    for (auto e:cnter){
        reverse_cnter.push_back({e.second,-e.first});//23 21 12
    }
    sort(reverse_cnter.begin(),reverse_cnter.end());
    //for (auto e:cnter){
        
    //    printf("%d,%d\n",e.first,e.second);
    //}
    vector<vector<int>> ret;
    for (int i=reverse_cnter.size()-1;i>=0;i--){
        vector<int>cur(2,0);
        cur[1]=reverse_cnter[i].first;
        cur[0]=-reverse_cnter[i].second;
        ret.push_back(cur);
    }
    return ret;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string arr_count_temp;
    getline(cin, arr_count_temp);

    int arr_count = stoi(ltrim(rtrim(arr_count_temp)));

    vector<int> arr(arr_count);

    for (int i = 0; i < arr_count; i++) {
        string arr_item_temp;
        getline(cin, arr_item_temp);

        int arr_item = stoi(ltrim(rtrim(arr_item_temp)));

        arr[i] = arr_item;
    }

    vector<vector<int>> result = groupSort(arr);

    for (int i = 0; i < result.size(); i++) {
        for (int j = 0; j < result[i].size(); j++) {
            fout << result[i][j];

            if (j != result[i].size() - 1) {
                fout << " ";
            }
        }

        if (i != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
