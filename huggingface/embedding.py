from sentence_transformers import SentenceTransformer,util
from sentence_transformers.cross_encoder import CrossEncoder

model = SentenceTransformer("dragonkue/BGE-m3-ko")

db_sentences = [
    "오늘 점심 메뉴는 김치찌개가 좋겠어.",
    "날씨가 정말 화창하고 좋네요.",
    "요즘 재미있는 영화 추천 좀 해주세요.",
    "파이썬 코딩은 정말 재미있습니다.",
    "가까운 지하철역이 어디인가요?",
    "맛있는 저녁 식사 메뉴를 고민 중이다.",
    "타입스크립트 배우기 1",
    "파이썬 배우기 1",
    "JS란? 1강",
    "Javascript 고찰 13강"
]
db_embeddings = model.encode(db_sentences)

query = "자바스크립트 배우려면 어떻게 해야하지"
query_embedding = model.encode(query)

cosine_scores = util.cos_sim(query_embedding, db_embeddings)
scores_list = cosine_scores[0]
all_results = []
for i in range(len(db_sentences)):
    all_results.append((db_sentences[i], scores_list[i].item()))

sorted_results = sorted(all_results, key=lambda x: x[1], reverse=True)

print("--- 1단계 결과 (임베딩 유사도 순) ---")
for sentence, score in sorted_results:
    print(f"{score:.4f} | {sentence}")
print("-" * 30)




reranker_model = CrossEncoder("dragonkue/bge-reranker-v2-m3-ko")


reranker_input_pairs = []
for sentence, score in sorted_results:
    reranker_input_pairs.append((query, sentence))


reranker_scores = reranker_model.predict(reranker_input_pairs)


reranked_results = []
for i in range(len(reranker_input_pairs)):
    sentence = reranker_input_pairs[i][1]
    score = reranker_scores[i]
    reranked_results.append((sentence, score))


final_sorted_results = sorted(reranked_results, key=lambda x: x[1], reverse=True)

print("--- 2단계 최종 결과 (Reranker 정밀 점수 순) ---")
for sentence, score in final_sorted_results:
    print(f"{score:.4f} | {sentence}")