S='''Chiều chiều trước bến Văn Lâu
Ai ngồi, ai câu, ai sầu, ai thảm
Ai thương, ai cảm, ai nhớ, ai trông
Thuyền ai thấp thoáng ven sông
Đưa câu mái vẩy chạnh lòng nước non'''

word=input("Nhập từ cần đếm: ")
print("Câu 63A (có phân biệt HOA và thường): trong đoạn thơ trên có %d từ %s" %(S.count(word), word))
print("Câu 63B (KHÔNG phân biệt HOA và thường): trong đoạn thơ trên có %d từ %s" %(S.upper().count(word.upper()), word))

