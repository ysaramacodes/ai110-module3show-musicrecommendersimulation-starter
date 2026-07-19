from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs: List[Dict] = []
    print(f"Loading songs from {csv_path}...")
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields from strings to floats
            numeric_fields = ["energy", "tempo_bpm", "valence", "danceability", "acousticness"]
            for field in numeric_fields:
                if field in row and row[field] != "":
                    try:
                        row[field] = float(row[field])
                    except ValueError:
                        pass
            # Convert id to int
            if "id" in row and row["id"] != "":
                try:
                    row["id"] = int(row["id"])
                except ValueError:
                    pass
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song based on genre, mood, and energy match to user preferences."""
    reasons: List[str] = []
    score = 0.0

    # Genre match: +3 points
    if song.get("genre", "").lower() == user_prefs.get("genre", "").lower():
        score += 3.0
        reasons.append(f"genre matches ({song.get('genre')})")

    # Mood match: +1 point
    if song.get("mood", "").lower() == user_prefs.get("mood", "").lower():
        score += 1.0
        reasons.append(f"mood matches ({song.get('mood')})")

    # Energy closeness: up to +1 point (bonus for being close to target)
    target_energy = float(user_prefs.get("energy", 0.5))
    song_energy = float(song.get("energy", 0.5))
    energy_distance = abs(song_energy - target_energy)
    energy_bonus = max(0.0, 1.0 - energy_distance)
    score += energy_bonus
    reasons.append(f"energy: {song_energy:.2f} (target: {target_energy:.2f}, distance: {energy_distance:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs scored against user preferences with explanations."""
    # For small lists, build a scored list with a single call to score_song per song
    scored = [
        (score, song, reasons)
        for song in songs
        for (score, reasons) in [score_song(user_prefs, song)]
    ]

    # Sort by score descending and return top-k as (song, score, explanation)
    scored.sort(key=lambda x: x[0], reverse=True)
    return [
        (song, score, ", ".join(reasons))
        for score, song, reasons in scored[:k]
    ]
