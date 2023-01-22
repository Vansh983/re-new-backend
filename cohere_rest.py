# COHERE API
import cohere

co = cohere.Client('bPnEkiW2KeYyupinU83dcN1wKVp4w1Lo1zXx28dC')

# Generates 4 tasks for a choice of category
def generateTasks(category):
    if category != 'skill' and category != 'fitness' and category != 'academic' and category != 'wellness':
        return
    # Set skill to skill learning is more language-like for the prompt
    if category == 'skill':
        category = 'skill learning'
    
    prompt = f"Give four unique {category} goals for me to do today, in a list."

    # Temperature is randomness - we want the tasks to be less predictable but on-track
    model = "command-medium-nightly" 
    max_tokens = 50
    temperature = 1.3

    response = co.generate(
        model = model, 
        prompt = prompt, 
        max_tokens = max_tokens,
        temperature = temperature,)

    tasks = response.generations[0].text
    task_list = [task.strip()[2:] for task in tasks.split("\n")]

    return task_list