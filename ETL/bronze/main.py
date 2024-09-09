import pandas as pd
import os

class BronzeETL:

    def __init__(self, path_df, output_dir, file_name):
        self.df = self.readDataframe(path_df)
        self.df = self.setColumns(self.df)
        self.df = self.createFeatures(self.df)

        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        self.save_to_csv(file_name)

    def readDataframe(self, path_df):
        df = pd.read_csv(path_df, parse_dates=["release_date"])
        return df
    
    def setColumns(self, df):
        df.columns = ["", "Title", "Budget", "Revenue", "Votes", "Average Rating", "Popularity", "Profit", "ROI"]
        return df

    def createFeatures(self, df):
        df['profit_musd'] = df['Revenue'].sub(df['Budget'])
        df['return'] = df['Revenue'].div(df['Budget'])
        return df

    def save_to_csv(self, file_name):
        if not self.df.empty:
            filepath = os.path.join(self.output_dir, file_name)
            self.df.to_csv(filepath, index=False)
            print(f"Arquivo salvo em: {filepath} ")
        else:
            print("Não possui valor o Dataframe")
