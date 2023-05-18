no_stop_lemma_words = []

for title in all_title:
    myEnWords = re.sub(r"[^a-zA-Z]+", " ", str(title))
    myEnWordsToken = word_tokenize(myEnWords.lower())
    no_stop_lemma_words.append(myEnWordsToken)

#list 합치기
no_stop_lemma_words2 = list(reduce(lambda x, y: x+y,no_stop_lemma_words))

count2 = Counter(no_stop_lemma_words2)

no_stop_lemma_words_count = {}
for tag, counts in count2.most_common(50):
    if(len(str(tag))>1):
        no_stop_lemma_words_count[tag] = counts
        #print("%s : %d" % (tag, counts))

del no_stop_lemma_words_count['big']
del no_stop_lemma_words_count['data']

no_stop_lemma_wc = WordCloud(background_color='ivory', width=800, height=600)
no_stop_lemma_cloud=wc.generate_from_frequencies(no_stop_lemma_words_count)
plt.figure(figsize=(8,8))
plt.imshow(no_stop_lemma_cloud)
plt.axis('off')
plt.show()

'''
stopword와 lemmatize를 진행하지 않으니 the, in, on 과 같은 불용어가 더 많이 잡히는 것을 알 수 있습니다.
많이 등장하지만 분석에 쓸모없는 단어인 불용어를 제거하지 않은데다가 표제어까지 처리하지 않으니 발생한 일인 것 같습니다.
'''