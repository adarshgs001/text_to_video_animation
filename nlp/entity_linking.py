import wikipedia

def entity_linking(entities):
    linked_entities = []
    for entity in entities:
        try:
            summary = wikipedia.summary(entity[0], sentences=1)  # Get Wikipedia summary
            linked_entities.append((entity[0], entity[1], summary))
        except wikipedia.exceptions.DisambiguationError as e:
            linked_entities.append((entity[0], entity[1], "Disambiguation Error"))
        except wikipedia.exceptions.PageError:
            linked_entities.append((entity[0], entity[1], "No page found"))

    return linked_entities
