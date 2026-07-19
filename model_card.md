# 🎧 Model Card: Music Recommender Simulation

======================================================================
TEST: BASELINE: Normal preferences
Profile: {'genre': 'pop', 'mood': 'happy', 'energy': 0.8}
======================================================================

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


======================================================================
TEST: CONFLICTING: High energy + sad mood
Profile: {'genre': 'pop', 'mood': 'sad', 'energy': 0.9}
======================================================================

Top recommendations:

1. Gym Hero — Max Pulse
   Score: 3.97
   Reasons: genre matches (pop), energy: 0.93 (target: 0.90, distance: 0.03)

2. Workout Anthem — Max Pulse
   Score: 3.95
   Reasons: genre matches (pop), energy: 0.95 (target: 0.90, distance: 0.05)

3. Sunrise City — Neon Echo
   Score: 3.92
   Reasons: genre matches (pop), energy: 0.82 (target: 0.90, distance: 0.08)

4. Storm Runner — Voltline
   Score: 0.99
   Reasons: energy: 0.91 (target: 0.90, distance: 0.01)

5. Electric Pulse — Neon Echo
   Score: 0.97
   Reasons: energy: 0.87 (target: 0.90, distance: 0.03)


======================================================================
TEST: CONFLICTING: Low energy + happy mood
Profile: {'genre': 'rock', 'mood': 'happy', 'energy': 0.1}
======================================================================

Top recommendations:

1. Storm Runner — Voltline
   Score: 3.19
   Reasons: genre matches (rock), energy: 0.91 (target: 0.10, distance: 0.81)

2. Horizon Drifters — Indigo Parade
   Score: 1.40
   Reasons: mood matches (happy), energy: 0.70 (target: 0.10, distance: 0.60)

3. Rooftop Lights — Indigo Parade
   Score: 1.34
   Reasons: mood matches (happy), energy: 0.76 (target: 0.10, distance: 0.66)

4. Sunrise City — Neon Echo
   Score: 1.28
   Reasons: mood matches (happy), energy: 0.82 (target: 0.10, distance: 0.72)

5. Deep Forest — Dusk Bloom
   Score: 0.85
   Reasons: energy: 0.25 (target: 0.10, distance: 0.15)


======================================================================
TEST: EXTREME: Maximum energy
Profile: {'genre': 'pop', 'mood': 'energetic', 'energy': 1.0}
======================================================================

Top recommendations:

1. Workout Anthem — Max Pulse
   Score: 3.95
   Reasons: genre matches (pop), energy: 0.95 (target: 1.00, distance: 0.05)

2. Gym Hero — Max Pulse
   Score: 3.93
   Reasons: genre matches (pop), energy: 0.93 (target: 1.00, distance: 0.07)

3. Sunrise City — Neon Echo
   Score: 3.82
   Reasons: genre matches (pop), energy: 0.82 (target: 1.00, distance: 0.18)

4. Storm Runner — Voltline
   Score: 0.91
   Reasons: energy: 0.91 (target: 1.00, distance: 0.09)

5. Electric Pulse — Neon Echo
   Score: 0.87
   Reasons: energy: 0.87 (target: 1.00, distance: 0.13)


======================================================================
TEST: EXTREME: Minimum energy
Profile: {'genre': 'jazz', 'mood': 'calm', 'energy': 0.0}
======================================================================

Top recommendations:

1. Coffee Shop Stories — Slow Stereo
   Score: 3.63
   Reasons: genre matches (jazz), energy: 0.37 (target: 0.00, distance: 0.37)

2. Smooth Streets — Slow Stereo
   Score: 3.56
   Reasons: genre matches (jazz), energy: 0.44 (target: 0.00, distance: 0.44)

3. Deep Forest — Dusk Bloom
   Score: 1.75
   Reasons: mood matches (calm), energy: 0.25 (target: 0.00, distance: 0.25)

4. Spacewalk Thoughts — Orbit Bloom
   Score: 0.72
   Reasons: energy: 0.28 (target: 0.00, distance: 0.28)

