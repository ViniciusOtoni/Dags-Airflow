import pandas as pd
import os
import logging
logging.basicConfig(level=logging.INFO)

class BronzeETL:

    def __init__(self, path_df, output_dir, file_name):
        try:
            self.df = self.readDataframe(path_df)
            self.df = self.setColumns(self.df)
            self.df = self.createFeatures(self.df)

            self.output_dir = output_dir
            os.makedirs(self.output_dir, exist_ok=True)

            self.save_to_csv(file_name)

        except Exception as e:
            logging.error(f"Erro construtor: {e}")
            raise

    def readDataframe(self, path_df):
        try:
            df = pd.read_csv(path_df, parse_dates=["release_date"])
            logging.info("Leitura sucesso!")
            return df
        
        except Exception as e:
            logging.error(f"Erro na leitura!: {e}")
            raise

    
    def setColumns(self, df):
        try:
            new_columns = {
                    "id": "ID",
                    "title": "Movie_Title",
                    "tagline": "Movie_Tagline",
                    "release_date": "Movie_Release_date",
                    "genres": "Movie_Genres",
                    "belongs_to_collection": "Belongs_to_collection",
                    "original_language": "Movie_Original_Language",
                    "budget_musd": "Movie_Budget",
                    "revenue_musd": "Movie_Revenue",
                    "production_companies": "Production_Companies",
                    "production_countries": "Production_Countries",
                    "vote_count": "Movie_Vote_Count",
                    "vote_average": "Movie_Vote_Average",
                    "popularity": "Movie_Popularity",
                    "runtime": "Movie_Runtime",
                    "overview": "Movie_Overview",
                    "spoken_languages": "Movie_Spoken_Languages",
                    "poster_path": "Movie_Poster_Path",
                    "cast": "Cast",
                    "cast_size": "Cast_Size",
                    "crew_size": "Crew_Size",
                    "director": "Movie_Director"
                }
            
            df.rename(columns=new_columns, inplace=True)
            logging.info("alterando colunas")
            return df
        
        except Exception as e:
            logging.error(f"Erro alteração colunas: {e}")
            raise

    def createFeatures(self, df):
        try:
            df['Movie_Profit'] = df['Movie_Revenue'].sub(df['Movie_Budget'])
            df['Return'] = df['Movie_Revenue'].div(df['Movie_Budget'])
            logging.info("features criadas!")
            return df
        
        except Exception as e:
            logging.error(f"Erro criação de features: {e}")
            raise

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