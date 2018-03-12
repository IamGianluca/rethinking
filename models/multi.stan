data {
    int<lower=0> N;
    int<lower=0> K;
    matrix[N, K] X;
    vector[N] kcal_per_g;
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
    alpha ~ normal(0, 100);
    beta ~ normal(0, 1);
    //sigma ~ uniform(0, 1);
    kcal_per_g ~ normal(mu, sigma);
}