5. Library Rain — Paper Lanterns
   Score: 0.65
   Reasons: energy: 0.35 (target: 0.00, distance: 0.35)


======================================================================
TEST: UNCOMMON: Metal + romantic
Profile: {'genre': 'metal', 'mood': 'romantic', 'energy': 0.4}
======================================================================

Top recommendations:

1. Focus Flow — LoRoom
   Score: 1.00
   Reasons: energy: 0.40 (target: 0.40, distance: 0.00)

2. Midnight Coding — LoRoom
   Score: 0.98
   Reasons: energy: 0.42 (target: 0.40, distance: 0.02)

3. Study Zen — Paper Lanterns
   Score: 0.98
   Reasons: energy: 0.38 (target: 0.40, distance: 0.02)

4. Coffee Shop Stories — Slow Stereo
   Score: 0.97
   Reasons: energy: 0.37 (target: 0.40, distance: 0.03)

5. Morning Breeze — Luna Harbor
   Score: 0.96
   Reasons: energy: 0.36 (target: 0.40, distance: 0.04)


======================================================================
TEST: UNCOMMON: Classical + party
Profile: {'genre': 'classical', 'mood': 'party', 'energy': 0.95}
======================================================================

Top recommendations:

1. Workout Anthem — Max Pulse
   Score: 1.00
   Reasons: energy: 0.95 (target: 0.95, distance: 0.00)

2. Gym Hero — Max Pulse
   Score: 0.98
   Reasons: energy: 0.93 (target: 0.95, distance: 0.02)

3. Storm Runner — Voltline
   Score: 0.96
   Reasons: energy: 0.91 (target: 0.95, distance: 0.04)

4. Electric Pulse — Neon Echo
   Score: 0.92
   Reasons: energy: 0.87 (target: 0.95, distance: 0.08)

5. Sunrise City — Neon Echo
   Score: 0.87
   Reasons: energy: 0.82 (target: 0.95, distance: 0.13)


======================================================================
TEST: EDGE CASE: Empty genre
Profile: {'genre': '', 'mood': 'happy', 'energy': 0.8}
======================================================================

Top recommendations:

1. Sunrise City — Neon Echo
   Score: 1.98
   Reasons: mood matches (happy), energy: 0.82 (target: 0.80, distance: 0.02)

2. Rooftop Lights — Indigo Parade
   Score: 1.96
   Reasons: mood matches (happy), energy: 0.76 (target: 0.80, distance: 0.04)

3. Horizon Drifters — Indigo Parade
   Score: 1.90
   Reasons: mood matches (happy), energy: 0.70 (target: 0.80, distance: 0.10)

4. City Neon — LoRoom
   Score: 0.98
   Reasons: energy: 0.78 (target: 0.80, distance: 0.02)

5. Night Drive Loop — Neon Echo
   Score: 0.95
   Reasons: energy: 0.75 (target: 0.80, distance: 0.05)


======================================================================
TEST: EDGE CASE: Energy > 1.0
Profile: {'genre': 'pop', 'mood': 'happy', 'energy': 1.5}
======================================================================

Top recommendations:

1. Sunrise City — Neon Echo
   Score: 4.32
   Reasons: genre matches (pop), mood matches (happy), energy: 0.82 (target: 1.50,
           distance: 0.68)

2. Workout Anthem — Max Pulse
   Score: 3.45
   Reasons: genre matches (pop), energy: 0.95 (target: 1.50, distance: 0.55)

3. Gym Hero — Max Pulse
   Score: 3.43
   Reasons: genre matches (pop), energy: 0.93 (target: 1.50, distance: 0.57)

4. Rooftop Lights — Indigo Parade
   Score: 1.26
   Reasons: mood matches (happy), energy: 0.76 (target: 1.50, distance: 0.74)

5. Horizon Drifters — Indigo Parade
   Score: 1.20
   Reasons: mood matches (happy), energy: 0.70 (target: 1.50, distance: 0.80)

