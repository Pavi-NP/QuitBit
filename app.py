from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import random
import json
import os
from datetime import datetime

app = Flask(__name__)

# Load sentiment analysis model
try:
    sentiment_pipeline = pipeline("sentiment-analysis")
except Exception as e:
    print(f"Error loading model: {e}")
    sentiment_pipeline = None

# Extended response templates based on sentiment and context
responses = {
    "POSITIVE": [
        "That's amazing! Keep up the great work 💪",
        "You're on fire! Stay strong and celebrate every win.",
        "Your progress is inspiring. Keep pushing forward!",
        "Wonderful! Remember how far you've come.",
        "Fantastic! Each smoke-free day makes you stronger.",
        "You're crushing it! Your body is already healing."
    ],
    "NEGATIVE": [
        "It's okay to struggle. You're not alone in this journey.",
        "Take a deep breath. This moment will pass.",
        "Cravings are tough, but you're tougher. Stay focused!",
        "Remember why you started. You can get through this.",
        "Cravings usually last only 5-10 minutes. Distract yourself!",
        "Drink a glass of water and take deep breaths. You've got this."
    ],
    "NEUTRAL": [
        "Every step counts. You're doing great.",
        "Keep checking in—your awareness is powerful.",
        "You're making progress just by showing up here.",
        "Staying consistent is key. You're on the right track.",
        "How are you feeling today? Remember your motivations.",
        "One day at a time. You're building healthier habits."
    ]
}

# Special responses for common smoking-related phrases
smoking_keywords = {
    "craving": [
        "Cravings are temporary. Try the 4 D's: Delay, Deep breathe, Drink water, Do something else.",
        "When a craving hits, distract yourself for 5 minutes. It will pass!",
        "Remember: cravings get weaker every time you resist them."
    ],
    "stress": [
        "Stress is a common trigger. Try deep breathing or a quick walk instead.",
        "Smoking doesn't actually relieve stress - it adds to it. You're stronger without it!",
        "Find healthy stress relievers like exercise, meditation, or talking to someone."
    ],
    "relapse": [
        "It's a slip, not a failure. Get right back on track!",
        "Don't be too hard on yourself. Learn from this and keep going.",
        "Many people have slips on their quitting journey. What matters is what you do next."
    ],
    "withdrawal": [
        "Withdrawal symptoms mean your body is healing. They'll get better soon!",
        "Withdrawal is temporary, but the benefits of quitting last forever.",
        "Stay hydrated and get plenty of rest. Your body is adjusting."
    ]
}

# Motivational facts about quitting
motivational_facts = [
    "Within 20 minutes of quitting, your heart rate drops to normal!",
    "After 24 hours, your risk of heart attack starts decreasing.",
    "Within 2 weeks to 3 months, your lung function improves up to 30%!",
    "After 1 year, your risk of heart disease is cut in half!",
    "By 5 years, your stroke risk is the same as a non-smoker's!",
    "After 10 years, your lung cancer risk drops by 50%!"
]

def analyze_user_message(message):
    """Analyze user message and generate appropriate response"""
    message_lower = message.lower()
    
    # Check for smoking-related keywords
    for keyword, responses_list in smoking_keywords.items():
        if keyword in message_lower:
            return random.choice(responses_list)
    
    # Use sentiment analysis if model is available
    if sentiment_pipeline:
        try:
            sentiment_result = sentiment_pipeline(message)[0]
            sentiment = sentiment_result["label"]
            confidence = sentiment_result["score"]
            
            # Normalize sentiment label
            if sentiment not in responses:
                sentiment = "NEUTRAL"
            
            # Occasionally add motivational facts
            if random.random() < 0.3:  # 30% chance
                return random.choice(responses[sentiment]) + " " + random.choice(motivational_facts)
            
            return random.choice(responses[sentiment])
        except Exception as e:
            print(f"Sentiment analysis error: {e}")
    
    # Fallback response
    return random.choice(responses["NEUTRAL"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message", "").strip()
        
        if not user_input:
            return jsonify({"response": "Please share how you're feeling today."})
        
        bot_response = analyze_user_message(user_input)
        
        return jsonify({
            "response": bot_response,
            "timestamp": datetime.now().strftime("%H:%M")
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({"response": "I'm here to support you. How are you feeling about your smoke-free journey?"})

@app.route("/motivation")
def get_motivation():
    """Endpoint to get random motivational fact"""
    return jsonify({"fact": random.choice(motivational_facts)})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)