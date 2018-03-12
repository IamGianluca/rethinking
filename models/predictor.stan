data {
    int<lower=0> N;
    vector[N] x;
    vector[N] h;
}
parameters {
    real alpha;
    real beta;
    real<lower=0> sigma;
}
model {
    //sigma ~ uniform(0, 50);
    alpha ~ normal(178, 100);
    beta ~ normal(0, 10);
    h ~ normal(alpha + beta * x, sigma);
}
