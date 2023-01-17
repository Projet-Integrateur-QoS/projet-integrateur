import plotly.express as px

def figure():
    df = px.data.gapminder().query("continent=='Oceania'")
    
    fig = px.line(df, x="year", y="lifeExp", color='country')
    fig.write_html('first_figure.html', auto_open=True)