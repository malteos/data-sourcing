import json
import streamlit as st

# from PIL import Image
from email.mime.text import MIMEText
import smtplib
import os

title = "OpenGPT-X: Multilingual Data Sourcing"

EMAIL_SUBJECT = title
EMAIL_TO = os.environ.get("EMAIL_TO")
EMAIL_TO_LIST = EMAIL_TO.split(",") if EMAIL_TO else []
EMAIL_FROM = os.environ.get("EMAIL_FROM")
SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = os.environ.get("SMTP_PORT")
SMTP_LOGIN = os.environ.get("SMTP_LOGIN")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
OUTPUT_PATH = os.environ.get("OUTPUT_PATH")

language_lists = json.load(open("./resources/languages.json", encoding="utf-8"))
licenses = json.load(open("./resources/licenses.json", encoding="utf-8"))

st.set_page_config(
    page_title=title,
)

st.header(title)

# st.subheader(f"Details about your data source")

# with st.form("sourcing_form"):
input_title = st.text_input(
    key="title",
    label=f"Title of the data source (required)",
)
input_data_type = st.radio(
    key="data_type",
    label="What type of data do you want to contribute? (required)",
    options=[
        "unsupervised dataset (text data for language model training)",
        "supervised task dataset (for evaluation or instruction fine-tuning)",
        "pretrained model (baselines or transfer learning)",
        "other data types",
    ],
    help="",
)
input_availibility = st.radio(
    key="availibility",
    label="Can the data be obtained online? (required)",
    options=[
        "Yes - it has a direct download link or links",
        "Yes - after signing a user agreement",
        "No - but the current owners/custodians have contact information for data queries",
        "No - we would need to spontaneously reach out to the current owners/custodians",
    ],
)
input_url = st.text_input(
    key="url",
    label=f"URL of the data source (homepage or download link)",
    help="If the data is not publicly available, please provide a link to the data source.",
)

input_languages = st.multiselect(
    key="languages",
    label="What languages does your resource cover? Select as many as apply here:",
    options=[l["name"] for _, l in language_lists.items()] + ["other"],
)
input_license = st.multiselect(
    key="license",
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
)
input_description = st.text_area(
    key="description",
    label=f"Provide a short description of the resource",
    help="Describe the resource in a few words to a few sentences, the description will help us understand the resource and how it can be used.",
)

st.markdown("**Details about you (optional)**")

input_ontributor_name = st.text_input(
    key="contributor_name",
    label=f"Your name",
    help="This information will only be used to contact you.",
)

input_contributor_email = st.text_input(
    key="contributor_email",
    label=f"Your email address",
    help="This information will only be used to contact you.",
)

submitted = st.button("Submit form")

if submitted:
    if (
        st.session_state["title"]
        and st.session_state["data_type"]
        and st.session_state["availibility"]
    ):
        form_data = json.dumps(dict(st.session_state))
        # st.info(form_data)

        # Write to file
        if OUTPUT_PATH:
            with open(OUTPUT_PATH, "a") as f:
                f.write(form_data + "\n")

        # Send mail
        if EMAIL_FROM and EMAIL_TO and SMTP_HOST and SMTP_PORT:
            msg = MIMEText(f"Data sourcing:\n\n{form_data}")

            # me == the sender's email address
            # you == the recipient's email address
            msg["Subject"] = EMAIL_SUBJECT
            msg["To"] = ", ".join(EMAIL_TO_LIST)
            msg["From"] = EMAIL_FROM

            # Send the message via our own SMTP server, but don't include the
            # envelope header.
            s = smtplib.SMTP(SMTP_HOST, port=SMTP_PORT)
            s.login(SMTP_LOGIN, SMTP_PASSWORD)
            s.sendmail(
                msg=msg.as_string(), from_addr=EMAIL_FROM, to_addrs=EMAIL_TO_LIST
            )
            s.quit()
        else:
            st.info(
                "Email not sent. Please set the environment variables EMAIL_FROM, EMAIL_TO, SMTP_HOST, SMTP_PORT."
            )

        # Show success message
        st.success(
            "Thanks for your contribution! Do you have more data? Please fill the form again.",
        )
    else:
        st.error("Please fill in the required fields.")
