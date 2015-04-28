def generate_model_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept
        

NOTES = """TITLE: Lesson 3 - Functions/'Procedures'
DESCRIPTION: A functions takes a value, or values, as its input, processes it and produces an output. 
def  my_fuction(): is an example of a function. It always starts with the word def, followed by any given function name, and then the function parameters in parentheses. These parameters will eventually be replaced by actual values when the function is used or called.
To use a function, we write the name of the function followed by the value(s) we want to give it in parentheses.
For example, a function named square might take a number as input and produce the square of that number as output. def square (n): On next line – return n * n    
Functions help programmers avoid repetition by minimizing the amount of code. Once defined, it does not need to be defined again and can be reused over and over.
A function needs the return keyword to tell Python what the function should produce as output.
TITLE: Lesson 4 Control Loops & Flow: If & While
DESCRIPTION: For loops are traditionally used when you have a piece of code which you want to repeat n number of times. As an alternative, there is the While Loop. A While Loop repeatedly executes the body of the loop until the "test condition" is no longer true.
Lists store data in a structured manner. Each element of a sequence is assigned a number - its position or index. The first index is zero, the second index is one, and so forth. Objects in a list are comma-separated values (items) between square brackets. Lists can have other lists inside them. [‘a’, ‘b’, [‘c’, ‘d’]]. Lists can contain different type of variables, i.e. strings, integers, characters. [‘Python’, 'Python is a Programming Language', ‘2’,].
Mutation '' It means that we can change the value of a list after we have created it, but we cannot in case of strings. Strings can only hold a set of characters.
Append - It's the command used to add elements to a list. list = ['a', 'b', 'c'].  list.append('d').
New values are List = ['a', 'b', 'c', 'd']
+ - concatenates values in a list creating new list.  ['a', 'b',] + ['c','d'] = ['a', 'b', 'c', 'd']
When two identifiers refer to the same variable (and therefore value), this is known as an alias.
Len = length of the elements in a list."""


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_model_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(NOTES)
