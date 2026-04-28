
---

##Data Pipeline Design

A layered data architecture was implemented to reflect real-world data engineering workflows:

- **raw/** → source transactional data  
- **validated/** → cleaned and quality-checked data  
- **processed/** → feature-engineered data for ML  
- **outputs/** → model predictions and risk scores  
- **sql_reports/** → analytics outputs and business insights  

---

##Fraud Detection Model

A Logistic Regression model was developed to identify fraudulent transactions using engineered features such as:

- transaction behavior patterns  
- customer spending behavior  
- merchant fraud indicators  

The system produces:
- transaction-level fraud predictions  
- customer-level risk scores  

---

## SQL Analytics

The system includes structured SQL analytics to extract business insights:

- fraud rate by country  
- fraud rate by transaction channel  
- high-risk customers  
- high-risk merchants  

These queries simulate real-world reporting and risk monitoring use cases.

---

## Azure Integration

- **Azure Blob Storage** used for structured, layered data storage  
- **Azure Data Factory** used to orchestrate data movement across pipeline stages  

This setup reflects a scalable cloud-based data engineering architecture.

---

## Outputs

- Fraud predictions (`predictions.csv`)  
- Customer risk scores (`risk_scores.csv`)  
- SQL-based analytics reports  
- Visual charts for decision-making insights  

---

## Pipeline Automation

The entire workflow is automated using a batch script:
