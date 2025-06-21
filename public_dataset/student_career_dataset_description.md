# 🎓 Student Career Prediction Dataset

Welcome to the **Student Career Prediction Dataset** — a large-scale synthetic dataset designed to model, predict, and understand the relationship between high school student profiles and their potential future careers. This dataset simulates **10,000 students** and maps them to over **100+ diverse career paths**, making it ideal for **multi-class classification**, **recommender systems**, or **educational analytics research**.

---

## 🌍 Dataset Overview

| Property            | Value                               |
|---------------------|-------------------------------------|
| Rows                | 10,000                              |
| Features            | 20 input features + 1 target label  |
| Target Variable     | `target_career` (100+ classes)      |
| File Format         | CSV + Markdown Documentation        |
| Use Cases           | Classification, Career Guidance, Recommender Systems |

---

## 🎯 Prediction Goal

> Given a high school student’s academic scores, interests, and behavioral traits, **predict the most likely career path** from over 100 real-world professions spanning technology, medicine, law, business, arts, trades, education, and more.

---

## 🧠 Features Description

| Feature Name           | Type        | Description                                                                 |
|------------------------|-------------|-----------------------------------------------------------------------------|
| `gender`               | Categorical | Gender of the student (`Male`, `Female`, `Other`)                          |
| `age`                  | Integer     | Age (between 16–19)                                                         |
| `gpa`                  | Float       | Grade Point Average (0.0 to 4.0)                                            |
| `math_score`           | Integer     | Score in Mathematics (40–100)                                              |
| `physics_score`        | Integer     | Score in Physics (40–100)                                                  |
| `chemistry_score`      | Integer     | Score in Chemistry (40–100)                                                |
| `biology_score`        | Integer     | Score in Biology (40–100)                                                  |
| `cs_score`             | Integer     | Score in Computer Science (40–100)                                         |
| `english_score`        | Integer     | Score in English (40–100)                                                  |
| `social_studies_score` | Integer     | Score in Social Studies (40–100)                                           |
| `volunteer_hours`      | Integer     | Total hours spent volunteering (0–100)                                     |
| `leadership_score`     | Integer     | Leadership trait score (0–9)                                               |
| `curiosity_score`      | Integer     | Intellectual curiosity score (0–9)                                         |
| `problem_solving_score`| Integer     | Critical thinking score (0–9)                                              |
| `attendance_rate`      | Float       | Percentage of school attendance (0.70–1.00)                                |
| `parental_education`   | Categorical | Highest education level of parents (`None` to `PhD`)                       |
| `school_type`          | Categorical | Type of school (`Public`, `Private`)                                       |
| `interest_medicine`    | Integer     | Interest in medicine/health (0–9)                                          |
| `interest_tech`        | Integer     | Interest in technology and engineering (0–9)                               |
| `interest_law`         | Integer     | Interest in law and political science (0–9)                                |
| `target_career`        | Categorical | 🎯 The predicted career path (100+ possibilities)                          |

---

## 🧪 Sample Target Careers

Here's a sample of the 100+ possible careers:

- 👩‍⚕️ Doctor, Nurse, Pharmacist, Psychologist, Veterinarian  
- 🧠 Data Scientist, Software Engineer, AI Researcher, Game Developer  
- ⚖️ Lawyer, Judge, Politician, Policy Analyst  
- 📈 Accountant, Entrepreneur, Financial Analyst, Marketing Manager  
- 🎨 Artist, Filmmaker, Journalist, Writer, Music Producer  
- 👨‍🏫 Teacher, Professor, Education Administrator  
- 🛠 Mechanic, Electrician, Carpenter, HVAC Technician  
- 🎮 E-sports Player, UX Designer, Content Creator, Drone Operator

> The target label is assigned using a **heuristic logic** based on student scores, interests, and behavior — mimicking how academic and personality indicators influence career pathways.

---

## 🔍 Use Cases

This dataset is perfect for:

- 📊 **Multi-class classification modeling** (100+ classes)
- 🎯 **AI-based career guidance systems**
- 🤖 **Recommender systems** (suggest top-N career paths)
- 🧬 **Behavioral prediction** based on academic performance
- 🧠 **Explainable AI** for understanding model decisions in education

---

## 💡 Challenge Ideas

1. **Train a classifier** to predict careers using XGBoost, LightGBM, or Neural Networks.
2. **Use SHAP or LIME** to explain why certain features lead to specific career predictions.
3. **Build a web app** where students input scores and get career recommendations.
4. **Cluster students** into groups and analyze career trajectories.

---

## 🛠 Technical Notes

- Data is fully synthetic but mirrors real-world academic patterns.
- Built using controlled randomness + scoring heuristics.
- No PII or sensitive information — safe for public release & modeling.

---

## 📂 Files

- `student_career_prediction_dataset.csv` — 10,000 rows of student records.
- `student_career_dataset_description.md` — This documentation.

---

## 👏 Credits

Dataset generated with ❤️ by Kao Panboonyuen.

---

Happy Modeling! 🚀
