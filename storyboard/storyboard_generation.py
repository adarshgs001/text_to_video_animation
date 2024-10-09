def generate_storyboard(entities, actions, sentiment):
    """
    Generate a simple storyboard based on the extracted entities, actions, and sentiment.
    """
    storyboard = {
        "entities": entities,
        "actions": actions,
        "sentiment": sentiment
    }
    return storyboard
