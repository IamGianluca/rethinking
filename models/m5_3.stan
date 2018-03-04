data {
    int<lower=0> N;
    int<lower=0> K;
    matrix[N, K] X;
    vector<lower=0, upper=100>[N] divorce_rate;
}
parameters {
    real alpha;
    vector[K] beta;
    real<lower=0> sigma;
}
transformed parameters {
    vector<lower=-100, upper=100>[N] mu;

    mu = alpha + X * beta;
}
model {
    alpha ~ normal(10, 10);
    beta ~ normal(0, 1);
    sigma ~ uniform(0, 10);
    divorce_rate ~ normal(mu, sigma);
}
