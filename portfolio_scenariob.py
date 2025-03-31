import numpy as np
import matplotlib.pyplot as plt

# Constants
initial_investment_per_stock = 200000  # Initial allocation per stock
additional_investment_per_year = 200000  # Additional investment per year
years = 5  # Forecast period in years

# Expected Annualized Returns (in decimal form)
annualized_returns = {
    "MSFT": 0.3091,
    "DIS": 0.1283,
    "PG": 0.1532,
    "VZ": 0.3135,
    "UNH": 0.2899
}


# Function to calculate future values over time with additional annual investment
def project_future_values(annualized_return, initial_investment, additional_investment, years):
    time_points = np.arange(0, years + 1)  # Time from 0 to years
    future_values = np.zeros(years + 1)
    current_investment = initial_investment

    for t in time_points:
        future_values[t] = current_investment
        current_investment = current_investment * (1 + annualized_return) + additional_investment

    return time_points, future_values


# Plot future values for each stock with additional annual investment
plt.figure(figsize=(14, 8))

for stock, annualized_return in annualized_returns.items():
    time_points, future_values_with_additional_investment = project_future_values(
        annualized_return, initial_investment_per_stock, additional_investment_per_year, years
    )
    plt.plot(time_points, future_values_with_additional_investment, marker='s', linestyle='--',
             label=f'{stock} (With Additional $200,000/year)')

# Aggregate total portfolio value with additional investment
total_portfolio_values_with_additional_investment = np.zeros(years + 1)

for stock, annualized_return in annualized_returns.items():
    _, future_values_with_additional_investment = project_future_values(
        annualized_return, initial_investment_per_stock, additional_investment_per_year, years
    )
    total_portfolio_values_with_additional_investment += future_values_with_additional_investment

# Adding the original investment of $1,000,000 to the future values from year 2 onwards
initial_total_investment = 1000000  # Original investment
total_portfolio_values_with_initial_investment = np.zeros(years + 1)
total_portfolio_values_with_initial_investment[0] = initial_total_investment

for t in range(1, years + 1):
    total_portfolio_values_with_initial_investment[t] = (initial_total_investment +
                                                         total_portfolio_values_with_additional_investment[t] -
                                                         total_portfolio_values_with_additional_investment[t - 1])

# Plot total portfolio value with additional investment
time_points = np.arange(0, years + 1)  # Time from 0 to years
plt.plot(time_points, total_portfolio_values_with_initial_investment, marker='^', linestyle=':', color='black',
         label='Total Portfolio (Original $1,000,000 + $200,000/year)')

# Add labels and title
plt.title("Projected Portfolio Values with Annual $200,000 Investment Per Stock (Sep 2024 - Aug 2029)", fontsize=16)
plt.xlabel("Years", fontsize=14)
plt.ylabel("Projected Value ($)", fontsize=14)
plt.ylim(0, max(total_portfolio_values_with_initial_investment) * 1.1)  # Adjust y-axis for better visualization

# Format y-axis with dollar signs
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "${:,}".format(int(x))))

# Adding grid and legend
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Show plot
plt.show()
