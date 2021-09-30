import streamlit as st
import pandas as pd
import streamlit as st
from datetime import datetime

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

st.title('Index Coop Community Dashboard')

st.header("Discord Role Data")

df_role_audit = pd.read_csv("role_audit.csv")

st.write("Last Updated Sept 29, 2021")

#total membership
df_total_membership = pd.read_csv("./discord_insights_raw_data/guild-total-membership-20210929.csv")
st.write("Current Member Count")
current_total_membership = list(df_total_membership["total_membership"].tail(1))[0]
st.write(current_total_membership)

#metal owl coults
st.write("Gold Owl Count")
st.write(df_role_audit["Gold Owls"].count())

st.write("Silver Owl Count")
st.write(df_role_audit["Silver Owls"].count())

st.write("Bronze Owl Count")
st.write(df_role_audit["Bronze Owls"].count())


csv_role_audit = convert_df(df_role_audit)

st.download_button(label="Download data as CSV",data=csv_role_audit,file_name='IC_role_audit.csv',mime='text/csv')


st.header("Discord Insights Data")

df_joins_by_source = pd.read_csv("./discord_insights_raw_data/guild-joins-by-source-20210929.csv")

df_joins_by_source["New Members"] = df_joins_by_source["discovery_joins"] + df_joins_by_source["vanity_joins"] + df_joins_by_source["invites"]
df_joins_by_source = df_joins_by_source.drop(columns=["discovery_joins","vanity_joins","invites"])

def returnDateTime(x):
    return(datetime.fromisoformat(x).strftime('%Y-%m-%d'))
    
df_joins_by_source['interval_start_timestamp'] = df_joins_by_source['interval_start_timestamp'].apply(returnDateTime)


df_joins_by_source = df_joins_by_source.set_index('interval_start_timestamp')

st.write("New Joiners per day over the last 2 weeks")
st.line_chart(df_joins_by_source.tail(14))

csv_joins = convert_df(df_joins_by_source)

st.download_button(label="Download data as CSV",data=csv_joins,file_name='IC_new_joins.csv',mime='text/csv')

