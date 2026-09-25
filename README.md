# Enterprise Supply Chain Analytics & Predictive Suite 🚚📊

## 📌 Project Overview
This project delivers a production-ready **Supply Chain Control Tower** designed to solve a classic enterprise challenge: fragmented logistics data silos and delayed inventory risk visibility. 

Emulating architecture standards frequently implemented by global consultancies like **Accenture**, this end-to-end business intelligence engine transforms messy transactional records into interactive, real-time executive insights. It ensures **360° operational value** by tracking revenue trends alongside critical stock-out thresholds.

---

## 🏗️ Technical Architecture & Pipeline
The suite is built upon an enterprise data lifecycle model, moving seamlessly from raw ingestion to diagnostic machine learning:

1. **Data Lakehouse Strategy (Bronze to Gold):** Simulated ingestion pipelines process raw transactional records (`CSV`/`JSON`), cleaning duplicates, handling schema validation, and masking PII compliance data via SQL/Python logic.
2. **Semantic Modeling & Aggregation (Gold Layer):** Modeled high-performance relational tables optimized for fast query execution and analytical reporting.
3. **Analytical BI Layer (Power BI):** Formulated deep business logic using advanced DAX calculations to isolate moving operational metrics.
4. **Augmented AI Layer:** Utilized embedded Machine Learning (Linear and Logistic Regression models) to dynamically diagnose operational bottlenecks.

---

## ⚡ Core Business Metrics Engineered (DAX)
*   **Units Sold Today:** Running total metric aggregating instant daily sales throughput.
*   **Inventory Risk %:** Dynamic operational health metric tracking items falling below calculated safety stock parameters.
*   **Dynamic Alert Engine:** Categorical logic dividing SKUs into `HEALTHY`, `HIGH RISK`, and `CRITICAL: OUT OF STOCK` tiers.

---

## 🤖 Machine Learning Diagnostic Insights
Rather than just displaying historical performance, the suite features a native **AI Key Influencers** layer. This model runs automated root-cause classifications on the data model, informing supply chain managers exactly *why* stock failures occur.
*   **Key Discovery:** The model isolated that when `total_units_sold_today` crosses a threshold of **33 units**, the mathematical probability of a product entering a **CRITICAL: OUT OF STOCK** state increases by **3.28x**.

---

## 💻 Tech Stack
*   **BI & Data Visualization:** Microsoft Power BI Desktop
*   **Data Transformation:** SQL (Common Table Expressions, Window Functions, Aggregate Joins), Python (Pandas DataFrames)
*   **Analytics Engine:** DAX (Data Analysis Expressions)
*   **AI Framework:** Power BI Embedded Key Influencers Regression Model

---

## 📷 Dashboard Preview
<img width="464" height="252" alt="image" src="https://github.com/user-attachments/assets/66df6b10-ec06-4cad-88bb-f13d5e5a9ccc" />



---

## 🚀 How to Explore This Project
1. Clone this repository to your machine.
2. Open the `/bi-dashboard/Enterprise_Supply_Chain_Control_Tower.pbix` file using Microsoft Power BI Desktop.
3. Interact with the top-level **Region** and **Category** tile slicers to explore real-time cross-filtering behavior across different global logistics hubs.
