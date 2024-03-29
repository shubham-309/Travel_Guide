import streamlit as st
from ui_helper import create_sources_string
from streamlit_chat import message
from chain.session import Session
from chain.constants import MemoryType, ChainType
import time
from dotenv import load_dotenv

load_dotenv()
 
session = Session()

if "chain_session" not in st.session_state:
    st.session_state.chain_session = session

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

with st.sidebar:
    st.subheader("Advanced Settings")

    def get_new_values_list():
        st.write(st.session_state["cb_sources"])

    st.checkbox(
        "Show Sources",
        value=st.session_state.chain_session.show_sources,
        key="cb_sources",
        help="Enable the checkbox to display the answer source.",
        on_change=lambda: st.session_state.chain_session.update_sources(
            st.session_state["cb_sources"]
        ),
    )
    st.divider()
    st.selectbox(
        "Chain",
        (
            ChainType.Stuff.name,
        ),
        key="sb_chain",
        index=st.session_state.chain_session.chain_type.value,
        on_change=lambda: st.session_state.chain_session.update_chain(
            st.session_state["sb_chain"]
        ),
    )
    st.divider()
    st.slider(
        "Temperature",
        key="sl_temperature",
        min_value=0.0,
        max_value=2.0,
        value=st.session_state.chain_session.temperature,
        help="It controls the randomness of the responses.",
        step=0.1,
        on_change=lambda: st.session_state.chain_session.update_temperature(
            st.session_state["sl_temperature"]
        ),
    )
    st.divider()
    st.selectbox(
        "Memory",
        (MemoryType.no_memory.name, MemoryType.chat_history.name),
        index=st.session_state.chain_session.memory_type.value,
        key="sb_memory",
        label_visibility="visible",
        on_change=lambda: st.session_state.chain_session.update_memory(
            st.session_state["sb_memory"]
        ),
    )
    st.divider()
    st.write("version 1.1.2")


st.header("Legal Query Bot")
with st.form(key="QA", clear_on_submit=True):
    prompt = st.text_input(
        "Question",
        placeholder="Enter your question here..",
        key="et_question",
    )
    generate_answer = st.form_submit_button("Generate Answer")


if generate_answer:
    with st.spinner(f"Generating response for: {prompt}"):
        start_time = time.time()
        generated_response, cb = st.session_state.chain_session.get_answer(prompt)
        print("<<<<<<<<<<<<<<<")
        print(generated_response)
        try:
            sources = set(
                [
                    doc.metadata["source"]
                    for doc in generated_response["source_documents"]
                ]
            )

            formatted_response = (
                f"{generated_response['answer']} \n\n {create_sources_string(sources)}"
            )
        except:
            formatted_response = f"{generated_response['answer']}"

        st.session_state["user_prompt_history"].insert(0, prompt)
        st.session_state["chat_answers_history"].insert(
            0,
            formatted_response
            + "\n\n Tech Details: "
            + st.session_state.chain_session.get_details()
            + "\n\n"
            + str(cb)
            + "\n \n"
            + "Total Time Taken: "
            + str(time.time() - start_time)
            + "seconds",
        )


if st.session_state["chat_answers_history"]:
    for index, (generated_response, user_query) in enumerate(
        zip(
            st.session_state["chat_answers_history"],
            st.session_state["user_prompt_history"],
        )
    ):
        message(user_query, is_user=True, key=index)
        message(generated_response)
