# Define video settings
width, height = 1080, 1920  # Portrait resolution
fps = 24

# Define each scene's text and duration (in seconds)
scenes = [
    {"text": "Why does a blockchain need tokens?", "duration": 5},
    {"text": "Tokens, or coins, manage state changes on the blockchain.", "duration": 10},
    {"text": "Every transaction is a state change:\ntokens move from one address to another.", "duration": 10},
    {"text": "Transactions also carry data—state changes update this data\nin an immutable system.", "duration": 10},
    {"text": "Technically, a blockchain doesn’t need coins to operate.", "duration": 10},
    {"text": "But without tokens, another mechanism must verify transactions\nand manage state changes securely.", "duration": 10},
    {"text": "Tokens are essential—they’re more than just currency!", "duration": 5}
]

# Function to create a scene clip
def create_scene(text, duration):
    # Create a background clip (solid color)
    bg_clip = ColorClip(size=(width, height), color=(30, 30, 30), duration=duration)
    
    # Create the text clip
    txt_clip = TextClip(text,
                        fontsize=70,
                        color='white',
                        font='Arial-Bold',
                        size=(width - 100, None),
                        method='caption',
                        align='center')
    txt_clip = txt_clip.set_duration(duration).set_position('center')
    
    # Composite text on background
    scene = CompositeVideoClip([bg_clip, txt_clip])
    return scene

# Create list of scene clips
clips = [create_scene(scene["text"], scene["duration"]) for scene in scenes]

# Optionally, add a short crossfade between clips
clips_with_transitions = []
for i, clip in enumerate(clips):
    if i > 0:
        # crossfadein 0.5 seconds for each clip except the first
        clip = clip.crossfadein(0.5)
    clips_with_transitions.append(clip)

# Concatenate all clips
final_video = concatenate_videoclips(clips_with_transitions, method="compose")

# Write the video file
final_video.write_videofile("blockchain_tokens_explained.mp4", fps=fps)