yousifsarama@MacBook-Pro ai110-module3show-musicrecommendersimulation-starter % 
yousifsarama@MacBook-Pro ai110-module3show-musicrecommendersimulation-starter % /Users/yousifsarama/ai110-module3show-musicrecommendersimulation-starter/.venv/bin/python /
Users/yousifsarama/ai110-module3show-musicrecommendersimulation-starter/tests/test_recommender.py
Traceback (most recent call last):
  File "/Users/yousifsarama/ai110-module3show-musicrecommendersimulation-starter/tests/test_recommender.py", line 1, in <module>
    from src.recommender import Song, UserProfile, Recommender
ModuleNotFoundError: No module named 'src'
yousifsarama@MacBook-Pro ai110-module3show-musicrecommendersimulation-starter % /Users/yousifsarama/ai110-module3show-musicrecommendersimulation-starter/.venv/bin/python /
Users/yousifsarama/ai110-module3show-musicrecommendersimulation-starter/src/main.py
Loading songs from data/songs.csv...

======================================================================
TEST: BASELINE: Normal preferences
Profile: {'genre': 'pop', 'mood': 'happy', 'energy': 0.8}
======================================================================

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


======================================================================
TEST: CONFLICTING: Pop genre + intense mood (pop usually happy)
Profile: {'genre': 'pop', 'mood': 'intense', 'energy': 0.9}
======================================================================

Top recommendations:

1. Gym Hero — Max Pulse
   Score: 4.97
   Reasons: genre matches (pop), mood matches (intense), energy: 0.93 (target: 0.90,
           distance: 0.03)

2. Workout Anthem — Max Pulse
   Score: 4.95
   Reasons: genre matches (pop), mood matches (intense), energy: 0.95 (target: 0.90,
           distance: 0.05)

3. Sunrise City — Neon Echo
   Score: 3.92
   Reasons: genre matches (pop), energy: 0.82 (target: 0.90, distance: 0.08)

4. Storm Runner — Voltline
   Score: 1.99
   Reasons: mood matches (intense), energy: 0.91 (target: 0.90, distance: 0.01)

5. Electric Pulse — Neon Echo
   Score: 0.97
   Reasons: energy: 0.87 (target: 0.90, distance: 0.03)


======================================================================
TEST: CONFLICTING: Low energy + intense mood (rock usually high-energy)
Profile: {'genre': 'rock', 'mood': 'intense', 'energy': 0.1}
======================================================================

Top recommendations:

1. Storm Runner — Voltline
   Score: 4.19
   Reasons: genre matches (rock), mood matches (intense), energy: 0.91 (target:
           0.10, distance: 0.81)

2. Quiet Ballad — Stone Path
   Score: 3.80
   Reasons: genre matches (rock), energy: 0.30 (target: 0.10, distance: 0.20)

3. Gym Hero — Max Pulse
   Score: 1.17
   Reasons: mood matches (intense), energy: 0.93 (target: 0.10, distance: 0.83)

4. Workout Anthem — Max Pulse
   Score: 1.15
   Reasons: mood matches (intense), energy: 0.95 (target: 0.10, distance: 0.85)

5. Deep Forest — Dusk Bloom
   Score: 0.85
   Reasons: energy: 0.25 (target: 0.10, distance: 0.15)


======================================================================
TEST: EXTREME: Maximum energy
Profile: {'genre': 'electropop', 'mood': 'upbeat', 'energy': 1.0}
======================================================================

Top recommendations:

1. Electric Pulse — Neon Echo
   Score: 4.87
   Reasons: genre matches (electropop), mood matches (upbeat), energy: 0.87 (target:
           1.00, distance: 0.13)

2. Workout Anthem — Max Pulse
   Score: 0.95
   Reasons: energy: 0.95 (target: 1.00, distance: 0.05)

3. Gym Hero — Max Pulse
   Score: 0.93
   Reasons: energy: 0.93 (target: 1.00, distance: 0.07)

