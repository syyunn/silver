import utils

fname = "../raw/silver_daily.csv"
f = open(fname, 'r')

dates = []
silvers = []

for line in f.readlines():
    content = line.split(',')
    idx = content[0]
    print(idx)
    if len(idx) == 0:
        continue
    date = content[1]
    silver = content[2].split('\n')[0]
    if len(silver) == 0:
        continue
    print(silver)
    silver = float(silver)

    dates.append(date)
    silvers.append(silver)

df = utils.make_as_pandas_df(dates, content_name='Silver', content_list=silvers)

utils.standard_plot(df, column_name='Silver')

utils.pickle_object(df, "../data/silver_daily.pkl")


if __name__ == "__main__":
    pass
