import pandas as pd
from pathlib import Path 

class DataManager:
    """
    Class responsible for loading and saving the CSV data.
    """
    
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    DATA_DIR = BASE_DIR / 'data'

    @classmethod
    def load_csv(cls, filename: str = "AmesHousing.csv", processed: bool=False) -> pd.DataFrame:
        """Reads CSV data into a DataFrame, using non default NA values.

        Args:
            filename (str, optional): Name of the CSV file. Defaults to "AmesHousing.csv".
            processed (bool, optional): If True loads data from 'processed' subdirectory, else from 'raw'. Defaults to False.

        Raises:
            FileNotFoundError: If file was not found.

        Returns:
            pd.DataFrame: DataFrame with loaded dataset.
        """
        
        sub_dir = 'processed' if processed else 'raw'

        path = cls.DATA_DIR / sub_dir / filename

        if path.suffix != '.csv':
            path = path.with_suffix('.csv') 

        if not path.exists():
            raise FileNotFoundError(f'Could not find the file: {path}')

        return pd.read_csv(path, keep_default_na=False, na_values=['','NA'])
    
    @classmethod
    def save_csv(cls, df: pd.DataFrame , filename: str) -> None:
        """Saves DataFrame to a CSV file in the 'processed' subdirectory.

        Args:
            df (pd.DataFrame): DataFrame to save.
            filename (str): Name of the CSV file.
        """

        path = cls.DATA_DIR / 'processed' / filename

        if path.suffix != '.csv':
            path = path.with_suffix('.csv')

        #create the 'processed' subdirectory if not exists
        path.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(path, sep=',', header = True, index = False)
        