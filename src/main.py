"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs

Usage:
  python src/main.py              # Run all tests with detailed view
  python src/main.py summary      # Run all tests with summary table
  python src/main.py <num>        # Run single test (1-9)
  python src/main.py <num> table  # Run single test with table view
"""

from recommender import load_songs, recommend_songs
import textwrap


def print_recommendations(user_prefs: dict, songs: list, profile_name: str = "") -> None:
    """Print recommendations in detailed format."""
    if profile_name:
        print(f"\n{'='*75}")
        print(f"TEST: {profile_name}")
        print(f"Profile: {user_prefs}")
        print(f"{'='*75}")

    recommendations = recommend_songs(user_prefs, songs, k=5)
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


def print_table_view(user_prefs: dict, songs: list, profile_num: int, profile_name: str = "", use_tabulate: bool = True) -> None:
    """Print recommendations in formatted table with reasons.

    Args:
        user_prefs: User preference dictionary
        songs: List of songs
        profile_num: Profile number for display
        profile_name: Profile name for display
        use_tabulate: If True, use tabulate library; if False, use ASCII formatting
    """
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\n{'='*130}")
    print(f"Profile {profile_num}: {profile_name}")
    print(f"User Preferences: Genre={user_prefs.get('genre') or '(any)'}, Mood={user_prefs.get('mood')}, Energy={user_prefs.get('energy')}")
    print(f"{'='*130}\n")

    # Build table data
    table_data = []
    for i, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        title = song.get("title", "<unknown>")
        artist = song.get("artist", "—")

        table_data.append([
            i,
            title,
            artist,
            f"{score:.2f}",
            explanation
        ])

    headers = ["Rank", "Song Title", "Artist", "Score", "Reasons for Recommendation"]

    if use_tabulate:
        try:
            from tabulate import tabulate
            print(tabulate(table_data, headers=headers, tablefmt="grid", maxcolwidths=[6, 25, 20, 8, 60]))
        except ImportError:
            # Fallback to ASCII formatting if tabulate not available
            print_ascii_table(table_data, headers)
    else:
        print_ascii_table(table_data, headers)

    print()


def print_ascii_table(table_data: list, headers: list) -> None:
    """Print a formatted ASCII table with word wrapping for long content."""
    import textwrap

    # Column widths
    col_widths = [6, 25, 20, 8, 60]

    # Print header
    header_row = " | ".join(f"{h:<{col_widths[i]}}" for i, h in enumerate(headers))
    print(header_row)
    print("-" * len(header_row))

    # Print rows with wrapping for reasons column
    for row in table_data:
        rank, title, artist, score, reasons = row

        # Wrap the reasons text
        wrapped_reasons = textwrap.wrap(reasons, width=col_widths[4])

        if not wrapped_reasons:
            wrapped_reasons = [""]

        # Print first line with all columns
        first_line = " | ".join([
            f"{str(rank):<{col_widths[0]}}",
            f"{title:<{col_widths[1]}}",
            f"{artist:<{col_widths[2]}}",
            f"{score:<{col_widths[3]}}",
            f"{wrapped_reasons[0]:<{col_widths[4]}}"
        ])
        print(first_line)

        # Print continuation lines for wrapped reasons
        for continuation in wrapped_reasons[1:]:
            cont_line = " | ".join([
                f"{'': <{col_widths[0]}}",
                f"{'': <{col_widths[1]}}",
                f"{'': <{col_widths[2]}}",
                f"{'': <{col_widths[3]}}",
                f"{continuation:<{col_widths[4]}}"
            ])
            print(cont_line)

        print("-" * len(header_row))


def print_summary_table(test_profiles: list, songs: list) -> None:
    """Print a summary table of all profiles and their top recommendation."""
    print(f"\n{'='*110}")
    print("SUMMARY: Top Recommendation for Each Profile")
    print(f"{'='*110}\n")

    print(f"{'#':<3} {'Profile Type':<35} {'Genre':<15} {'Mood':<12} {'Energy':<8} {'Top Song':<25} {'Score':<7}")
    print("-" * 110)

    for idx, (prefs, name) in enumerate(test_profiles, start=1):
        recommendations = recommend_songs(prefs, songs, k=1)

        if recommendations:
            song, score, _ = recommendations[0]
            song_title = song.get("title", "unknown")[:23]
            genre = prefs.get("genre", "—")[:13] or "—"
            mood = prefs.get("mood", "—")[:10] or "—"
            energy = f"{prefs.get('energy', 0):.1f}" if prefs.get('energy') is not None else "—"
        else:
            song_title = "N/A"
            score = 0
            genre = prefs.get("genre", "—")
            mood = prefs.get("mood", "—")
            energy = str(prefs.get("energy", "—"))

        profile_type = name.split(":")[0][:33]
        print(f"{idx:<3} {profile_type:<35} {genre:<15} {mood:<12} {energy:<8} {song_title:<25} {score:>6.2f}")

    print(f"{'='*110}\n")


def main() -> None:
    import sys
    songs = load_songs("data/songs.csv")

    # Test suite of adversarial/edge case profiles
    test_profiles = [
        (
            {"genre": "pop", "mood": "happy", "energy": 0.8},
            "BASELINE: Normal preferences"
        ),
        (
            {"genre": "pop", "mood": "intense", "energy": 0.9},
            "CONFLICTING: Pop genre + intense mood (pop usually happy)"
        ),
        (
            {"genre": "rock", "mood": "intense", "energy": 0.1},
            "CONFLICTING: Low energy + intense mood (rock usually high-energy)"
        ),
        (
            {"genre": "electropop", "mood": "upbeat", "energy": 1.0},
            "EXTREME: Maximum energy"
        ),
        (
            {"genre": "ambient", "mood": "calm", "energy": 0.0},
            "EXTREME: Minimum energy"
        ),
        (
            {"genre": "synthwave", "mood": "happy", "energy": 0.5},
            "UNCOMMON: Synthwave + happy (synthwave usually moody)"
        ),
        (
            {"genre": "rock", "mood": "relaxed", "energy": 0.3},
            "UNCOMMON: Rock + relaxed (rock usually intense)"
        ),
        (
            {"genre": "", "mood": "happy", "energy": 0.8},
            "EDGE CASE: Empty genre"
        ),
        (
            {"genre": "pop", "mood": "happy", "energy": 1.5},
            "EDGE CASE: Energy > 1.0"
        ),
    ]

    # Parse command-line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if arg == "summary":
            # Show summary table for all profiles
            print_summary_table(test_profiles, songs)
        elif arg == "help":
            print(__doc__)
        else:
            # Run single test
            try:
                test_num = int(arg) - 1
                if 0 <= test_num < len(test_profiles):
                    prefs, name = test_profiles[test_num]

                    if len(sys.argv) > 2 and sys.argv[2] == "table":
                        print_table_view(prefs, songs, test_num + 1, name)
                    else:
                        print_recommendations(prefs, songs, name)
                else:
                    print(f"Test {arg} not found (1-{len(test_profiles)})")
            except ValueError:
                print(f"Invalid argument: {arg}")
                print("Usage: python src/main.py [summary|help|<num>]")
    else:
        # Default: run all tests with summary
        print_summary_table(test_profiles, songs)
        print("\nRun 'python src/main.py <num>' for detailed output (e.g., 'python src/main.py 1')")
        print("Run 'python src/main.py help' for more options\n")


if __name__ == "__main__":
    main()
