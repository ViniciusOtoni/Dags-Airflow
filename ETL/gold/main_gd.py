import pandas as pd
import os

import logging
logging.basicConfig(level=logging.INFO)

class GoldETL:

    def __init__(self, path_df, output_dir, file_name, len_df, orderby, ascending, min_bud, min_votes):

        self.df = self.readDataframe(path_df)

        self.df = self.best_worst(self.df, len_df, orderby, ascending, min_bud, min_votes)  

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
    
    def best_worst(self, df, n, by, ascending = False, min_bud = 0, min_votes = 0):
        new_df = df.loc[(df["Movie_Budget"] >= min_bud) & (df["Movie_Vote_Count"] >= min_votes)].sort_values(by=by, ascending= ascending).head(n).copy()
        return new_df


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