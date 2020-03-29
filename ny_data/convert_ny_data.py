import pandas as pd


def main():
    df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
    df_ny = df[df.state == 'New York']
    df_ny.date = df.date.apply(lambda x: pd.to_datetime(x).strftime('%m/%d/%y'))

    (pd.pivot_table(df_ny, index='county', columns='date', values='cases', aggfunc='sum')
     .reset_index()
     .rename(columns={'county': 'Country/Region'})
     .to_csv('ny_cases_by_day.csv', index=False)
     )


# ny_deaths_by_day = pd.pivot_table(df, index='county', columns='date', values='deaths', aggfunc='sum')


if __name__ == '__main__':
    main()
