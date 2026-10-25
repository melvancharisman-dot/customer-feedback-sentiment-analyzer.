
def analyze_sentiment(feedback):
    positive_words = [
        "bagus", "puas", "baik", "ramah", "cepat",
        "suka", "mantap", "excellent", "great", "good"
    ]

    negative_words = [
        "buruk", "kecewa", "lambat", "mahal", "jelek",
        "kecewa", "rusak", "parah", "bad", "poor"
    ]

    text = feedback.lower()

    positive_score = sum(word in text for word in positive_words)
    negative_score = sum(word in text for word in negative_words)

    if positive_score > negative_score:
        sentiment = "POSITIVE"
        reason = "Feedback menunjukkan kepuasan pelanggan."
    elif negative_score > positive_score:
        sentiment = "NEGATIVE"
        reason = "Feedback menunjukkan keluhan atau ketidakpuasan."
    else:
        sentiment = "NEUTRAL"
        reason = "Feedback belum menunjukkan sentimen positif atau negatif yang dominan."

    return sentiment, reason


print("=" * 50)
print("   CUSTOMER FEEDBACK SENTIMENT ANALYZER")
print("=" * 50)

while True:
    feedback = input("\nMasukkan feedback pelanggan (atau ketik 'exit'): ")

    if feedback.lower() == "exit":
        print("Terima kasih telah menggunakan aplikasi.")
        break

    if not feedback.strip():
        print("Feedback tidak boleh kosong.")
        continue

    sentiment, reason = analyze_sentiment(feedback)

    print("\n--- HASIL ANALISIS ---")
    print("Feedback :", feedback)
    print("Sentiment:", sentiment)
    print("Reason   :", reason)
    print("-" * 50)