4. Storm Runner — Voltline
   Score: 0.91
   Reasons: energy: 0.91 (target: 1.00, distance: 0.09)

5. Sunrise City — Neon Echo
   Score: 0.82
   Reasons: energy: 0.82 (target: 1.00, distance: 0.18)


======================================================================
TEST: EXTREME: Minimum energy
Profile: {'genre': 'ambient', 'mood': 'calm', 'energy': 0.0}
======================================================================

Top recommendations:

1. Deep Forest — Dusk Bloom
   Score: 4.75
   Reasons: genre matches (ambient), mood matches (calm), energy: 0.25 (target:
           0.00, distance: 0.25)

2. Spacewalk Thoughts — Orbit Bloom
   Score: 3.72
   Reasons: genre matches (ambient), energy: 0.28 (target: 0.00, distance: 0.28)

3. Quiet Ballad — Stone Path
   Score: 0.70
   Reasons: energy: 0.30 (target: 0.00, distance: 0.30)

4. Library Rain — Paper Lanterns
   Score: 0.65
   Reasons: energy: 0.35 (target: 0.00, distance: 0.35)

5. Morning Breeze — Luna Harbor
   Score: 0.64
   Reasons: energy: 0.36 (target: 0.00, distance: 0.36)


======================================================================
TEST: UNCOMMON: Synthwave + happy (synthwave usually moody)
Profile: {'genre': 'synthwave', 'mood': 'happy', 'energy': 0.5}
======================================================================

Top recommendations:

1. Neon Smile — Glow State
   Score: 4.82
   Reasons: genre matches (synthwave), mood matches (happy), energy: 0.68 (target:
           0.50, distance: 0.18)

2. Night Drive Loop — Neon Echo
   Score: 3.75
   Reasons: genre matches (synthwave), energy: 0.75 (target: 0.50, distance: 0.25)

3. City Neon — LoRoom
   Score: 3.72
   Reasons: genre matches (synthwave), energy: 0.78 (target: 0.50, distance: 0.28)

4. Horizon Drifters — Indigo Parade
   Score: 1.80
   Reasons: mood matches (happy), energy: 0.70 (target: 0.50, distance: 0.20)

5. Rooftop Lights — Indigo Parade
   Score: 1.74
   Reasons: mood matches (happy), energy: 0.76 (target: 0.50, distance: 0.26)


======================================================================
TEST: UNCOMMON: Rock + relaxed (rock usually intense)
Profile: {'genre': 'rock', 'mood': 'relaxed', 'energy': 0.3}
======================================================================

Top recommendations:

1. Quiet Ballad — Stone Path
   Score: 5.00
   Reasons: genre matches (rock), mood matches (relaxed), energy: 0.30 (target:
           0.30, distance: 0.00)

2. Storm Runner — Voltline
   Score: 3.39
   Reasons: genre matches (rock), energy: 0.91 (target: 0.30, distance: 0.61)

3. Morning Breeze — Luna Harbor
   Score: 1.94
   Reasons: mood matches (relaxed), energy: 0.36 (target: 0.30, distance: 0.06)

4. Coffee Shop Stories — Slow Stereo
   Score: 1.93
   Reasons: mood matches (relaxed), energy: 0.37 (target: 0.30, distance: 0.07)

5. Smooth Streets — Slow Stereo
   Score: 1.86
   Reasons: mood matches (relaxed), energy: 0.44 (target: 0.30, distance: 0.14)


======================================================================
TEST: EDGE CASE: Empty genre
Profile: {'genre': '', 'mood': 'happy', 'energy': 0.8}
======================================================================

Top recommendations:

1. Sunrise City — Neon Echo
   Score: 1.98
   Reasons: mood matches (happy), energy: 0.82 (target: 0.80, distance: 0.02)

2. Rooftop Lights — Indigo Parade
   Score: 1.96
   Reasons: mood matches (happy), energy: 0.76 (target: 0.80, distance: 0.04)

