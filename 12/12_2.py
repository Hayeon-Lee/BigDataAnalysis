nlp = Okt()
all_message_pos = nlp.pos(message) #(단어,품사) 여러개가 저장됨
message_V = []

for tuple_item in all_message_pos:
    #print(tuple_item)
    if tuple_item[1] == 'Verb':
        message_V.append(tuple_item[0])

message_V