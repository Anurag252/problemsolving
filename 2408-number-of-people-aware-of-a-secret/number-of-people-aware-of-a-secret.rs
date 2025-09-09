impl Solution {
    pub fn people_aware_of_secret(n: i32, delay: i32, forget: i32) -> i32 {
        const MOD: usize = 1_000_000_007;

        let n = n as usize;
        let delay = delay as usize;
        let forget = forget as usize;

        // Edge: if delay >= forget, no one ever shares
        if delay >= forget {
            // Everyone forgets before they can share
            // Only original person might remain if n < forget
            return if n < forget { 1 } else { 0 } as i32;
        }

        // d[i] = number of people who are on their i-th day of delay (0-indexed)
        let mut d = vec![0usize; delay];
        // f[i] = number of people who are on their i-th day of "active sharing" (after delay, before forget)
        let mut f = vec![0usize; forget - delay];

        // Day 1
        d[0] = 1;

        for day in 2..=n {
            // 1. People finishing delay today: they are at the last slot of d
            let mut finished_delay = 0;
            if delay > 0 {
                finished_delay = d[delay - 1];
            }

            // 2. Shift delay queue LEFT
            if delay > 0 {
                for i in (1..delay).rev() {
                    d[i] = d[i - 1];
                }
                d[0] = 0; // will be filled with new people
            }

            // 3. Shift forget queue LEFT
            let mut finished_forget = 0;
            if !f.is_empty() {
                finished_forget = f[f.len() - 1];
                for i in (1..f.len()).rev() {
                    f[i] = f[i - 1];
                }
                f[0] = 0;
            }

            // 4. People who finished delay today now enter sharing phase
            if !f.is_empty() {
                f[0] = finished_delay;
            } else {
                // if forget - delay == 0, then they forget immediately after delay — so don't add
            }

            // 5. Current active sharers = sum of f
            let sharing_count = f.iter().sum::<usize>() % MOD;

            // 6. New people generated today start delay — go into d[0]
            if delay > 0 {
                d[0] = sharing_count;
            } else {
                // if delay == 0, they start sharing immediately → should go into f[0]
                // But if delay == 0 and forget > 0, then f exists
                if !f.is_empty() {
                    f[0] = (f[0] + sharing_count) % MOD;
                }
            }
        }

        // Answer = everyone still in d or f
        let mut total = d.iter().sum::<usize>() + f.iter().sum::<usize>();
        total %= MOD;
        total as i32
    }
}