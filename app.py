import streamlit as st
import pandas as pd
import plotly.express as px


# Emoji cheat sheet: https://www.webfx.com/tools/emoji-cheat-sheet/

# App config, always first
st.set_page_config(
    page_title="Juleøltest 2019-2021", page_icon=":beers:", layout="wide"
)

# Dataselection
@st.cache
def get_data():
    df = pd.read_csv("data1.csv")
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    return df


df = get_data()


def get_data2():
    df = pd.read_csv("data2.csv")
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    return df


df2 = get_data2()


def get_data3():
    df = pd.read_csv("data3.csv")
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    return df


df3 = get_data3()


def get_data4():
    df = pd.read_csv("data4.csv")
    return df


df4 = get_data4()

# Sidebar config

st.sidebar.header("Slik testet vi:")
with st.sidebar.expander("Panel og antall slag"):
    st.write(
        "Panelet har bestått av mellom 3 til 6 dommere,der alle har betydelig erfaring med malt og humle.  \n  "
        "Antall testede slag har vært mellom 14 og 19.  \n"
    )

with st.sidebar.expander("Poenggivning"):
    st.write(
        "Testene var blindtester der kun den som skjenket visste hva slags type som ble testet.  \n"
        "Alle dommerne gav en score mellom 0 og 100. Snittet av dette er endelig score på testet slag."
    )

st.sidebar.header("Graf:")

år = st.sidebar.selectbox(
    "Velg år:",
    options=df4["År"].unique(),
)

df_selection = df4.query("År == @år")

# -----MAIN PAGE-----
st.title(":beers: Juleøltest 2019-2021 :christmas_tree:")
st.subheader("En høyst uoffisiell rangering av juleøl fra 2019-2021")

st.markdown("---")

# Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("2019")
    st.dataframe(df)

with col2:
    st.subheader("2020")
    st.dataframe(df2)

with col3:
    st.subheader("2021")
    st.dataframe(df3)

st.markdown("---")

# BAR CHART
st.subheader("Score per år")

sort_år = df_selection.groupby(by=["Type"]).sum()[["Score"]]
chart_år = px.bar(
    sort_år,
    x=sort_år.index,
    y="Score",
    color_discrete_sequence=["#0083B8"] * len(sort_år),
    template="plotly_white",
)

chart_år.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

st.plotly_chart(chart_år, use_container_width=True)
