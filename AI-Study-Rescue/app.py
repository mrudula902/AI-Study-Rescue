import streamlit as st
from datetime import datetime, date, time

st.set_page_config(
    page_title="AI Study Rescue",
    page_icon="📚",
    layout="wide"
)

# ---------- HEADER ----------
st.title("📚 AI Study Rescue")
st.caption("Your intelligent last-minute exam preparation assistant")

# ---------- EXAM COUNTDOWN ----------
st.subheader("⏳ Exam Countdown")

c1, c2 = st.columns(2)

with c1:
    exam_date = st.date_input(
        "Exam Date",
        min_value=date.today()
    )

with c2:
    exam_time = st.time_input(
        "Exam Time",
        value=time(9, 0)
    )

exam_datetime = datetime.combine(exam_date, exam_time)
remaining = exam_datetime - datetime.now()

if remaining.total_seconds() > 0:
    days = remaining.days
    hours = remaining.seconds // 3600
    minutes = (remaining.seconds % 3600) // 60

    st.success(
        f"🚨 **{days} Days {hours} Hours {minutes} Minutes remaining!**"
    )
else:
    st.error("Exam time has passed.")

st.divider()

# ---------- INPUTS ----------
st.subheader("📋 Tell AI About Your Exam")

syllabus = st.text_area(
    "📖 Syllabus",
    placeholder="""Example:
Digital Image Processing
Image Segmentation
Sampling and Quantization
Convolution and Correlation
Computer Vision Applications""",
    height=130
)

weak_topics = st.text_input(
    "⚠️ Weak Topics",
    placeholder="Example: Segmentation, Convolution"
)

col1, col2 = st.columns(2)

with col1:
    preparation = st.slider(
        "📊 Preparation Level",
        0, 100, 40
    )

with col2:
    stress = st.slider(
        "😰 Stress Level",
        1, 10, 5
    )

# ---------- TABS ----------
tab1, tab2, tab3, tab4 = st.tabs([
    "🚨 Rescue Plan",
    "📖 Quick Notes",
    "🧠 Quiz Me",
    "🎯 Study Strategy"
])

# ---------- RESCUE PLAN ----------
with tab1:

    if st.button("🚀 Generate My Rescue Plan", use_container_width=True):

        st.subheader("🔥 Your Emergency Study Plan")

        if remaining.total_seconds() <= 0:
            st.error("Your exam time has passed.")
        else:

            if days == 0:
                st.warning(
                    "🚨 LAST-MINUTE MODE: Focus only on high-priority topics!"
                )
            elif days <= 1:
                st.warning(
                    "⚡ 1-DAY MODE: Avoid learning everything. Revise smartly."
                )
            else:
                st.info(
                    "📅 You have enough time for focused learning + revision."
                )

            st.markdown("### ⭐ Priority Order")

            if weak_topics.strip():
                st.write("🥇 **Weak Topics:**", weak_topics)

            if syllabus.strip():
                topics = [
                    x.strip()
                    for x in syllabus.split("\n")
                    if x.strip()
                ]

                for i, topic in enumerate(topics[:5], 1):
                    st.write(f"**{i}.** {topic}")

            st.markdown("### ⏰ What Should You Study NOW?")

            if weak_topics.strip():
                st.success(
                    f"🎯 Study this NOW → **{weak_topics.split(',')[0].strip()}**"
                )
            else:
                st.success(
                    "🎯 Study this NOW → Your first syllabus topic"
                )

            if stress >= 8:
                st.info(
                    "🧘 High stress detected. Study for 25 minutes, "
                    "then take a 5-minute break."
                )

# ---------- QUICK NOTES ----------
with tab2:

    st.subheader("📖 Quick Notes Generator")

    note_topic = st.text_input(
        "Enter a topic",
        placeholder="Example: Image Segmentation"
    )

    if st.button("✨ Generate Quick Notes"):

        if not note_topic.strip():
            st.warning("Enter a topic first.")
        else:

            st.success(f"Quick revision notes for: **{note_topic}**")

            st.markdown(f"""
### 📌 {note_topic}

**Definition:**  
{note_topic} is an important concept that should be understood
using its basic definition, purpose and applications.

**Key Points:**
- Understand the basic concept
- Remember important terminology
- Learn the main steps/process
- Focus on examples
- Revise important advantages and applications

**🧠 Exam Trick:**  
Remember the **Definition → Process → Example → Application**
pattern when writing a 5-mark answer.

**⚡ 30-Second Revision:**  
Read the definition → remember 3 key points → recall one example.
""")

# ---------- QUIZ ----------
with tab3:

    st.subheader("🧠 Rapid Quiz")

    quiz_topic = st.text_input(
        "Quiz Topic",
        placeholder="Example: Digital Image Processing"
    )

    if st.button("🎯 Start Quiz"):

        if not quiz_topic.strip():
            st.warning("Enter a topic first.")
        else:

            st.success(f"Quiz generated for **{quiz_topic}**")

            st.markdown("### Question 1")

            answer = st.radio(
                "What should you focus on first when revising a topic?",
                [
                    "Only memorizing the topic name",
                    "Definition and basic concept",
                    "Skipping difficult concepts",
                    "Reading without understanding"
                ]
            )

            if st.button("Check Answer"):
                if answer == "Definition and basic concept":
                    st.success("✅ Correct!")
                else:
                    st.error(
                        "❌ Not quite. Start with the definition and basic concept."
                    )

            st.markdown("### Question 2")

            answer2 = st.radio(
                "Which approach is useful for last-minute revision?",
                [
                    "Study every topic equally",
                    "Focus on important and weak topics",
                    "Avoid revision",
                    "Study random topics"
                ]
            )

            if st.button("Check Q2"):
                if answer2 == "Focus on important and weak topics":
                    st.success("✅ Correct!")
                else:
                    st.error("❌ Focus on important and weak topics.")

# ---------- STRATEGY ----------
with tab4:

    st.subheader("🎯 Personalized Study Strategy")

    score = preparation

    if weak_topics.strip():
        score += 10

    if stress >= 8:
        score -= 10

    score = max(0, min(100, score))

    st.metric("📈 Readiness Score", f"{score}%")

    if score < 40:
        st.warning(
            "🚨 Rescue Mode: Learn important concepts first, "
            "then practice questions."
        )

    elif score < 70:
        st.info(
            "📚 Build Mode: Focus on weak topics and active revision."
        )

    else:
        st.success(
            "🔥 Revision Mode: Practice questions and rapid recall."
        )

    st.markdown("### ✅ Recommended Cycle")

    st.write("1️⃣ Learn → 2️⃣ Make Notes → 3️⃣ Quiz → 4️⃣ Identify Weakness → 5️⃣ Revise")

# ---------- FOOTER ----------
st.divider()

st.caption(
    "AI Study Rescue | Exam Preparation Assistant | IBM SkillsBuild Project"
)