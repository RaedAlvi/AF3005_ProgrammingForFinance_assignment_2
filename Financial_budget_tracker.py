import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
import uuid 


if "page" not in st.session_state:
    st.session_state.page = "landing"
if "expenses" not in st.session_state:
    st.session_state.expenses = {}
if "utility_bills" not in st.session_state:
    st.session_state.utility_bills = {}
if "monthly_income" not in st.session_state:
    st.session_state.monthly_income = 0
if "investment_cost" not in st.session_state:
    st.session_state.investment_cost = 0
if "monthly_budget" not in st.session_state:
    st.session_state.monthly_budget = 0
if "timeline" not in st.session_state:
    st.session_state.timeline = 0




# Add the heading and subheading
import streamlit as st

def landing_page():
    # Apply CSS for styling and hover effect, and set the background color to black
    st.markdown(
        """
        <style>
            /* Apply a black background to the whole Streamlit app */
            .stApp {
                background-color: black !important;
                color: white !important;
            }

            /* Apply hover effect to text with the 'hover-text' class */
            .element-container .stMarkdown p.hover-text {
                background: none !important;
                color: #ffa260 !important;
                font-size: 1.5em !important;
                font-weight: bold !important;
                transition: color 0.25s, box-shadow 0.25s, transform 0.25s !important;
                display: inline-block !important;
                padding: 10px !important;
                margin: 0 !important;
            }

            .element-container .stMarkdown p.hover-text:hover {
                color: #f1ff5c !important;
                box-shadow: 0 0.5em 0.5em -0.4em #f1ff5c !important;
                transform: translateY(-0.25em) !important;
                cursor: pointer !important;
            }

            /* Apply a style for the title with larger font and highlight color */
            .stMarkdown h1 {
                color: #ffa260;
                font-size: 3em;
                font-weight: bold;
                transition: color 0.25s, box-shadow 0.25s, transform 0.25s;
            }

            .stMarkdown h1:hover {
                color: white;
                box-shadow: 0 0.5em 0.5em -0.4em #f1ff5c;
                transform: translateY(-0.25em);
                cursor: pointer;
            }
        </style>
        """, unsafe_allow_html=True
    )

    # Title with emojis, highlighted with hover effect
    st.markdown("<h1 class='hover-text'>💰 Welcome to Your Personal Finance Tracker!</h1>", unsafe_allow_html=True)
    st.markdown("### Let's help you save and track your finances like a pro! 🧮")

    # Key benefits section with emojis
    st.markdown("### 🌟 Why Choose Us?")
    st.markdown("""
    - 🧾 **Easily track your expenses**: Stay on top of where your money goes.
    - 📊 **Visualize your savings**: Interactive charts to monitor progress.
    - 🎯 **Set financial goals**: Achieve milestones with personalized plans.
    - 🚀 **Boost your financial health**: Take control of your future!
    """)

    # Call-to-action with a button
    st.markdown("### Ready to take control of your finances?")
    if st.button("🚀 Get Started Now"):
        st.success("Welcome aboard! Let's start tracking.")
        st.session_state.page = "savings"

    # Button to start tracking savings
    if st.button("Start Tracking Your Savings"):
        st.session_state.page = "savings"  # Navigate to the savings page



