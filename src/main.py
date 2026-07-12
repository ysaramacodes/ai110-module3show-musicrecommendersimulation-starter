"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    import textwrap
    print("\nTop recommendations:\n")
    for i, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        title = song.get("title", "<unknown>")
        artist = song.get("artist")
        header = f"{i}. {title}"
        if artist:
            header += f" — {artist}"
        print(header)
        print(f"   Score: {score:.2f}")
        wrapped = textwrap.fill(explanation, width=72, subsequent_indent=' ' * 11)
        print(f"   Reasons: {wrapped}")
        print()


if __name__ == "__main__":
    main()
