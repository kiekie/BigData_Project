import sys
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Scatter
# import matplotlib as mpl
# mpl.use('Agg')
# import matplotlib.pyplot as plt
# from mpl_toolkits import mplot3d
# from mpl_toolkits.mplot3d import Axes3D
data = []

for line in sys.stdin:
    words = line.split(',')
    data.append([int(words[0]),float(words[1])])

data.sort(key=lambda x: x[0])
x_data = [d[0] for d in data]
y_data = [d[1] for d in data]

(
    Scatter(init_opts=opts.InitOpts(width="1600px", height="1000px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol_size=20,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_series_opts()
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        tooltip_opts=opts.TooltipOpts(is_show=False),
    )
    .render("basic_scatter_chart.html")
)

# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(x, y, z)
# ax.set_zlabel('Z', fontdict={'size': 1700000, 'color': 'red'})
# ax.set_ylabel('Y', fontdict={'size': 6200, 'color': 'red'})
# ax.set_xlabel('X', fontdict={'size': 90, 'color': 'red'})
# ax.set_title('Hot line')

# plt.savefig('c1' + '_labeled.png')


