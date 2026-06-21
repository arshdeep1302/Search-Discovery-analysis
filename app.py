import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Company Recruitment Funnel Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Company Recruitment Funnel Dashboard")
st.markdown("Analyze company hiring performance and recruitment funnel metrics.")

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():
    companies = pd.read_csv("Data/companies.csv")
    jobs = pd.read_csv("Data/jobs.csv")
    applications = pd.read_csv("Data/applications.csv")
    shortlists = pd.read_csv("Data/shortlists.csv")
    interviews = pd.read_csv("Data/interviews.csv")
    hired = pd.read_csv("Data/hired.csv")

    return (
        companies,
        jobs,
        applications,
        shortlists,
        interviews,
        hired
    )

try:
    (
        companies,
        jobs,
        applications,
        shortlists,
        interviews,
        hired
    ) = load_data()

except Exception as e:
    st.error(f"Error Loading Files: {e}")
    st.stop()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.header("Dashboard Overview")

st.sidebar.success(f"Companies: {len(companies)}")
st.sidebar.success(f"Jobs: {len(jobs)}")
st.sidebar.success(f"Applications: {len(applications)}")
st.sidebar.success(f"Shortlists: {len(shortlists)}")
st.sidebar.success(f"Interviews: {len(interviews)}")
st.sidebar.success(f"Hires: {len(hired)}")

# =====================================================
# KPI METRICS
# =====================================================

total_companies = len(companies)
total_jobs = len(jobs)
total_applications = len(applications)
total_shortlists = len(shortlists)
total_interviews = len(interviews)
total_hires = len(hired)

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

st.info(f"""
### Executive Summary

• {total_companies} Companies Registered

• {total_jobs} Jobs Posted

• {total_applications} Applications Received

• {total_shortlists} Candidates Shortlisted

• {total_interviews} Interviews Conducted

• {total_hires} Successful Hires
""")

# =====================================================
# KPI CARDS
# =====================================================

st.subheader("📌 Key Metrics")

row1_col1, row1_col2, row1_col3 = st.columns(3)

row1_col1.metric("Companies", total_companies)
row1_col2.metric("Jobs Posted", total_jobs)
row1_col3.metric("Applications", total_applications)

row2_col1, row2_col2, row2_col3 = st.columns(3)

row2_col1.metric("Shortlisted", total_shortlists)
row2_col2.metric("Interviews", total_interviews)
row2_col3.metric("Hires", total_hires)

st.divider()

# =====================================================
# CONVERSION METRICS
# =====================================================

st.subheader("📈 Conversion Metrics")

shortlist_rate = (
    total_shortlists / total_applications * 100
    if total_applications else 0
)

interview_rate = (
    total_interviews / total_shortlists * 100
    if total_shortlists else 0
)

hire_rate = (
    total_hires / total_applications * 100
    if total_applications else 0
)

c1, c2, c3 = st.columns(3)

c1.metric("Shortlist Rate", f"{shortlist_rate:.2f}%")
c2.metric("Interview Rate", f"{interview_rate:.2f}%")
c3.metric("Hire Rate", f"{hire_rate:.2f}%")

st.divider()

# =====================================================
# FUNNEL CHART
# =====================================================

st.subheader("🎯 Company Recruitment Funnel")

funnel_fig = go.Figure(
    go.Funnel(
        y=[
            "Companies",
            "Jobs",
            "Applications",
            "Shortlisted",
            "Interviews",
            "Hires"
        ],
        x=[
            total_companies,
            total_jobs,
            total_applications,
            total_shortlists,
            total_interviews,
            total_hires
        ],
        textinfo="value+percent initial"
    )
)

funnel_fig.update_layout(height=600)

st.plotly_chart(
    funnel_fig,
    use_container_width=True
)

st.divider()

# =====================================================
# TOP HIRING COMPANIES
# =====================================================

st.subheader("🏆 Top Hiring Companies")

