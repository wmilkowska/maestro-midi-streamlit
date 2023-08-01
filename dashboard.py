import streamlit as st
from fortepyan import MidiPiece
from datasets import load_dataset

import utils as U


dataset = load_dataset("roszcz/maestro-v1-sustain", split="train")

st.set_page_config(layout="wide")

cols = st.columns(2)


n_records = 20
for it in range(n_records):
    record = dataset[it]
    col = it % 2

    piece = MidiPiece.from_huggingface(record)
    paths = U.piece_av_files(piece)
    with cols[col]:
        st.image(paths["pianoroll_path"])
        st.audio(paths["mp3_path"])
        st.table(piece.source)