3. Horizon Drifters — Indigo Parade
   Score: 1.90
   Reasons: mood matches (happy), energy: 0.70 (target: 0.80, distance: 0.10)

4. Neon Smile — Glow State
   Score: 1.88
   Reasons: mood matches (happy), energy: 0.68 (target: 0.80, distance: 0.12)

5. City Neon — LoRoom
   Score: 0.98
   Reasons: energy: 0.78 (target: 0.80, distance: 0.02)


======================================================================
TEST: EDGE CASE: Energy > 1.0
Profile: {'genre': 'pop', 'mood': 'happy', 'energy': 1.5}
======================================================================

Top recommendations:

1. Sunrise City — Neon Echo
   Score: 4.32
   Reasons: genre matches (pop), mood matches (happy), energy: 0.82 (target: 1.50,
           distance: 0.68)

2. Workout Anthem — Max Pulse
   Score: 3.45
   Reasons: genre matches (pop), energy: 0.95 (target: 1.50, distance: 0.55)

3. Gym Hero — Max Pulse
   Score: 3.43
   Reasons: genre matches (pop), energy: 0.93 (target: 1.50, distance: 0.57)

4. Rooftop Lights — Indigo Parade
   Score: 1.26
   Reasons: mood matches (happy), energy: 0.76 (target: 1.50, distance: 0.74)

5. Horizon Drifters — Indigo Parade
   Score: 1.20
   Reasons: mood matches (happy), energy: 0.70 (target: 1.50, distance: 0.80)

yousifsarama@MacBook-Pro ai110-module3show-musicrecommendersimulation-starter % /Users/yousifsarama/ai110-module3show-musicrecommendersimulation-starter/.venv/bin/python /
Users/yousifsarama/ai110-module3show-musicrecommendersimulation-starter/src/main.py
Loading songs from data/songs.csv...

======================================================================
TEST: BASELINE: Normal preferences
Profile: {'genre': 'pop', 'mood': 'happy', 'energy': 0.8}
======================================================================

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


======================================================================
TEST: CONFLICTING: Pop genre + intense mood (pop usually happy)
Profile: {'genre': 'pop', 'mood': 'intense', 'energy': 0.9}
======================================================================

Top recommendations:

1. Gym Hero — Max Pulse
   Score: 4.97
   Reasons: genre matches (pop), mood matches (intense), energy: 0.93 (target: 0.90,
           distance: 0.03)

2. Workout Anthem — Max Pulse
   Score: 4.95
   Reasons: genre matches (pop), mood matches (intense), energy: 0.95 (target: 0.90,
           distance: 0.05)

3. Sunrise City — Neon Echo
   Score: 3.92
   Reasons: genre matches (pop), energy: 0.82 (target: 0.90, distance: 0.08)

4. Storm Runner — Voltline
   Score: 1.99
   Reasons: mood matches (intense), energy: 0.91 (target: 0.90, distance: 0.01)

5. Electric Pulse — Neon Echo
   Score: 0.97
   Reasons: energy: 0.87 (target: 0.90, distance: 0.03)


======================================================================
TEST: CONFLICTING: Low energy + intense mood (rock usually high-energy)
Profile: {'genre': 'rock', 'mood': 'intense', 'energy': 0.1}
======================================================================

Top recommendations:

1. Storm Runner — Voltline
   Score: 4.19
   Reasons: genre matches (rock), mood matches (intense), energy: 0.91 (target:
           0.10, distance: 0.81)

2. Quiet Ballad — Stone Path
   Score: 3.80
   Reasons: genre matches (rock), energy: 0.30 (target: 0.10, distance: 0.20)

3. Gym Hero — Max Pulse
   Score: 1.17
   Reasons: mood matches (intense), energy: 0.93 (target: 0.10, distance: 0.83)

4. Workout Anthem — Max Pulse
   Score: 1.15
   Reasons: mood matches (intense), energy: 0.95 (target: 0.10, distance: 0.85)

