import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

sns.boxplot(x='embark_town', y='age', data=titanic)
model = ols('age~embark_town', titanic).fit()
print(anova_lm(model))