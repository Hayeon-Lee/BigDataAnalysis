my_addr = backup #backup은 위에서 선언 하였습니다.

#병상수를 주소 데이터 프레임에 합치기
bedside = data['병상수'].values
for index, row in my_addr.iterrows():
    my_addr.loc[index, 'count'] = bedside[index]

#count 컬럼의 이름 바꾸기
my_addr = my_addr.rename(columns = {my_addr.columns[3]:'병상수'})
#display(my_addr) #확인용

#시도군구 별 병상수 groupby 하기
my_addr_group = pd.DataFrame(my_addr.groupby('시도군구', as_index = False).sum())
#display(my_addr_group) #확인용

#데이터프레임 합치기
my_population = backup_pop #backup_pop은 위에서 선언 하였습니다.
my_addr_pop_merge = pd.merge(my_addr_group, my_population, how='inner', left_on = '시도군구', right_on='시도군구')
my_addr_pop_merge_left = pd.merge(my_addr_group, my_population, how='left', left_on='시도군구', right_on='시도군구')
my_addr_pop_merge_left[my_addr_pop_merge['총인구수 (명)'].isnull()]

my_local_MC_pop = my_addr_pop_merge[['시도군구', '병상수', '총인구수 (명)']]
#display(my_local_MC_pop) #확인용

#인구수 대비 병상수 구하기
my_local_MC_pop['bedside_ratio'] = my_local_MC_pop['병상수']/my_local_MC_pop['총인구수 (명)'] * 100000
#display(my_local_MC_pop) #확인용

#한국 데이터 합치기
my_data_draw_korea_MC_Population_all = pd.merge(data_draw_korea,my_local_MC_pop,  how='left',  left_on='시도군구', right_on='시도군구')
#display(my_data_draw_korea_MC_Population_all) #확인용

#블록맵 그리기
draw_blockMap(my_data_draw_korea_MC_Population_all, '병상수', '행정구역별 병상수', 'cubehelix_r')