from .verb_extraction import extract_verbs
from .event_detection import classify_event
from .scene_context_analysis import analyze_scene_context

def detect_actions(text, entities):
    """
    Detects actions, classifies events, and analyzes scene context.
    
    Parameters:
        text (str): The input text.
        entities (list): A list of entities detected in the text.
    
    Returns:
        dict: A dictionary containing actions, events, and scene context.
    """
    # Step 1: Extract verbs (actions)
    verbs = extract_verbs(text)

    # Step 2: Classify the event based on actions
    actions = [verb[0] for verb in verbs]
    event = classify_event(actions)

    # Step 3: Analyze the scene context for interactions between entities and actions
    scene_context = analyze_scene_context(entities, actions)

    return {
        "actions": verbs,
        "event": event,
        "scene_context": scene_context
    }
