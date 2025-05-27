def preprocess_data(df):
    df = df.dropna(axis=1, how="all")
    df = df.fillna(0)
    return df