def savings_page():
    # Apply custom CSS for the Savings page
    st.markdown(
        """
        <style>
            /* Apply a black background to the entire page */
            .stApp {
                background-color: black !important;
                color: white !important;
            }

            /* Style the title */
            .stMarkdown h1 {
                color: #ffa260;
                font-size: 3.5em;
                font-weight: bold;
                transition: color 0.25s ease;
            }

            /* Style for input fields */
            .stTextInput, .stSelectbox, .stButton {
                background-color: #333 !important;
                color: white !important;
                border-radius: 5px;
                padding: 10px !important;
                font-size: 1.2em;
                border: 2px solid #555;
            }

            /* Change button background on hover */
            .stButton:hover {
                background-color: #f1ff5c !important;
                color: black !important;
            }

            /* Apply hover effect for text */
            .element-container .stMarkdown p.hover-text {
                background: none !important;
                color: #ffa260 !important;
                font-size: 1.5em !important;
                font-weight: bold !important;
                transition: color 0.25s, box-shadow 0.25s, transform 0.25s !important;
                display: inline-block !important;
                padding: 10px !important;
                margin: 0 !important;
            }

            .element-container .stMarkdown p.hover-text:hover {
                color: #f1ff5c !important;
                box-shadow: 0 0.5em 0.5em -0.4em #f1ff5c !important;
                transform: translateY(-0.25em) !important;
                cursor: pointer !important;
            }

        </style>
        """, unsafe_allow_html=True
    )

    # Title with hover effect
    st.markdown("## 💸 Savings Goal Tracker 💸")
    st.markdown("### Let's start saving for your future!")

    # User Input: What are you saving for?
    goal = st.text_input("What are you trying to save for? (e.g., car, vacation, house)")

    # Dropdown for timeline (month selection)
    months = [str(i) + " months" for i in range(1, 25)]  # Dropdown from 1 to 24 months
    timeline = st.selectbox("By when do you expect to make this purchase?", months)

    # Calculate remaining time
    time_remaining = int(timeline.split()[0])  # Extract the number of months
    st.markdown(f"### According to your timeline, you have about {time_remaining} months to save!")

    # Add a cool CTA button to navigate to the budget tracker
    if st.button("Go to Budget Tracker"):
        st.session_state.page = "budget"  # Navigate to the budget page

    # Add some space and info for motivation
    st.markdown("""
    **💡 Tip:** Break your savings goal into smaller milestones and track your progress every month!
    """, unsafe_allow_html=True)

