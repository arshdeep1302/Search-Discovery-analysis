# 📊 Company Recruitment Funnel Dashboard

## Overview

The Company Recruitment Funnel Dashboard is an interactive analytics solution developed using Python, Pandas, Plotly, and Streamlit. The dashboard helps analyze the company-side recruitment journey, from job posting to successful hiring, by tracking key recruitment metrics and conversion rates.

This project was developed as part of the PlaceMux Data Analyst Search & Discovery task, focusing on building a Company Funnel and generating actionable business insights from recruitment data.

---

## Objectives

* Track the recruitment funnel from Companies to Hires.
* Measure conversion rates at each hiring stage.
* Identify recruitment bottlenecks and drop-off points.
* Visualize hiring trends and company performance.
* Provide business insights to improve recruitment efficiency.

---

## Tech Stack

### Programming Language

* Python

### Libraries Used

* Pandas
* Plotly
* Streamlit

### Data Storage

* CSV Files

### Visualization

* Plotly Interactive Charts

---

## Dataset Structure

The project uses six datasets:

### Companies

Contains company registration information.

### Jobs

Contains job postings created by companies.

### Applications

Contains candidate applications submitted for jobs.

### Shortlists

Contains shortlisted candidates.

### Interviews

Contains interview records.

### Hired

Contains successful hiring records.

---

## Recruitment Funnel

The dashboard tracks the following recruitment stages:

Companies
→ Jobs Posted
→ Applications Received
→ Candidates Shortlisted
→ Interviews Conducted
→ Successful Hires

---

## Dashboard Features

### KPI Cards

Displays:

* Total Companies
* Total Jobs
* Total Applications
* Total Shortlisted Candidates
* Total Interviews
* Total Hires

### Recruitment Funnel

Visualizes candidate movement through the hiring process.

### Conversion Metrics

Measures:

* Shortlist Rate
* Interview Rate
* Hire Rate

### Hiring Trend Analysis

Shows hiring activity over time.

### Top Hiring Companies

Identifies companies with the highest hiring activity.

### Applications by Company

Displays application volume across companies.

### Funnel Drop-Off Analysis

Highlights stages where the highest candidate loss occurs.

### Data Quality Checks

Monitors:

* Missing Values
* Dataset Record Counts
* Data Completeness

### Business Insights

Provides actionable recommendations based on recruitment performance.

---

## Key Business Questions Answered

* How many companies are actively hiring?
* How many jobs are posted?
* What percentage of applicants get shortlisted?
* What percentage of shortlisted candidates reach interviews?
* What percentage of applicants are eventually hired?
* Where are the biggest recruitment drop-offs occurring?
* Which companies hire the most candidates?

---

## Project Structure

```text
company-funnel-dashboard/

├── app.py
├── requirements.txt
├── README.md

├── Data/
│   ├── companies.csv
│   ├── jobs.csv
│   ├── applications.csv
│   ├── shortlists.csv
│   ├── interviews.csv
│   └── hired.csv
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd company-funnel-dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Sample Metrics

* Companies: 50
* Jobs Posted: 100
* Applications: 500
* Shortlisted: 150
* Interviews: 80
* Hires: 30

---

## Business Insights

* Recruitment efficiency can be measured through funnel conversion rates.
* Candidate drop-offs help identify hiring bottlenecks.
* Companies with higher hiring activity can be analyzed for best practices.
* Data-driven recruitment decisions improve overall hiring performance.

---

## Future Enhancements

* Company-level filtering
* Date range filters
* Department-wise hiring analysis
* Predictive hiring analytics
* Real-time database integration
* Automated reporting

---

## Author

**Arshdeep**
