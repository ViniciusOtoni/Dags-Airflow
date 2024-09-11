import pandas as pd
import os
import json

import logging
logging.basicConfig(level=logging.INFO)

class SilverETL:

    def __init__(self, path_df, output_dir, file_name):

        self.df = self.readDataframe(path_df)
        
        self.df = self.cleaningBudget(self.df)
        self.df = self.cleaningRevenue(self.df)
        self.df = self.cleaningVoteCount(self.df)
        self.df = self.applyCastSize(self.df)

        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        self.save_to_csv(file_name)

    def readDataframe(self, path_df):
        try:
            df = pd.read_csv(path_df)
            logging.info("Leitura sucesso!")
            return df
        
        except Exception as e:
            logging.error(f"Erro na leitura!: {e}")
            raise
    
    def cleaningBudget(self, df):

        df["Movie_Budget"] = pd.to_numeric(df["Movie_Budget"], errors="coerce")
        df["Movie_Budget"].fillna(0)

        return df

    def cleaningRevenue(self, df):
        
        df["Movie_Revenue"] = pd.to_numeric(df["Movie_Revenue"], errors="coerce")
        df["Movie_Revenue"].fillna(0)

        return df

    def cleaningVoteCount(self, df):
        
        df["Movie_Vote_Count"] = pd.to_numeric(df["Movie_Vote_Count"], errors="coerce")
        df["Movie_Vote_Count"].fillna(0)

        return df
    
    def applyCastSize(self, df):

        df["Cast_List"] = df["Cast"].apply(lambda x: x.strip('|').split('|') if isinstance(x, str) else [])
        df["Cast_Size"] = df["Cast_List"].apply(lambda x: len(x))
        df.drop(columns=["Cast_List"], inplace=True)

        return df

    def save_to_csv(self, file_name):
        try:
            if not self.df.empty:
                filepath = os.path.join(self.output_dir, file_name)
                self.df.to_csv(filepath, index=False)
                logging.info(f"Arquivo salvo em: {filepath} ")
            else:
                logging.warning("Não possui valor o Dataframe")

        except Exception as e:
            logging.error(f"Erro salvando CSV: {e}")
            raise