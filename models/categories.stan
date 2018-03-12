data {
    int N;
    int K;
    matrix[N, K] X;
    vector[N] k;
}
parameters {
    real alpha;
    vector[K] beta;
    real<lower=0> sigma;
}
transformed parameters {
    vector[N] mu;
    mu = alpha + X * beta;
}
model {
    sigma ~ uniform(0, 10);
    beta ~ normal(0, 1);
    alpha ~ normal(0.6, 10);
    k ~ normal(mu, sigma);
}
