import seaborn as sns
import pandas as pd

titanic= sns.load_dataset("titanic")
pd.Categorical(titanic['embark_town'], categories=['Southampton', 'Cherbourg']).unique()