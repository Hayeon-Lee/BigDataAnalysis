after_trimming = CB3

import re
my_p = re.compile("[ 가-힣]+\d+-?\d*")

for index, row in after_trimming.iterrows():
    if after_trimming.loc[index,'x']==0:
        a1 = after_trimming.loc[index, 'address2']
        my_m = my_p.search(a1)
        after_trimming.loc[index, 'address2'] = my_m.group()

display(after_trimming)