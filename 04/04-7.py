from scipy.stats import chisquare
num_class=sample1["embark_town"].value_counts()
print (num_class)
print ( chisquare (num_class) )
#pvalue가 7.973716005 이므로 0.05보다 크기 때문에 유의하지 않다.
