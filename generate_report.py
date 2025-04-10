import os
from datetime import datetime
import streamlit as st

def generate_html_report(dcf_analyzer, returns_array):
    """
    Generate an HTML report summarizing key DCF metrics and Monte Carlo stats
    """
    output_path = "attached_assets/EasyJet_DCF_Report.html"

    if not os.path.exists("attached_assets"):
        os.makedirs("attached_assets")

    metrics = dcf_analyzer.variables

    mean_return = f"{returns_array.mean()*100:.2f}%" if returns_array is not None else "N/A"
    volatility = f"{returns_array.std()*100:.2f}%" if returns_array is not None else "N/A"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='UTF-8'>
        <title>EasyJet DCF Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; line-height: 1.6; }}
            h1 {{ color: #E67E22; }}
            h2 {{ color: #2980B9; }}
            .section {{ margin-bottom: 30px; }}
            .metric {{ margin-bottom: 10px; }}
        </style>
    </head>
    <body>
        <h1>EasyJet DCF Valuation Report</h1>
        <p><b>Date:</b> {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>

        <div class='section'>
            <h2>DCF Key Inputs</h2>
            <div class='metric'><b>Valuation Date:</b> {metrics['valuation_date']}</div>
            <div class='metric'><b>WACC:</b> {metrics['wacc']*100:.2f}%</div>
            <div class='metric'><b>Terminal Growth:</b> {metrics['terminal_growth']*100:.2f}%</div>
            <div class='metric'><b>Current Share Price:</b> £{metrics['current_share_price']:.2f}</div>
            <div class='metric'><b>Diluted Shares Outstanding:</b> {metrics['diluted_shares_outstanding']:.0f}</div>
        </div>

        <div class='section'>
            <h2>Valuation Results</h2>
            <div class='metric'><b>Implied EV (Multiples):</b> £{metrics['ev_multiples']:.2f}</div>
            <div class='metric'><b>Implied EV (Perpetuity):</b> £{metrics['ev_perpetuity']:.2f}</div>
            <div class='metric'><b>Implied Share Price (Multiples):</b> £{metrics['share_price_multiples']:.2f}</div>
            <div class='metric'><b>Implied Share Price (Perpetuity):</b> £{metrics['share_price_perpetuity']:.2f}</div>
        </div>

        <div class='section'>
            <h2>Monte Carlo Summary</h2>
            <div class='metric'><b>Mean Daily Return:</b> {mean_return}</div>
            <div class='metric'><b>Volatility:</b> {volatility}</div>
        </div>

        <p><i>This report is automatically generated from the Streamlit DCF dashboard for EasyJet plc.</i></p>
    </body>
    </html>
    """

    with open(output_path, "w") as f:
        f.write(html_content)

    return output_path
