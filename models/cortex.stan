data {
    int<lower=0> N;
    vector[N] X;
    vector[N] kcal_per_g;
}
parameters {
    real alpha;
    real beta;
    real<lower=0> sigma;

}
transformed parameters {
    vector[N] mu;

    mu = alpha + beta * X;
}
model {
    alpha ~ normal(0, 100);
    beta ~ normal(0, 1);
    //sigma ~ uniform(0, 1);
    kcal_per_g ~ normal(mu, sigma);
}