5. Deep Forest — Dusk Bloom
   Score: 0.85
   Reasons: energy: 0.25 (target: 0.10, distance: 0.15)


======================================================================
TEST: EXTREME: Maximum energy
Profile: {'genre': 'electropop', 'mood': 'upbeat', 'energy': 1.0}
======================================================================

Top recommendations:

1. Electric Pulse — Neon Echo
   Score: 4.87
   Reasons: genre matches (electropop), mood matches (upbeat), energy: 0.87 (target:
           1.00, distance: 0.13)

2. Workout Anthem — Max Pulse
   Score: 0.95
   Reasons: energy: 0.95 (target: 1.00, distance: 0.05)

3. Gym Hero — Max Pulse
   Score: 0.93
   Reasons: energy: 0.93 (target: 1.00, distance: 0.07)

4. Storm Runner — Voltline
   Score: 0.91
   Reasons: energy: 0.91 (target: 1.00, distance: 0.09)

5. Sunrise City — Neon Echo
   Score: 0.82
   Reasons: energy: 0.82 (target: 1.00, distance: 0.18)


======================================================================
TEST: EXTREME: Minimum energy
Profile: {'genre': 'ambient', 'mood': 'calm', 'energy': 0.0}
======================================================================

Top recommendations:

1. Deep Forest — Dusk Bloom
   Score: 4.75
   Reasons: genre matches (ambient), mood matches (calm), energy: 0.25 (target:
           0.00, distance: 0.25)

2. Spacewalk Thoughts — Orbit Bloom
   Score: 3.72
   Reasons: genre matches (ambient), energy: 0.28 (target: 0.00, distance: 0.28)

3. Quiet Ballad — Stone Path
   Score: 0.70
   Reasons: energy: 0.30 (target: 0.00, distance: 0.30)

4. Library Rain — Paper Lanterns
   Score: 0.65
   Reasons: energy: 0.35 (target: 0.00, distance: 0.35)

5. Morning Breeze — Luna Harbor
   Score: 0.64
   Reasons: energy: 0.36 (target: 0.00, distance: 0.36)


======================================================================
TEST: UNCOMMON: Synthwave + happy (synthwave usually moody)
Profile: {'genre': 'synthwave', 'mood': 'happy', 'energy': 0.5}
======================================================================

Top recommendations:

1. Neon Smile — Glow State
   Score: 4.82
   Reasons: genre matches (synthwave), mood matches (happy), energy: 0.68 (target:
           0.50, distance: 0.18)

2. Night Drive Loop — Neon Echo
   Score: 3.75
   Reasons: genre matches (synthwave), energy: 0.75 (target: 0.50, distance: 0.25)

3. City Neon — LoRoom
   Score: 3.72
   Reasons: genre matches (synthwave), energy: 0.78 (target: 0.50, distance: 0.28)

4. Horizon Drifters — Indigo Parade
   Score: 1.80
   Reasons: mood matches (happy), energy: 0.70 (target: 0.50, distance: 0.20)

5. Rooftop Lights — Indigo Parade
   Score: 1.74
   Reasons: mood matches (happy), energy: 0.76 (target: 0.50, distance: 0.26)


======================================================================
TEST: UNCOMMON: Rock + relaxed (rock usually intense)
Profile: {'genre': 'rock', 'mood': 'relaxed', 'energy': 0.3}
======================================================================

Top recommendations:

1. Quiet Ballad — Stone Path
   Score: 5.00
   Reasons: genre matches (rock), mood matches (relaxed), energy: 0.30 (target:
           0.30, distance: 0.00)

2. Storm Runner — Voltline
   Score: 3.39
   Reasons: genre matches (rock), energy: 0.91 (target: 0.30, distance: 0.61)

3. Morning Breeze — Luna Harbor
   Score: 1.94
   Reasons: mood matches (relaxed), energy: 0.36 (target: 0.30, distance: 0.06)

4. Coffee Shop Stories — Slow Stereo
   Score: 1.93
   Reasons: mood matches (relaxed), energy: 0.37 (target: 0.30, distance: 0.07)

