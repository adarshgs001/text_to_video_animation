# from flask import Flask, render_template, request
# import webbrowser
# import os
# from nlp.entity_recognition import extract_entities
# from nlp.action_detection import detect_actions
# from nlp.sentiment_analysis import analyze_sentiment
# from storyboard.storyboard_generation import generate_storyboard
# from animation.animation_generator import generate_frames, generate_video_from_frames, clear_frames

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         # Get user input from the form
#         input_text = request.form["input_text"]

#         # Extract entities (with language and coreference resolution support)
#         entities = extract_entities(
#             input_text, 
#             language="en",           # You can change this based on user input for multilingual support
#             use_coref=True           # Toggle coreference resolution
#         )

#         # Detect actions in the text
#         actions = detect_actions(input_text)

#         # Analyze sentiment of the input text
#         sentiment = analyze_sentiment(input_text)

#         # Generate the storyboard
#         storyboard = generate_storyboard(entities, actions, sentiment)

#         # Clear old frames
#         clear_frames()

#         # Generate animation frames based on the storyboard
#         generate_frames(storyboard)

#         # Convert frames to video and save to the static folder
#         generate_video_from_frames("static/animation_video.mp4")

#         # Pass the generated video and other data to the template
#         return render_template("index.html", 
#                                input_text=input_text, 
#                                entities=entities, 
#                                actions=actions, 
#                                sentiment=sentiment, 
#                                video_path="static/animation_video.mp4")

#     return render_template("index.html")

# if __name__ == "__main__":
#     # Only open the browser once, not during the reloader process
#     if os.getenv('WERKZEUG_RUN_MAIN') == 'true':  # Only open browser on initial run
#         webbrowser.open("http://127.0.0.1:5001/")

#     app.run(host="0.0.0.0", port=5001, debug=True)











from flask import Flask, render_template, request
import webbrowser
import os
from nlp.entity_recognition import extract_entities
from nlp.action_detection import detect_actions
from nlp.sentiment_analysis import analyze_sentiment
from storyboard.storyboard_generation import generate_storyboard
from animation.animation_generator import generate_frames, generate_video_from_frames, clear_frames

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form["input_text"]

        # Perform entity recognition
        entities = extract_entities(input_text)

        # Detect actions and classify events
        actions_info = detect_actions(input_text, entities)
        actions = actions_info["actions"]
        event = actions_info["event"]
        scene_context = actions_info["scene_context"]

        # Analyze sentiment
        sentiment = analyze_sentiment(input_text)

        # Generate the storyboard
        storyboard = generate_storyboard(entities, actions, sentiment)

        # Clear old frames
        clear_frames()

        # Generate frames and video
        generate_frames(storyboard)
        generate_video_from_frames("static/animation_video.mp4")

        return render_template("index.html", 
                               input_text=input_text, 
                               entities=entities, 
                               actions=actions, 
                               event=event, 
                               scene_context=scene_context, 
                               sentiment=sentiment, 
                               video_path="static/animation_video.mp4")

    return render_template("index.html")

if __name__ == "__main__":
    if os.getenv('WERKZEUG_RUN_MAIN') == 'true':
        webbrowser.open("http://127.0.0.1:5001/")
    app.run(host="0.0.0.0", port=5001, debug=True)
