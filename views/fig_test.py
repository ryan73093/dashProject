import plotly.express as px
from db_wrapper.db_test import dfA, dfB, dfC

figB = px.bar(dfB, x="Fruit", y="Amount", color="City", barmode="group")

figC = px.line(dfC, x='Date', y='Price', color='Code')
