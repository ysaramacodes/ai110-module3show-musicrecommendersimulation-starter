# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.


A real world recommendation works based on user's listening habits, playlists. Spotify uses this information to make recommendations to the user on what song they potentially would like based on genre and energy. My app will lean more towards making recommendations to the user based on the genre they listen to. I chose to prioritize genre over mood because the user more than likely listens to most of the same genre so it will connect with the user more than just a change in mood. The features will include a title, artist nae, genre, mood, id, favorite genre, energy, tempo_bpm.


The app will award 3 points for a genre match and will award 1 point for a mood match. Therefore, this app will over prioritize same genre, ignoring great songs that match the user's mood.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```
Top recommendations:

1. Sunrise City — Neon Echo
   Score: 4.98
   Reasons: genre matches (pop), mood matches (happy), energy: 0.82 (target: 0.80,
           distance: 0.02)

2. Gym Hero — Max Pulse
   Score: 3.87
   Reasons: genre matches (pop), energy: 0.93 (target: 0.80, distance: 0.13)

3. Workout Anthem — Max Pulse
   Score: 3.85
   Reasons: genre matches (pop), energy: 0.95 (target: 0.80, distance: 0.15)

4. Rooftop Lights — Indigo Parade
   Score: 1.96
   Reasons: mood matches (happy), energy: 0.76 (target: 0.80, distance: 0.04)

5. Horizon Drifters — Indigo Parade
   Score: 1.90
   Reasons: mood matches (happy), energy: 0.70 (target: 0.80, distance: 0.10)

   
**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



