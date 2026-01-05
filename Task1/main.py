from transformers import pipeline

"""
# use bart
summarizer = pipeline("summarization")
summarizer("An apple a day, keeps the doctor away", min_length=5, max_length=20)
"""
pipe = pipeline("summarization", 
                device = -1, 
                min_length = 5, 
                max_length = 50)

while True:
    text = input("Enter text to summarize (or 'exit' to quit): ")
    if text.lower() in ['exit', 'quit', 'q']:
        break
    summary = pipe(text)
    print("Summary:", summary[0]['summary_text'])
    print("\n" * 3)