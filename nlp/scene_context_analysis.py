def analyze_scene_context(entities, actions):
    """
    Detects interactions between entities based on actions.
    
    Parameters:
        entities (list): A list of entities detected in the text.
        actions (list): A list of actions (verbs) extracted from the text.
    
    Returns:
        list: A list of interactions between entities.
    """
    interactions = []

    for action in actions:
        for entity in entities:
            if entity[1] == "PERSON":
                interactions.append(f"{entity[0]} is involved in {action}")
    
    return interactions
