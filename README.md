# 🌊 Advanced Sankey Diagram in Tableau: User Acquisition Flow


## 📌 Project Overview
This repository showcases a **100% custom-built Sankey Diagram** created entirely in Tableau without the use of any third-party extensions or plugins. 

The visualization maps the user acquisition flow from **Marketing Channels** (e.g., Organic SEO, Meta Ads) to **Device Types** (e.g., iOS, Android, Web). It demonstrates advanced Tableau engineering techniques to create mathematically perfect, smooth S-curves for data storytelling.

<img width="1449" height="936" alt="Screenshot 2026-04-09 at 7 56 23 PM" src="https://github.com/user-attachments/assets/d6a4e30f-f868-4a9b-a775-c5d9f943ea22" />


## 🚀 Technical Highlights & Advanced Techniques

Building a true Sankey Diagram natively in Tableau requires bypassing standard chart limitations. This project successfully implements the following advanced concepts:

* **Data Densification :** Generating 49 virtual data points (Bins) per flow line using index-based calculations, forcing Tableau to draw curves where no raw data exists.
* **Mathematical Modeling :** Utilizing the Sigmoid function (`1 / (1 + EXP(-[T]))`) to calculate the exact X and Y coordinates for the smooth "S" trajectory of the data flow.
* **Complex Nested Table Calculations:** Configuring highly complex, multi-layered window calculations (`Window_Max`, `Index()`) with precise `Compute Using` and `At the Level` directions to control the start and end heights of each channel.
* **Sankey Hook Elimination:** Overcoming Tableau's native drawing limitations by applying axis-fixing techniques and custom sorting to remove the classic "Sankey Hook" artifact, resulting in a flawless connection.
* **Pixel-Perfect Dashboard Design:** Achieving a `0-padding` Tiled layout to seamlessly blend three independent worksheets (Left Bar + Middle Curve + Right Bar) into a single, unified visual experience.

## 🗂️ Repository Contents

* `Marketing_Sankey_Dashboard.twbx`: The packaged Tableau workbook containing the fully functional visualization and calculated fields.
* `marketing_growth_data.csv`: The underlying dataset used for this project.
* `dashboard_preview.png`: High-resolution preview of the final dashboard.

## 🛠️ How to View the Dashboard

1. Clone or download this repository.
2. Ensure you have **Tableau Desktop** or **Tableau Public** installed on your machine.
3. Open the `Marketing_Sankey_Dashboard.twbx` file.
4. Alternatively, you can view the live interactive version on my Tableau Public profile here: [https://public.tableau.com/app/profile/chenge.li3102/vizzes]

## 💡 Use Case
This specific dashboard is designed for Growth and Marketing teams to instantly identify which user acquisition channels are driving traffic to specific platforms, aiding in budget allocation and conversion rate optimization (CRO).

---
*Built with ❤️ and advanced Table Calculations by [Chenge Li]*
