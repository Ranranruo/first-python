from transformers import pipeline

print("model load...")
model = pipeline(
    "text-generation",
    model="upstage/SOLAR-10.7B-Instruct-v1.0",

)
print("model loaded")
message = [
    {"role": "user", "content": "파이썬으로 Hellow World를 출력하는 방법을알려줘."}
]

outputs = model(
    message,
    max_new_tokens=512,
    pad_token_id=model.tokenizer.eos_token_id
)
print("---- result ----")
print(outputs[0]['generated_text'][-1]['content'])