try:

    hire_company = (
        jobs
        .merge(companies, on="company_id")
        .merge(applications, on="job_id")
        .merge(hired, on="application_id")
    )

    top_hiring = (
        hire_company
        .groupby("company_name")
        .size()
        .reset_index(name="Hires")
        .sort_values(
            "Hires",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        top_hiring,
        x="company_name",
        y="Hires",
        title="Top Hiring Companies"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

except:
    st.warning("Unable to build Top Hiring Companies chart.")

st.divider()

# =====================================================
# APPLICATIONS BY COMPANY
# =====================================================

st.subheader("📨 Applications by Company")

try:

    app_company = (
        jobs
        .merge(companies, on="company_id")
        .merge(applications, on="job_id")
    )

    app_chart = (
        app_company
        .groupby("company_name")
        .size()
        .reset_index(name="Applications")
        .sort_values(
            "Applications",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        app_chart,
        x="company_name",
        y="Applications",
        title="Applications Received by Company"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

except:
    st.warning("Unable to build Applications chart.")

st.divider()

# =====================================================
# HIRING TREND
# =====================================================

st.subheader("📅 Hiring Trend")

if "hire_date" in hired.columns:

    hired["hire_date"] = pd.to_datetime(
        hired["hire_date"],
        errors="coerce"
    )

    trend = (
        hired
        .dropna(subset=["hire_date"])
        .groupby(
            hired["hire_date"].dt.strftime("%Y-%m")
        )
        .size()
        .reset_index(name="Hires")
    )

    if not trend.empty:

        fig = px.line(
            trend,
            x="hire_date",
            y="Hires",
            markers=True,
            title="Monthly Hiring Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.divider()

# =====================================================
# DROP OFF ANALYSIS
# =====================================================

st.subheader("📉 Funnel Drop-Off Analysis")

drop_df = pd.DataFrame({
    "Stage": [
        "Companies",
        "Jobs",
        "Applications",
        "Shortlisted",
        "Interviews",
        "Hires"
    ],
    "Count": [
        total_companies,
        total_jobs,
        total_applications,
        total_shortlists,
        total_interviews,
        total_hires
    ]
})

drop_df["Previous Stage"] = drop_df["Count"].shift(1)

drop_df["Drop %"] = (
    (
        drop_df["Previous Stage"]
        - drop_df["Count"]
    )
    / drop_df["Previous Stage"]
    * 100
).round(2)

st.dataframe(
    drop_df,
    use_container_width=True
)

st.divider()

# =====================================================
# DATA QUALITY
# =====================================================

st.subheader("✅ Data Quality Check")

quality = pd.DataFrame({
    "Dataset": [
        "Companies",
        "Jobs",
        "Applications",
        "Shortlists",
        "Interviews",
        "Hires"
    ],
    "Rows": [
        len(companies),
        len(jobs),
        len(applications),
        len(shortlists),
        len(interviews),
        len(hired)
    ],
    "Missing Values": [
        companies.isnull().sum().sum(),
        jobs.isnull().sum().sum(),
        applications.isnull().sum().sum(),
        shortlists.isnull().sum().sum(),
        interviews.isnull().sum().sum(),
        hired.isnull().sum().sum()
    ]
})

st.dataframe(
    quality,
    use_container_width=True
)

st.divider()

# =====================================================
# BUSINESS INSIGHTS
# =====================================================

st.subheader("💡 Business Insights")

st.success(f"""
Key Findings

• Total Companies: {total_companies}

• Total Applications: {total_applications}

• Shortlist Rate: {shortlist_rate:.2f}%

• Interview Rate: {interview_rate:.2f}%

• Hire Rate: {hire_rate:.2f}%

Recommendation:
Improve candidate screening and job-candidate matching to increase hiring efficiency.
""")

# =====================================================
# RAW DATA
# =====================================================

with st.expander("📂 View Raw Data"):

    st.write("Companies")
    st.dataframe(companies)

    st.write("Jobs")
    st.dataframe(jobs)

    st.write("Applications")
    st.dataframe(applications)

    st.write("Shortlists")
    st.dataframe(shortlists)

    st.write("Interviews")
    st.dataframe(interviews)

    st.write("Hired")
    st.dataframe(hired)