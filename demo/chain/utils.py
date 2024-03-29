from colored import fg
import logging
from IPython.display import display, Markdown


def pprint(clr, message):
    print(f"{clr}{message}")
    return


blue, red, green, yellow = (
    fg("blue"),
    fg("red"),
    fg("green"),
    fg("yellow"),
)


def enable_logging():
    logging.getLogger("llama_index").setLevel(logging.DEBUG)
    logging.getLogger("langchain").setLevel(logging.DEBUG)


def print_result(result, question):
    print(result)
    output_text = f"""### Question: 
    {question}
    ### Answer: 
    {result['answer']}
   
    """
    # ### Sources:
    # {result['source_documents']}
    display(Markdown(output_text))
