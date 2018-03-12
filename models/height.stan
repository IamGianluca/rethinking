data {
    int<lower=0> N;                      // number of observations
    real<lower=0, upper=200> height[N];
}
parameters {
    real<lower=0, upper=200> mu;
    real<lower=0, upper=50> sigma;
}
model {
    sigma ~ uniform(0, 50);
    mu ~ normal(178, 20);
    height ~ normal(mu, sigma);
}
