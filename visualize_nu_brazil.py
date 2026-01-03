import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_nu_brazil():
    df = pd.read_csv("data/nu_brazil_merged.csv", index_col=0, parse_dates=True)

    # Create subplots
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05)

    # $NU Price vs. BRL/USD
    fig.add_trace(
        go.Scatter(x=df.index, y=df["Close"], name="$NU Price", line=dict(color="blue")),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=df.index, y=df["brl_usd"], name="BRL/USD", line=dict(color="red"), yaxis="y2"),
        row=1, col=1
    )
    fig.update_yaxes(title_text="$NU Price (USD)", row=1, col=1)
    fig.update_yaxes(title_text="BRL/USD", secondary_y=True, row=1, col=1)

    # Selic Rate vs. $NU Returns
    fig.add_trace(
        go.Scatter(x=df.index, y=df["selic"], name="Selic Rate", line=dict(color="green")),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=df.index, y=df["NU_Return"], name="$NU Returns", line=dict(color="orange"), yaxis="y2"),
        row=2, col=1
    )
    fig.update_yaxes(title_text="Selic Rate (%)", row=2, col=1)
    fig.update_yaxes(title_text="$NU Daily Returns", secondary_y=True, row=2, col=1)

    # IPCA Inflation vs. $NU MA50
    fig.add_trace(
        go.Scatter(x=df.index, y=df["ipca"], name="IPCA Inflation", line=dict(color="purple")),
        row=3, col=1
    )
    fig.add_trace(
        go.Scatter(x=df.index, y=df["NU_MA_50"], name="$NU MA50", line=dict(color="cyan"), yaxis="y2"),
        row=3, col=1
    )
    fig.update_yaxes(title_text="IPCA Inflation (%)", row=3, col=1)
    fig.update_yaxes(title_text="$NU MA50 (USD)", secondary_y=True, row=3, col=1)

    # Update layout
    fig.update_layout(
        title_text="$NU vs. Brazil Macro (2021–2026)",
        height=900,
        showlegend=True
    )
    fig.write_html("visualizations/nu_brazil_dashboard.html")
    print("Dashboard saved to visualizations/nu_brazil_dashboard.html")

if __name__ == "__main__":
    plot_nu_brazil()
