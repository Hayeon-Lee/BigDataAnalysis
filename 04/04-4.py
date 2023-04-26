### 과제4 : numeric column 들의 boxplot을 한 그림에 그리시오
#titanic.info()
#numeric column: survived, pclass, age, sibsp, parch, fare
columns = titanic.columns
plot_columns = [columns[0], columns[1], columns[3], columns[4], columns[5], columns[6]]

fig, ax = plt.subplots()
ax.boxplot([titanic['survived'], titanic['pclass'], titanic['age'], titanic['sibsp'], titanic['parch'], titanic['fare']])
plt.title('Numeric Columns of Titanic')
plt.xticks([1,2,3,4,5,6], plot_columns)
plt.show()