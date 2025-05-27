def anonymize_data(df, columns_to_remove):
    return df.drop(columns=columns_to_remove, errors='ignore')