def budget_page():
    st.markdown(
        """
        <style>
            /* Apply a black background to the entire page */
            .stApp {
                background-color: #1e1e1e !important;
                color: white !important;
            }

            /* Style the title */
            .stMarkdown h1 {
                color: #ffa260;
                font-size: 3.5em;
                font-weight: bold;
                transition: color 0.25s ease;
            }

            /* Style for input fields */
            .stNumberInput, .stButton {
                background-color: #333 !important;
                color: white !important;
                border-radius: 5px;
                padding: 10px !important;
                font-size: 1.2em;
                border: 2px solid #555;
            }

            /* Change button background on hover */
            .stButton:hover {
                background-color: #f1ff5c !important;
                color: black !important;
            }

            /* Apply hover effect for text */
            .element-container .stMarkdown p.hover-text {
                background: none !important;
                color: #ffa260 !important;
                font-size: 1.5em !important;
                font-weight: bold !important;
                transition: color 0.25s, box-shadow 0.25s, transform 0.25s !important;
                display: inline-block !important;
                padding: 10px !important;
                margin: 0 !important;
            }

            .element-container .stMarkdown p.hover-text:hover {
                color: #f1ff5c !important;
                box-shadow: 0 0.5em 0.5em -0.4em #f1ff5c !important;
                transform: translateY(-0.25em) !important;
                cursor: pointer !important;
            }
        </style>
        """, unsafe_allow_html=True
    )
    st.title("Monthly Budget Tracker")
    
    # Ask for monthly income, investment cost, and monthly savings target
    st.session_state.monthly_income = st.number_input(
        "What is your monthly income?", 
        min_value=1, 
        step=1000, 
        value=st.session_state.monthly_income if st.session_state.monthly_income >= 1 else 1
    )
    st.session_state.investment_cost = st.number_input(
        "What is the total cost of your investment (e.g., car, house)?", 
        min_value=1, 
        step=1000, 
        value=st.session_state.investment_cost if st.session_state.investment_cost >= 1 else 1
    )
    st.session_state.monthly_budget = st.number_input(
        "How much are you willing to save each month?", 
        min_value=1, 
        step=1000, 
        value=st.session_state.monthly_budget if st.session_state.monthly_budget >= 1 else 1
    )
    
    # Define months list and set current month based on datetime
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]

    # Limit the number of months to the selected timeline
    for current_month in range(st.session_state.timeline):
        month_name = months[current_month]
        st.subheader(f"Month {month_name} Expenses:")
        
        # Input for current month expenses with unique keys using uuid
        grocery = st.number_input(
            f"Enter Grocery expenses for {month_name}:",
            min_value=0, 
            value=st.session_state.expenses.get(month_name, {}).get("Grocery", 0), 
            key=f"grocery_{month_name}"
        )
        entertainment = st.number_input(
            f"Enter Entertainment expenses for {month_name}:",
            min_value=0, 
            value=st.session_state.expenses.get(month_name, {}).get("Entertainment", 0), 
            key=f"entertainment_{month_name}"
        )
        
        st.write("Select the utility bills for this month:")
        utilities = ['Maintenance', 'Electricity', 'Gas', 'Water', 'Other']
        
        selected_utilities = st.multiselect(
            f'Which utility bills would you like to track for {month_name}?',
            utilities, 
            default=list(st.session_state.expenses.get(month_name, {}).get("Utilities", {}).keys()), 
            key=f"utilities_{month_name}"
        )
        
        # Create a dictionary to hold the utility values for the current month
        utility_values = {}
        for utility in selected_utilities:
            price = st.number_input(
                f"Enter the price for {utility} for {month_name}", 
                min_value=0, 
                value=st.session_state.expenses.get(month_name, {}).get("Utilities", {}).get(utility, 0), 
                key=f"utility_{utility}_{month_name}"
            )
            utility_values[utility] = price

        # Save the current month's expenses in session state
        st.session_state.expenses[month_name] = {
            "Grocery": grocery, 
            "Entertainment": entertainment, 
            "Utilities": utility_values
        }

        # Display the bar chart after expenses for the current month
        display_monthly_expenses_vs_savings([month_name], st.session_state.expenses, st.session_state.monthly_income)
        
        # Ask if the user wants to record expenses for the next month
        if current_month == st.session_state.timeline - 1:
            break  # Exit the loop if we've reached the last month

        # If we haven't reached the last month yet, ask for the next month
        record_next_month = st.radio(
            f"Would you like to record your expenses for {months[current_month + 1]}?", 
            ("Yes", "No"), 
            key=f"record_next_month_{months[current_month]}", 
            index=1
        )
        
        if record_next_month == "No":
            break  # Exit the loop if user doesn't want to continue

    # After exiting the loop, display a final summary for the last recorded month
    final_month = months[min(st.session_state.timeline - 1, 11)]
    final_data = st.session_state.expenses.get(final_month, {"Grocery": 0, "Entertainment": 0, "Utilities": {}})
    total_expenses = (final_data["Grocery"] + final_data["Entertainment"] + sum(final_data["Utilities"].values()))
    remaining_budget = st.session_state.monthly_income - total_expenses
        
    st.write(f"Total Expenses for {final_month}: ${total_expenses}")
    st.write(f"Remaining Budget for {final_month}: ${remaining_budget}")
        
    # Calculate the savings journey towards the investment goal for the last month
    savings_per_month = st.session_state.monthly_budget - total_expenses
    months_to_reach_goal = st.session_state.investment_cost / savings_per_month if savings_per_month > 0 else 0

    # Calculate total savings over the months
    total_savings = savings_per_month * st.session_state.timeline  # Accumulated savings

    st.write(f"Remaining Budget for {final_month}: ${remaining_budget}")
    # Check if the user has saved enough to purchase the item
    if total_savings >= st.session_state.investment_cost:
        st.image("Emerald_badge.png", use_container_width=True,width=200)  # Display the Emerald Badge
        st.success("🎉 You've now saved up enough to purchase your dream item! 🎉")
        st.write("You've now become a financial master. Congratulations on your success!")
        st.write("🎉✨ **Each emerald has a unique ID across Pakistan** ✨🎉\n\n"
         "🍽️🎉 **You can now get up to 70% off across all restaurants!** 🍽️💸\n\n"
         "🎁🎉 **Enjoy your financial mastery!** 🎉🎁")

    else:
        st.write("🚧 Keep going! You're on the right track to achieving your goal!")
    
    # Display the Savings Progress Line Chart
    display_progress_graph(st.session_state.investment_cost, months_to_reach_goal, savings_per_month)
    
    if st.button("Go Back to Home Page", key="back_home"):
        st.session_state.page = "landing"


