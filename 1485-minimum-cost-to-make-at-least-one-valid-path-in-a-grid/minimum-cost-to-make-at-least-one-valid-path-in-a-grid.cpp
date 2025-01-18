constexpr int MAX_N = 101;
constexpr int MAX_F = 2 * MAX_N;


constexpr int DR[] = {0, 0, 1, -1};
constexpr int DC[] = {1, -1, 0, 0};

class Solution {
    int m, n;
    vector<vector<int>> G;
    int dp[MAX_N][MAX_N][MAX_F] = {};
    bool seen[MAX_N][MAX_N][MAX_F] = {};

    bool valid(int r, int c) {
        return 0 <= r && r < m && 0 <= c && c < n;
    }

    int dfs(int r, int c, int fuel) {
        if (fuel >= MAX_F)
            return INT_MAX;
        if (r == m - 1 && c == n - 1)
            return fuel;
        // if (dp[r][c][fuel] != -1)
        //     return dp[r][c][fuel];
        if (seen[r][c][fuel])
            return INT_MAX;
        seen[r][c][fuel] = true;
        int d = G[r][c] - 1;
        int rr = r + DR[d];
        int cc = c + DC[d];
        int best = INT_MAX;
        if (valid(rr, cc))
            best = min(best, dfs(rr, cc, fuel));
        for (d = 0; d < 4; d++) {
            rr = r + DR[d];
            cc = c + DC[d];
            if (valid(rr, cc)) {
                int t = dfs(rr, cc, fuel + 1);
                best = min(best, t == INT_MAX ? INT_MAX : t);
            }
        }
        return best;
    }
public:
    int minCost(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        G = grid;
        for (int r = 0; r < MAX_N; r++)
            for (int c = 0; c < MAX_N; c++)
                for (int f = 0; f < MAX_F; f++)
                    dp[r][c][f] = -1;
        return dfs(0, 0, 0);
    }
};