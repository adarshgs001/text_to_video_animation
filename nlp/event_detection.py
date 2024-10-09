def classify_event(actions):
    """
    Classifies actions into higher-level events such as meetings, celebrations, or fights.
    
    Parameters:
        actions (list): A list of verbs or actions extracted from the text.
    
    Returns:
        str: The detected event type.
    """
    # Example classification based on the actions found in the text
    if any(action in actions for action in ["meet", "gather", "talk"]):
        return "Meeting"
    elif any(action in actions for action in ["celebrate", "dance", "cheer"]):
        return "Celebration"
    elif any(action in actions for action in ["fight", "argue", "shout"]):
        return "Confrontation"
    else:
        return "General Event"
