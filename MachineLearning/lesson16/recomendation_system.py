import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("/Users/mac/Downloads/AI_Engineer/MachineLearning/Datasets/movie_data/movies.csv", encoding='latin-1', sep="\t", usecols=["title", "genres"])
df["genres"] = df["genres"].apply(lambda s: s.replace("|", " ").replace("-", ""))
# vì sci-fi nếu mình không đổi "-" -> " " nó sẽ tách thành 2 từ riêng biệt -> nó cần thành 1 từ chung

# sử dụng những tfid vì cần biết những chủ đề nào quan trọng trong 1 document và tổng thể
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["genres"])
tfidf_matrix_dense = pd.DataFrame(tfidf_matrix.todense(), columns=vectorizer.get_feature_names_out(), index=df["title"])

# ví dụ gợi ý 10 bộ phim, chẳng lẻ bảo người dùng phải đánh giá họ thích thể loại gì, để đưa vào tập test -> lâu 
# khó thực hiện, người dùng chọn đại đại
# recommendation muốn chia tập train, test thì cần có bộ dữ liệu đánh nhãn từ người dùng

consine_sim = cosine_similarity(tfidf_matrix)
consine_sim_dense = pd.DataFrame(consine_sim, columns=df["title"], index=df["title"])
# print(consine_sim_dense)

seen_movie = "Meet the Parents (2000)"
top_k = 5

top_movie = consine_sim_dense[seen_movie].sort_values(ascending=False)[1:top_k+1]
print(top_movie)