def display_clustered_line_chart(expenses, monthly_income):
    # Extract months from the expenses data
    months = list(expenses.keys())  
    total_expenses = []
    savings = []

    # Calculate total expenses and savings for each month
    for month in months:
        month_data = expenses[month]
        grocery_expenses = month_data["Grocery"]
        entertainment_expenses = month_data["Entertainment"]
        utility_expenses = sum(month_data["Utilities"].values())  # Sum all utility values

        total_expenses.append(grocery_expenses + entertainment_expenses + utility_expenses)
        savings.append(monthly_income - total_expenses[-1])

    # Debugging: Print out the expenses and savings data to verify
    print("Expenses Data:", expenses)
    print("Total Expenses:", total_expenses)
    print("Savings Data:", savings)
    print("Monthly Income:", monthly_income)
    
    # Check if the months, total_expenses, and savings lists have the same length
    if len(months) != len(total_expenses) or len(months) != len(savings):
        print("Data Length Mismatch! Check the lists.")
    
    # Create the clustered line chart
    fig = go.Figure()

    # Add expenses line (in red)
    fig.add_trace(go.Scatter(
        x=months,
        y=total_expenses,
        mode='lines+markers',
        name='Total Expenses',
        line=dict(color='red', width=4),
        marker=dict(size=8)
    ))

    # Add savings line (in blue)
    fig.add_trace(go.Scatter(
        x=months,
        y=savings,
        mode='lines+markers',
        name='Savings',
        line=dict(color='blue', width=4),
        marker=dict(size=8)
    ))

    # Update layout for dark theme
    fig.update_layout(
        title="Expenses vs Savings Comparison",
        xaxis_title="Months",
        yaxis_title="Amount ($)",
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='white'),
        title_x=0.5,
        showlegend=True
    )

    # Display the clustered line chart
    st.plotly_chart(fig, use_container_width=True, key="clustered_line_chart")


# **Display Savings Progress Graph**
def display_progress_graph(investment_cost, months_to_reach_goal, savings_per_month):
    # Check if there is at least one month to plot
    if int(months_to_reach_goal) < 1:
        st.write("Savings progress chart cannot be displayed because your savings per month are too low to reach the goal.")
        return

    months = [i for i in range(1, int(months_to_reach_goal) + 1)]
    savings = [savings_per_month * i for i in months]

    # Create the plot
    fig = go.Figure()

    # Add the savings line
    fig.add_trace(go.Scatter(
        x=months,
        y=savings,
        mode='lines+markers',
        name='Savings Progress',
        line=dict(color='blue', width=4),
        marker=dict(size=8)
    ))

    # Add the investment goal line
    fig.add_trace(go.Scatter(
        x=[months[0], months[-1]],
        y=[investment_cost, investment_cost],
        mode='lines',
        name='Investment Goal',
        line=dict(color='red', dash='dash')
    ))

    # Update layout for dark theme
    fig.update_layout(
        title="Savings Goal Progress",
        xaxis_title="Months",
        yaxis_title="Total Savings ($)",
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='white'),
        title_x=0.5,
        showlegend=True
    )
    st.plotly_chart(fig)


# **Display Monthly Expenses vs Savings Bar Chart**
def display_monthly_expenses_vs_savings(months, expenses, monthly_income):
    expense_values = []
    savings_values = []
    
    # Ensure the month exists in the expenses before accessing
    for month in months:
        if month in expenses:
            grocery_expenses = expenses[month]["Grocery"]
            entertainment_expenses = expenses[month]["Entertainment"]
            utility_expenses = sum(expenses[month]["Utilities"].values())  # Sum all utility values

            # Calculate total expenses for the month
            total_expenses = grocery_expenses + entertainment_expenses + utility_expenses
            expense_values.append(total_expenses)
            savings_values.append(monthly_income - total_expenses)
        else:
            expense_values.append(0)  # If no expense data for the month, set it to 0
            savings_values.append(monthly_income)  # Assume all income is savings if no expenses

    fig = go.Figure()

    # Expenses Bar
    fig.add_trace(go.Bar(
        x=months,
        y=expense_values,
        name='Total Expenses',
        marker=dict(color='red')
    ))

    # Savings Bar
    fig.add_trace(go.Bar(
        x=months,
        y=savings_values,
        name='Savings',
        marker=dict(color='blue')
    ))

    # Update layout for dark theme
    fig.update_layout(
        title="Monthly Expenses vs Savings",
        xaxis_title="Months",
        yaxis_title="Amount ($)",
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='white'),
        barmode='group',
        title_x=0.5
    )
    
    # Provide a unique key for the plotly chart to avoid duplicate element ID error
    st.plotly_chart(fig, use_container_width=True, key=f"expenses_vs_savings_{uuid.uuid4()}")

# Main Flow Based on Current Page in Session State
if st.session_state.page == "landing":
    landing_page()
elif st.session_state.page == "savings":
    savings_page()
elif st.session_state.page == "budget":
    budget_page()
