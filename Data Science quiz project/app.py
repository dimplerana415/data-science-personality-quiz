import streamlit as st
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
import os
results_file = os.path.join(os.path.dirname(__file__), "results.csv")

# Load the trained model
with open('model_quiz.pkl','rb') as f:
    model = pickle.load(f)

# UI styling

page_bg= """
<style>
@import 
url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@500&family=Parisienne&family=Raleway:wght@400;600&display=swap'); 

[data-testid="stAppViewContainer"]{
    background: linear-gradient(to bottom right, #f9e6ff, #ffe6f2);
    color: #2c2c2c;
}

h1 {
    text-align: center;
    color: #996fab !important;
    font-family: 'Dancing Script', cursive !important;
    font-weight: 600;
    font-size: 38px;
    white-space: nowrap;
}
h2, h3, h4 {
    color: #bf82be !important;
    font-family: 'Parisienne', cursive !important;
}
div[data-testid= "stMarkdownContainer"]{
    color: #4f354f !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 16px;
}
div.row-widget.stradio > div {
    background-color: #bf82be;
    padding: 12px 18px;
    border-radius: 14px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    margin-bottom: 10px;
}
button[kind="primary"]{
    background-color: #ba68c8 !important;
    color: white !important;
    border-radius: 8px !important;
    font-weight: bold !important;
}
.footer {
    text-align: center;
    font-size: 13px;
    color: #8e24aa;
    margin-top: 30px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title and Description
st.title(" 📊The Data Science Personality Quiz🎀")

# Intro page
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "show_dashboard" not in st.session_state:
    st.session_state.show_dashboard=False

if not st.session_state.quiz_started:
    st.subheader('🌸Welcome, Data Scientist!')

    st.write("""
    Are you ready to discover your **Data Science Personality**?

    This insightful and fun quiz will reveal whether you're a
    logical 📈**Analyst**, the creative 🎨**Storyteller**,
    the curious 🌎**Explorer**, the efficient 💻**Coder,
                or the visionary 🎯**Strategist**?

    👉Answer 12 questions to begin your journey of self discovery!
    """)


    if st.button("💫 Start Quiz"):
        st.session_state.quiz_started = True
        st.rerun()

# ---- MAIN QUIZ SECTION ----
elif st.session_state.quiz_started and not st.session_state.show_dashboard:
    st.markdown("---")
    st.subheader("🧠 Let's get started!")

    # Define Questions
    questions = [
        "1. What is a moment of celebration for you?",
        "2.	Your dream data adventure involves…",
        "3.	What tool excites you the most?",
        "4.	Pick a metaphor for yourself",
        "5.	Pick a data-themed pet",
        "6.	What excites you most about being a data scientist?",
        "7.	What statement describes you the best?",
        "8.	How do you solve a problem?",
        "9.	Your desk is full of…",
        "10. How do you approach learning new skills?",
        "11. If your data project were a movie, it would be…",
        "12. If you had a superpower for one day, which would you pick?"
    ]

    options = [
        ["Seeing accurate patterns", "Sharing insights with others", "Efficient, automated process", "Discovering  new possibilities"],
        ["Finding hidden trends in a massive dataset", "Telling the story behind historical data", "Traveling to collect raw, unusual data", "Designing a plan that wins the project"],
        ["Excel / SQL", "Python / VS code", "APIs / New Datasets", "Project management / strategy tools "],
        ["Sherlock Holmes", "Shakespeare", "Robot", "Adventurer"],
        ["Owl 🦉(observant and logical)", "Parrot 🦜(colorful, communicates)", "Cat 🐱(curious, independent)", "Guide dog 🐶(plans and leads)"],
        ["Turning data into stories", "Automating workflows", "Exploring new domains", "Planning insights and strategies"],
        ['"Data tells the truth; I just find it.”', '“Data is boring without a story.”', '“If its repetitive, I will automate it.”', '“I love planning and optimizing every step.”'],
        ["Step-by-step logical analysis", "Writing scripts and functions", "Experimenting with multiple methods", "Strategizing the optimal plan"],
        ["Organized spreadsheets and notes", "Colorful charts, sticky notes, and doodles", "Cables, gadgets, and keyboards", "Project plans, timelines, and sticky reminders"],
        ["Watching tutorials and examples", "Practicing hands-on coding", "Trying multiple approaches", "Studying best practices and strategies"],
        ["A detective thriller, full of clues", "A sci-fi about robots and automation ", "An adventure exploring unknown lands", "A heist film with a perfect plan"],
        ["Seeing hidden patterns instantly", "Making everyone understand your story", "Instantly automate any task", "Explore anywhere in the world"]
    ]

    mapping = [
        ["Analyst", "Storyteller", "Coder", "Explorer"],
        ["Analyst", "Storyteller", "Explorer", "Strategist"],
        ["Analyst", "Coder", "Explorer", "Strategist"],
        ["Analyst", "Storyteller", "Coder", "Explorer"],
        ["Analyst", "Storyteller", "Explorer", "Strategist"],
        ["Storyteller", "Coder", "Explorer", "Strategist"],
        ["Analyst", "Storyteller", "Coder", "Strategist"],
        ["Analyst", "Coder", "Explorer", "Strategist"],
        ["Analyst", "Storyteller", "Coder", "Strategist"],
        ["Storyteller", "Coder", "Explorer", "Strategist"],
        ["Analyst", "Coder", "Explorer", "Strategist"],
        ["Analyst", "Storyteller", "Coder", "Explorer"]
    ]

    label_map = {
        "Analyst":0,
        "Storyteller":1,
        "Coder":2,
        "Explorer":3,
        "Strategist":4
    }

    if "current_q" not in st.session_state:
        st.session_state.current_q=0
        st.session_state.answers=[]

    q_index = st.session_state.current_q

    # Collect answers
    if q_index<len(questions):
        st.write(f'**Q.{questions[q_index]}**')
        current_options = options[q_index]
        selected_option = st.radio('Choose one:', current_options, key=f"q{q_index+1}")

        if st.button("Next"):
            option_index = current_options.index(selected_option)
            personality = mapping[q_index][option_index]
            numeric_value = label_map[personality]
            st.session_state.answers.append(numeric_value)
            st.session_state.current_q+=1
            st.rerun()

    # Predict pesonality type    
    else:
        # Convert user answers into NumPy array
        st.success("Quiz complete!!!")
        user_answers = np.array(st.session_state.answers).reshape(1,-1)
        prediction = model.predict(user_answers)[0]
        prediction= str(prediction)

        personality_map = {
            0:"Analyst", 
            1:"Storyteller", 
            2:"Coder", 
            3:"Explorer",
            4:"Strategist"
        }

        if prediction.isdigit():
            result= personality_map[int(prediction)]
        else:
            result= prediction

        st.write("🎉 Your Quiz Result 🎉")
        st.markdown(
            f"<h2 style= 'text-align: center; color: #6A5ACD;'>⭐ You are the {result}! ⭐</h2>",
            unsafe_allow_html=True
        )

        # Descriptions for each personality type
        descriptions = {
            "Analyst": "📊 *Analyst* — You love uncovering patterns and finding meaning in data. \
        You're detail-oriented, logical, and thrive on understanding how things work beneath the surface. \
        Your analytical mind helps you make smart, data-driven decisions that guide others effectively.",

            "Coder": "💻 *Coder* — You're a builder and a problem solver. \
        You love turning ideas into reality with code. Logical, curious, and persistent, you thrive when \
        you're solving puzzles or automating complex tasks.",

            "Storyteller": "🎨 *Storyteller* — You transform numbers into narratives. \
        You make data emotional and human, turning insights into stories that inspire others. \
        Creativity meets communication in your data-driven world!",

            "Explorer": "🧭 *Explorer* — Curiosity is your compass! \
        You love discovering new patterns, trends, and technologies. You're experimental, adaptive, and \
        never afraid to dive deep into the unknown.",

            "Strategist": "🎯 *Strategist* — You think big. \
        You're a planner who connects data, ideas, and people to achieve clear goals. \
        Your vision and leadership guide others toward success."
        }

        # Display the personality result
        st.markdown(f"<p style='text-align: center; font-size: 18px;'>{descriptions.get(result, 'You have a unique combination of traits!')}</p>", unsafe_allow_html=True)


        # Saving results to CSV file

        import csv
        import os
    
        file_exists= os.path.exists(results_file)

        with open(results_file,'a',newline="") as f:
            writer= csv.writer(f)
            if not file_exists or os.stat(results_file).st_size==0:
                writer.writerow(["Personality"])
            writer.writerow([result])
            
        # Creating restart quiz button

        if st.button("Restart Quiz🔄"):
            st.session_state.current_q=0
            st.session_state.answers=[]
            st.session_state.quiz_started=False
            st.rerun()

        # Creating a summary dashboard

        if st.button("View Summary Dashboard 📃"):
            st.session_state.show_dashboard=True
            st.rerun()

elif st.session_state.show_dashboard:
    st.title('📊 Your Quiz Summary Dashoboard')
    if not os.path.exists(results_file):
        st.warning("No valid data to show yet. Try after a few quiz completions.")
    else:
        data= pd.read_csv(results_file)
        if 'Personality' not in data.columns or data.empty:
            st.info("No data yet - take the quiz first! ❌")
            
        else:
            data['Personality']= data['Personality'].str.strip().str.title()
            data=data[data['Personality'].isin(['Analyst', 'Storyteller', 'Coder', 'Explorer', 'Strategist'])]
            summary= data["Personality"].value_counts()

            st.markdown(
                """
                <div style='text-align: center; background-color: #fbeaff;
                        border-radius: 15px; padding: 25px; margin-top: 20px;'>
                    <h2 style='color: #7b1fa2;'>🌸 Summary Dashboard 🌸</h2>
                    <p style='font-size: 16px; color: #6a1b9a;'>
                        Here's how your quiz results look so far!
                    </p>
                </div>
            """, unsafe_allow_html=True)

            pastel_colors = ['#b39ddb', '#f48fb1', '#ce93d8', '#81d4fa', '#ffe082']

            fig,ax = plt.subplots(figsize=(6,6))
            wedges, texts, autotexts = ax.pie(
                summary.values,
                labels=summary.index,
                autopct="%1.1f%%",
                startangle=90,
                colors=pastel_colors,
                textprops={'fontsize': 12, 'color': '#4a148c'}
            )

            # Add a circular border
            for w in wedges:
                w.set_edgecolor("white")
                w.set_linewidth(2)

            ax.axis("equal")
            plt.setp(autotexts, size=11, weight="bold", color="white")
            plt.title("Personality Type Distribution", color="#6a1b9a", fontsize=16, pad=20)
            st.pyplot(fig)

            if st.button("⬅ Back to Results"):
                st.session_state.show_dashboard=False
                st.rerun()
        