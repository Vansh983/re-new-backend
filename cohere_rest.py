# Setting up cohere
import cohere

co = cohere.Client('bPnEkiW2KeYyupinU83dcN1wKVp4w1Lo1zXx28dC')

# generating the tasks given a category
def generateTasks(category):
    # Asserting the correct values
    if category != 'skill' and category != 'fitness' and category != 'academic' and category != 'wellness':
        return
    if category == 'skill':
        category = 'skill learning' # this is better for the prompt
    
    prompt = f"Give four unique {category} goals for me to do today, in a list."

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

    # task_list is an array of strings
    return task_list