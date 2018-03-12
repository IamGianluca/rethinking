data {
    int<lower=0> N;                  // n observations
    int<lower=0> M;                  // n features
    vector[N] weight;
    vector[N] weight_2;              // weight^2
    vector[N] height;
}
parameters {
    real alpha;
    real beta[M];
    real<lower=0> sigma;
}
model {
    alpha ~ normal(178, 100);
    beta ~ normal(0, 10);
    height ~ normal(alpha + beta[1] * weight + beta[2] * weight_2, sigma);
}
