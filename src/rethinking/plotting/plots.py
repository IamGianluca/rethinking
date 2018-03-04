import numpy as np
from bokeh.models.ranges import DataRange1d
from bokeh.plotting import figure, show


def summaryplot(fit, pars=None, percentile_interval=(5, 95), debug=False):
    samples = fit.extract(permuted=True)

    pars = pars or list(samples.keys())

    try:
        pars.remove('lp__')
    except ValueError:
        pass

    min_p, max_p, medians, factors = list(), list(), list(), list()
    for par in pars:
        traces = samples[par]

        try:
            cols = traces.shape[1]
        except IndexError:
            cols = 1

        for n in range(cols):
            try:
                column = traces[:, n]
            except IndexError:
                column = traces
            if cols > 1:
                factor = f'{par}[{n}]'
            else:
                factor = par
            factors.append(factor)
            medians.append(np.median(column))
            min_, max_ = np.percentile(column, q=percentile_interval)
            min_p.append(min_)
            max_p.append(max_)

    if debug:
        for factor, m, mi, ma in zip(factors, medians, min_p, max_p):
            print(factor, round(m, ndigits=2), mi, ma)

    p = figure(title='Summary fit', x_axis_label='Value', y_range=sorted(factors, reverse=True))
    p.title.align = 'center'
    p.segment(x0=min_p, y0=factors, x1=max_p, y1=factors)
    p.circle(medians, factors, fill_color='blue', line_color='blue', alpha=.35, line_width=3)
    show(p)
