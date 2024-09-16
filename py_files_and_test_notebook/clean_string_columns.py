# Define function for cleaning string columns for search engines:
def mod_col_values(df, col):
    old_column_index = df.columns.get_loc(col)
    new_col_name = "mod_" + df.columns[old_column_index]
    df[new_col_name] = df[col].str.lower().replace("[^a-zA-Z0-9]", " ", regex=True)
    df[new_col_name] = df[new_col_name].str.replace('\s+', ' ', regex=True)
    df = df[df[new_col_name].str.len() > 0]
    return df