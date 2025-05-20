class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.size();
        vector<vector<int>> pref(n + 1, vector<int>(26, 0));
        int ans = 1;

        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < 26; ++j) {
                pref[i][j] = pref[i - 1][j];
            }

            int c = s[i - 1] - 'A';
            pref[i][c] += 1;

            for (int j = 0; j < 26; ++j) {
                c = j;
                int lo = 1, hi = i;
                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if (pref[i][c] - pref[mid - 1][c] + k >= i - mid + 1) {
                        hi = mid;
                    } else {
                        lo = mid + 1;
                    }
                }
                if (pref[i][c] - pref[lo - 1][c] + k >= i - lo + 1) {
                    ans = max(ans, i - lo + 1);
                }
            }
        }

        return ans;
    }
};
