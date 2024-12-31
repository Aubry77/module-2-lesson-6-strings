"""this application is a collection of string manipulation functions
"""
# Task 1: Keyword Highlighter
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

def highlight_keywords(review, keywords):
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
    return review

highlighted_reviews = [highlight_keywords(review, keywords) for review in reviews]
for review in highlighted_reviews:
    print(review)

# Task 2: Sentiment Tally
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(review, positive_words, negative_words):
    positive_count = sum(review.count(word) for word in positive_words)
    negative_count = sum(review.count(word) for word in negative_words)
    return positive_count, negative_count

for review in reviews:
    pos_count, neg_count = sentiment_tally(review, positive_words, negative_words)
    print(f"Review: {review}\nPositive words: {pos_count}, Negative words: {neg_count}\n")

# Task 3: Review Summary
def create_summary(review, length=30):
    if len(review) <= length:
        return review
    else:
        return review[:length].rsplit(' ', 1)[0] + "…"

for review in reviews:
    summary = create_summary(review)
    print(f"Summary: {summary}")

# User Input Data Processor
# Task 1: Input Length Validator
def input_length_validator(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Both first name and last name should be at least 2 characters long.")
    else:
        print("Input is valid.")

# Example usage
input_length_validator("John", "Doe")
input_length_validator("A", "B")