5. Smooth Streets — Slow Stereo
   Score: 1.86
   Reasons: mood matches (relaxed), energy: 0.44 (target: 0.30, distance: 0.14)


======================================================================
TEST: EDGE CASE: Empty genre
Profile: {'genre': '', 'mood': 'happy', 'energy': 0.8}
======================================================================

Top recommendations:

1. Sunrise City — Neon Echo
   Score: 1.98
   Reasons: mood matches (happy), energy: 0.82 (target: 0.80, distance: 0.02)

2. Rooftop Lights — Indigo Parade
   Score: 1.96
   Reasons: mood matches (happy), energy: 0.76 (target: 0.80, distance: 0.04)

3. Horizon Drifters — Indigo Parade
   Score: 1.90
   Reasons: mood matches (happy), energy: 0.70 (target: 0.80, distance: 0.10)

4. Neon Smile — Glow State
   Score: 1.88
   Reasons: mood matches (happy), energy: 0.68 (target: 0.80, distance: 0.12)

5. City Neon — LoRoom
   Score: 0.98
   Reasons: energy: 0.78 (target: 0.80, distance: 0.02)


======================================================================
TEST: EDGE CASE: Energy > 1.0
Profile: {'genre': 'pop', 'mood': 'happy', 'energy': 1.5}
======================================================================

Top recommendations:

1. Sunrise City — Neon Echo
   Score: 4.32
   Reasons: genre matches (pop), mood matches (happy), energy: 0.82 (target: 1.50,
           distance: 0.68)

2. Workout Anthem — Max Pulse
   Score: 3.45
   Reasons: genre matches (pop), energy: 0.95 (target: 1.50, distance: 0.55)

3. Gym Hero — Max Pulse
   Score: 3.43
   Reasons: genre matches (pop), energy: 0.93 (target: 1.50, distance: 0.57)

4. Rooftop Lights — Indigo Parade
   Score: 1.26
   Reasons: mood matches (happy), energy: 0.76 (target: 1.50, distance: 0.74)

5. Horizon Drifters — Indigo Parade
   Score: 1.20
   Reasons: mood matches (happy), energy: 0.70 (target: 1.50, distance: 0.80)






## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  


WaveLength




---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

My recommender is deigned to create a list of potential songs the user might like based on their genre and energy. However it does favor genre more than energy. This recommender assumes that the listener would like music that is the same genre which is good for people who just listen to one genre. However most people listen to a range of genres.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The scoring is based on genre, mood and energy. This recommender gives 3 points for a genre match, 1 point for an energy match and a 1 point for a mood match. Based on this we can tell that this recommender has a bias towards genre.
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

There are 20 songs in the catalog. The genres are pop, anthem, lofi, zen, rock, synthwave, ambient, indie pop, jazz, folk, electropop. There is definetley parts of musical taste missing in the dataset.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

This system is best for users with clear genre preferences(pop,rock,jazz).
This system is simple to understand and it always favor genre so the results are never suprising.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One weakness I discovered during this experiment is that this system ignores 7 out of 10 song attributes. This means users whose music taste that extends beyond genre/mood/energy are invisible. This system is very simple and it biases toward users with simple song preferences.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested 9 different user profiles. The profiles I tested where pop, rock, energy extreme and uncommon. I checked to see if the scoring was correct and the list was returning the correct songs. Nothing suprised me since this recommender heavily favours genre. 




---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I would include all of the 10 music attributes so it would recommend the best posible songs to the user and making sure it doesnt favour any attribute more than another. Instead of just listing matches, explain what was prioritized like genre in this case. The way to improve diversity is give a point for each attribute instead of 3. 
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  




I learned that recommender systems are very difficult because it is very hard to accomodate for everyone without using alot of code. Somwthing interesting I discovered is how sensitive the recommender system is based on the weight scoring. This changed the way I think about apps like spotify because it somehow recommends good songs even though the genre is not the same.