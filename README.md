# **Data Business Eleven**

## **Project Overview**
This project involves analyzing client and event data to identify valuable insights for improving business outcomes. It leverages machine learning techniques like clustering and causal inference to analyze transactional, client, and action-related datasets.

## **Directory Structure**
The project is organized as follows:

```
.
├── Data/
│   ├── actions.xlsx               # Contains data on marketing actions and events
│   ├── clients.xlsx               # Client data including contactability and demographics
│   ├── transactions.xlsx          # Transactional data with sales and quantities
├── Causal_inference.ipynb         # Notebook for performing causal inference
├── cluster_clients_actions.ipynb  # Notebook for clustering clients based on their transactions and event participation
├── Hackathon X-HEC 2024_vSENT.pdf # Hackathon challenge document
├── selected_clients.json          # JSON file storing the selected client IDs for invitations
├── streamlit_app.py               # Streamlit app to visualize selected clients by event
└── README.md                      # Documentation for the project
```

## **How to Run the Project**
### **1. Set up the environment**
- Ensure you have Python 3.8+ installed.
- Install the required Python libraries:
  ```bash
  pip install -r requirements.txt
  ```

### **2. Data Preparation**
- Place the datasets (`actions.xlsx`, `clients.xlsx`, `transactions.xlsx`) into the `Data/` directory.

### **3. Jupyter Notebooks**
- Open and run the following notebooks:
  - `Causal_inference.ipynb`: To analyze the causal impact of events on sales and client behavior.
  - `cluster_clients_actions.ipynb`: To perform clustering and analyze client engagement.

### **4. Streamlit Application**
- Launch the Streamlit app to visualize the selected clients:
  ```bash
  streamlit run streamlit_app.py
  ```
- The app allows you to:
  - Select an event type.
  - View client IDs to invite for the event.

## **Key Outputs**
- **Clusters of Clients**: Segmented client groups based on event participation and spending patterns.
- **Causal Inference**: Insights into the effectiveness of marketing actions.
- **Streamlit App**: Interactive tool to explore selected clients for each event.

## **Contact**
For any questions or contributions, feel free to reach out!
