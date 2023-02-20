import json
import streamlit as st

language_lists = json.load(open("./resources/languages.json", encoding="utf-8"))
licenses = json.load(open("./resources/licenses.json", encoding="utf-8"))

st.header("OpenGPT-X: Multilingual Data Sourcing")
st.subheader(f"Details about your data source")

input_title = st.text_input(
    label=f"Title of the data source",
)

input_url = st.text_input(
    label=f"URL of the data source",
    help="If the data is not publicly available, please provide a link to the data source.",
)


input_data_type = st.radio(
    label="What type of data do you want to contribute?",
    options=[
        "unsupervised dataset (text data for language model training)",
        "supervised task dataset (for evaluation or instruction fine-tuning)",
        "pretrained model (baselines or transfer learning)",
        "other data types",
    ],
    help="",
)

input_languages = st.multiselect(
    label="What languages does your resource cover? Select as many as apply here:",
    options=[l["name"] for code, l in language_lists.items()] + ["other"],
)

input_license_properties = st.multiselect(
    label="Which of the following best characterize the licensing status of the data? Select all that apply:",
    options=[
        "public domain",
        "multiple licenses",
        "copyright - all rights reserved",
        "open license",
        "research use",
        "non-commercial use",
        "do not distribute",
    ],
    key="validate_license_properties",
)

input_availibility = st.radio(
    label="Can the data be obtained online?",
    options=[
        "Yes - it has a direct download link or links",
        "Yes - after signing a user agreement",
        "No - but the current owners/custodians have contact information for data queries",
        "No - we would need to spontaneously reach out to the current owners/custodians",
    ],
)

input_description = st.text_area(
    label=f"Provide a short description of the resource",
    help="Describe the resource in a few words to a few sentences, the description will help us understand the resource and how it can be used.",
)

st.subheader(f"Details about you (optional)")

input_author_name = st.text_input(
    label=f"Your name",
    help="This information will only be used to contact you.",
)

input_author_email = st.text_input(
    label=f"Your email address",
    help="This information will only be used to contact you.",
)


if st.button("Submit form"):
    st.write(
        "Thank you for contributing a data source! If you have additional data, please fill the form again."
    )
