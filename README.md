# SaaS Sales Pipeline Conversion Analysis

Analysis of 78,025 sales records to identify why TechnoServe's 
conversion rate dropped from 35% to 25%.

## Problem Statement
TechnoServe, a B2B SaaS startup, experienced a significant drop 
in sales pipeline conversion. This project analyses the root causes 
across technology type, sales channel, client revenue, and 
opportunity size.

## Key Findings
- Overall conversion rate: **22.6%** (target was 35%)
- **Enterprise Sellers** had the highest conversion at 27.6%
- **ERP Implementation** leads converted better than other tech segments
- **Online Leads** performed worst at only 6.5% conversion
- Small opportunity sizes (under 10K) showed highest conversion rates

## Project Structure
        saas-pipeline-analysis/
    ├── data/
       └── saas_data.xlsx        # 78,025 sales records
    ├── output/
       ├── tech.png              # Conversion by technology
       └── channel.png           # Conversion by sales channel
    ├── main.py                   # Entry point
    ├── saas_analysis.py          # Core analysis logic
    └── README.md

## How to Run
```bash
pip install pandas matplotlib openpyxl
python main.py
```

## Tools Used
| Tool | Purpose |
|------|---------|
| Python | Core scripting |
| Pandas | Data processing |
| Matplotlib | Visualisation |

## Frameworks Used
- BANT Framework (Budget, Authority, Need, Timeline)
- 4P Marketing Mix Analysis

## Author
T V L N Samhigna — M.Sc Business Analytics