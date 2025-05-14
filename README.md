# Segment-Level Forecasting Model (NVIDIA, FY2014–FY2027)

**Subtitle:** Time-Series Forecasting with Prophet for 5 Business Segments  
**Author:** Ekkarit, Corporate Futurist & FP&A Strategist  
**Date:** May 13, 2025  

---

## 2. Executive Overview

This project develops a robust segment-level revenue forecasting model for NVIDIA Corporation using Prophet, a time-series algorithm developed by Meta. Covering data from Q1 FY2014 to Q4 FY2024, the goal was to model and forecast quarterly revenues for five strategic business segments: Gaming, Data Center, Professional Visualization (Pro Viz), Automotive, and OEM & Other.

By tuning Prophet with custom seasonality and changepoint configurations, we delivered 12-quarter forecasts through FY2027. This project enhances NVIDIA's financial planning and performance monitoring processes by providing segment-specific visibility for FP&A teams.

**Key outcomes:**
- High forecast accuracy in Gaming, Pro Viz, and Automotive (MAPE < 15%)
- Moderate predictability in OEM & Other (MAPE ~15.5%)
- Low forecast reliability in Data Center due to volatile AI-driven growth (MAPE > 50%)

---

## 3. Executive Summary

- **Problem:** NVIDIA requires high-resolution, forward-looking forecasts at the segment level to align investment, R&D, and operational decisions.
- **Methodology:** Time-series modeling with Prophet, tuned for quarterly financial data with additive/multiplicative seasonality and changepoint sensitivity.
- **Data Source:** NVIDIA Quarterly Segment Revenue Data (FY2014–FY2024)
- **Key Results:**
  - Gaming MAPE: 13.99%
  - Data Center MAPE: 51.25%
  - Pro Viz MAPE: 13.54%
  - Automotive MAPE: 7.88%
  - OEM & Other MAPE: 15.54%
- **Implications:** Gaming and Automotive can be reliably forecasted and integrated into strategic plans. Data Center requires ongoing model adjustment and close monitoring.
- **Recommendation:** Embed this forecasting pipeline into NVIDIA’s quarterly FP&A cycle for proactive planning.

---

## 4. Introduction

NVIDIA’s revenue mix is rapidly evolving due to macroeconomic factors, AI acceleration, and market diversification. Traditional top-line forecasting masks the idiosyncrasies of high-growth segments. This project introduces a segment-level forecasting engine that allows financial analysts to model, visualize, and interpret future segment trajectories individually.

---

## 5. Background and Context

- **Gaming** revenue fluctuates with product cycles and GPU demand.  
- **Data Center** growth has exploded with AI/ML investments.  
- **Pro Viz** and **Automotive** remain niche but stable.  
- **OEM & Other** includes legacy and licensing revenue.  

Segment-level forecasting is essential for:
- Product allocation & capacity planning
- Sales quota setting
- Long-range strategic roadmaps

---

## 6. Data Collection and Preparation

**Source:** NVIDIA Investor Relations (FY2014–FY2024)  
**Steps:**
- Cleaned CSV, removed year headers
- Parsed quarters to datetime
- Indexed by fiscal quarter start
- Segmented each column for modeling

**Limitations:**
- Q4 FY2024 data may be provisional
- Data Center volatility may bias Prophet’s trend fit

---

## 7. Methodology

**Tool:** Prophet (Meta)  
**Settings:**
- Multiplicative seasonality
- Quarterly seasonality (period=3, fourier_order=5)
- Changepoint scale = 0.3
- Forecast horizon = 12 quarters

Each segment was forecasted independently.

---

## 8. Analysis and Results

| Segment        | MAE ($M) | MAPE (%) | Accuracy Level |
|----------------|----------|-----------|-----------------|
| Gaming         | 215      | 13.99     | High            |
| Data Center    | 479      | 51.25     | Low             |
| Pro Viz        | 38       | 13.54     | High            |
| Automotive     | 12       | 7.88      | Very High       |
| OEM & Other    | 21       | 15.54     | Medium          |

---

## 9. Discussion

- **Strength:** Prophet captured seasonality well in Gaming, Auto, and Pro Viz.
- **Weakness:** Data Center’s hypergrowth caused over/underfit.
- **Future:** Consider adding macroeconomic regressors or hybrid models (e.g., XGBoost).

---

## 10. Recommendations

- Adopt this model for quarterly FP&A planning
- Re-forecast high-volatility segments every 3 months
- Use model outputs for scenario stress testing
- Present segment forecasts in earnings materials

---

## 11. Conclusion

This project delivers a reliable segment-level revenue forecast engine using tuned Prophet models. It improves NVIDIA’s capacity for planning, monitoring, and strategy across dynamic product lines and markets.

---

## 12. References

- [NVIDIA Investor Relations](https://investor.nvidia.com/)
- [Prophet documentation](https://facebook.github.io/prophet/)
- Plotly, Pandas, scikit-learn

---

## 13. Appendix

- 📁 Forecast CSVs: `/data/`
- 📈 Segment charts: `/charts/`
- 📋 Each forecast includes: `ds`, `yhat`, `yhat_lower`, `yhat_upper`
