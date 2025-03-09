from flask import Flask, render_template, request

app = Flask(__name__)

# Define 25 quiz questions
questions = [
    {"question": "Which part of the Indian Constitution deals with Fundamental Rights?", 
     "options": ["Part II", "Part III", "Part IV", "Part V"], "answer": "Part III"},

    {"question": "Fundamental Rights in India are borrowed from which country's constitution?", 
     "options": ["France", "United States", "Canada", "United Kingdom"], "answer": "United States"},

    {"question": "Which Fundamental Right is known as the 'Heart and Soul of the Constitution'?", 
     "options": ["Right to Equality", "Right to Freedom", "Right to Constitutional Remedies", "Right to Education"], 
     "answer": "Right to Constitutional Remedies"},

    {"question": "Who is known as the 'Father of the Indian Constitution'?", 
     "options": ["Mahatma Gandhi", "B. R. Ambedkar", "Jawaharlal Nehru", "Sardar Patel"], "answer": "B. R. Ambedkar"},

    {"question": "What does Article 21 of the Indian Constitution ensure?", 
     "options": ["Right to Property", "Right to Life and Personal Liberty", "Right to Education", "Right to Equality"], 
     "answer": "Right to Life and Personal Liberty"},

    {"question": "Which article of the Constitution deals with the abolition of untouchability?", 
     "options": ["Article 14", "Article 17", "Article 19", "Article 21"], "answer": "Article 17"},

    {"question": "Which amendment lowered the voting age from 21 to 18?", 
     "options": ["61st", "42nd", "44th", "73rd"], "answer": "61st"},

    {"question": "Who was the first President of independent India?", 
     "options": ["Dr. Rajendra Prasad", "S. Radhakrishnan", "Jawaharlal Nehru", "Indira Gandhi"], "answer": "Dr. Rajendra Prasad"},

    {"question": "What is the maximum duration for the President's rule in a state?", 
     "options": ["6 months", "1 year", "2 years", "Indefinite"], "answer": "1 year"},

    {"question": "Which body is responsible for conducting elections in India?", 
     "options": ["Supreme Court", "Election Commission", "Lok Sabha", "Rajya Sabha"], "answer": "Election Commission"},

    {"question": "Which fundamental right was removed by the 44th Amendment?", 
     "options": ["Right to Property", "Right to Equality", "Right to Education", "Right to Freedom"], "answer": "Right to Property"},

    {"question": "The Directive Principles of State Policy are inspired by which country's constitution?", 
     "options": ["United States", "Canada", "Ireland", "France"], "answer": "Ireland"},

    {"question": "What is the maximum strength of the Lok Sabha?", 
     "options": ["450", "545", "552", "600"], "answer": "552"},

    {"question": "Who appoints the Chief Justice of India?", 
     "options": ["President", "Prime Minister", "Lok Sabha", "Rajya Sabha"], "answer": "President"},

    {"question": "Which schedule of the Constitution contains anti-defection provisions?", 
     "options": ["7th", "8th", "9th", "10th"], "answer": "10th"},

    {"question": "Who has the power to dissolve the Lok Sabha?", 
     "options": ["President", "Prime Minister", "Chief Justice", "Governor"], "answer": "President"},

    {"question": "Which language is recognized as the official language of India?", 
     "options": ["English", "Hindi", "Sanskrit", "Tamil"], "answer": "Hindi"},

    {"question": "Which article deals with emergency provisions in India?", 
     "options": ["Article 352", "Article 356", "Article 360", "All of the above"], "answer": "All of the above"},

    {"question": "Which body is responsible for economic planning in India?", 
     "options": ["Finance Commission", "NITI Aayog", "RBI", "Lok Sabha"], "answer": "NITI Aayog"},

    {"question": "Which amendment introduced the GST?", 
     "options": ["100th", "101st", "102nd", "103rd"], "answer": "101st"},

    {"question": "Who is the constitutional head of India?", 
     "options": ["Prime Minister", "President", "Chief Justice", "Lok Sabha Speaker"], "answer": "President"},

    {"question": "Which schedule of the Indian Constitution deals with Panchayati Raj?", 
     "options": ["10th", "11th", "12th", "9th"], "answer": "11th"},

    {"question": "Who was the first woman Governor of independent India?", 
     "options": ["Sarojini Naidu", "Indira Gandhi", "Sonia Gandhi", "Sucheta Kripalani"], "answer": "Sarojini Naidu"},

    {"question": "Which article provides special status to Jammu & Kashmir (before abrogation)?", 
     "options": ["Article 356", "Article 370", "Article 371", "Article 377"], "answer": "Article 370"}
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    score = None
    user_answers = {}
    submitted = False

    if request.method == "POST":
        submitted = True
        user_answers = request.form.to_dict()
        score = sum(1 for i, q in enumerate(questions) if user_answers.get(str(i)) == q["answer"])

    return render_template("quiz.html", questions=enumerate(questions), score=score, user_answers=user_answers, submitted=submitted)

if __name__ == "__main__":
    app.run(debug=True)

