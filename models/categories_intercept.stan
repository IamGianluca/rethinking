data {
    int N;
    int J;
    int<lower=1, upper=J> clade_id[N];
    vector[N] k;
}
parameters {
    real alpha[J];
    real<lower=0> sigma;
}
transformed parameters {
    real mu[N];

    for (n in 1:N) {
        mu[n] = alpha[clade_id[n]];
    }
}
model {
    sigma ~ uniform(0, 10);
    alpha ~ normal(0.6, 10);
    k ~ normal(mu, sigma);
}
