wine.columns = [c.replace(' ', '_') for c in wine.columns]

red_df= pd.read_csv("winequality-red.csv", sep=";")
mymodel =  ols ( 'quality~fixed_acidity+volatile_acidity+citric_acid+residual_sugar', data=wine[:5000]).fit()
mymodel.summary()
mymodel.predict(wine[:5000])

from statsmodels.graphics.regressionplots import plot_partregress_grid
fig=plot_partregress_grid(mymodel)
fig.tight_layout(pad=1)