from src.data_cleaning import clean_data

from src.correlation_analysis import correlation_analysis

from src.probability_analysis import probability_analysis

from src.regression_model import regression_model

from src.visualization_dashboard import visualization_dashboard

# =====================================
# DATA CLEANING
# =====================================

df = clean_data()

# =====================================
# CORRELATION ANALYSIS
# =====================================

correlation_analysis(df)

# =====================================
# PROBABILITY ANALYSIS
# =====================================

probability_analysis(df)

# =====================================
# REGRESSION MODEL
# =====================================

model = regression_model(df)

# =====================================
# VISUALIZATION DASHBOARD
# =====================================

visualization_dashboard(df)