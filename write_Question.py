import json
lists=[]
def add(question, a,b,c,d,key,level):
    data = {}
    data['question']=question
    data['A'] = a
    data['B'] = b
    data['C'] = c
    data['D'] = d
    data['key'] = key
    data['level'] = level
    lists.append(data)

add('Cho 2 tập A, B rời nhau với |A|=12, |B|=18, | AB| là','12','18','30','29','C',1)
add('Cho tập A={1,2,3,4,5,6,7,8,9}, tập B={1,2,3,9,10}. Tập A-B là:','{1,2,3,9}','{4,5,6,7,8}','10','1,2,3,9,10','B',1)
add('Cho 2 tập A, B với |A|=13, |B|=19, |AB| =1. |AB| là','12','31','32','18', 'B', 2)
add('Cho 2 tập A, B với |A|=15, |B|=20, A⊆B. |AB| là','20','15','35','5','A',2)
add('Cho biết số phần tử của tập A  B  C nếu mỗi tập có 100 phần tử và các tập hợp đôi một rời nhau','200','300','100','0','B',3)
add('Cho biết số phần tử của A  B  C nếu mỗi tập có 100 phần tử và nếu có 50 phần tử chung của mỗi cặp 2 tập và có 10 phần tử chung của cả 3 tập','250','200','160','150','C',3)
add('Cho X={1,2,3,4,5,6,7,8,9}, A={1,2,3,8} Tìm xâu bit biểu diễn tập 𝐴','111000010','000111101','111001101','000110010', 'B',4)
add('Cho X={1,2,3,4,5,6,7,8,9}. Xâu bit biểu diễn tập A là: 111001011, xâu bit biểu diễn tập B là 010111001, Tìm xâu bit biểu diễn tập A or B','010001100','101110010','111111011','010001101','C',4)
add('Cho quy tắc f: ℝ → ℝ thỏa mãn f(x) = 2x2 + 5. Khi đó f là : ','Hàm đơn ánh','Hàm toàn ánh.','Hàm số','Hàm song ánh.','C', 5)
add('Cho tập A = {2, 3, 4, 5}. Hỏi tập nào KHÔNG bằng tập A?','{4, 3, 5, 2}','{a | a là số tự nhiên >1 và <6}','{b | b là số thực sao cho 1<b2 <36}','{b | b là số thực sao cho 1<b2 <36}','C',5)
add('Cho tập A = {1, 2, {3,4}, (a,b,c), }. Lực lượng của A bằng:','8','5','7','4','B',6)
add('Cho tập S = a, b, c khi đó số phần tử của tập lũy thừa của tập S là:','3','6','8','9','C',6)
add('Cho tập A = a, b, B = 0, 1, 2 câu nào dưới đây là SAI:','A x B = B x A','|A x B| = |B x A|','|A x B| = |A| x |B|','|A x B| = |B| x |A|','A',7)
add('Cho 2 tập A, B với A={1,a,2,b,3,c,d}, B ={x,5,y,6,c,1,z}. Số phần tử của tập (A –B) là:','0','5','a','none','B',8)
add('Cho tập S = a, b, c,d khi đó số phần tử của tập lũy thừa của tập S là:','4','16','8','9','B',8)
add('Số các xâu nhị phân có độ dài là 10 là:','1024','1000','20','10','A',9)
add('Có bao nhiêu xâu nhị phân độ dài là 8 hoặc bắt đầu bởi 00 hoặc kết thúc bởi 11','112','128','64','124','A',9)
add('Có bao nhiêu xâu nhị phân độ dài bằng 8 và không chứa 6 số 0 liên tiếp','246','248','256','254','B',10)
add('Có bao nhiêu xâu nhị phân độ dài bằng 8 bắt đầu bởi 00 và kết thúc bởi 11','64','16','32','128','B',10)

with open('.\questions.json','w') as fp:
    json.dump(lists,fp)