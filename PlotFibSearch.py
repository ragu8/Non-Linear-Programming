import matplotlib.pyplot as plt

def plot(df):
    # Reset index to start from 1
    df.index = range(1, len(df) + 1)

    # Extracting relevant columns
    iterations = df.index
    L_values = df['L']
    R_values = df['R']
    optimum_value = df['optium'].iloc[-1]  # Final optimum value

    # Plotting each iteration separately
    for i in iterations:
        if i == 1:
            continue  # Skip first iteration as there is no previous data point
        plt.plot([L_values[i-1], R_values[i-1]], [L_values[i], R_values[i]], label=f"Iteration {i}", linestyle='-', marker='o')

    # Marking each iteration with a marker
    for i in iterations:
        plt.scatter(L_values[i], R_values[i], color='red', marker='o')
        plt.text(L_values[i], R_values[i], f'{i}', fontsize=9, verticalalignment='bottom')

    # Marking the final optimum point
    plt.scatter(L_values.iloc[-1], R_values.iloc[-1], color='green', marker='o', label='Final Optimum')
    plt.text(L_values.iloc[-1], R_values.iloc[-1], f'Optimum: {optimum_value}', fontsize=9, verticalalignment='bottom')

    # Highlighting the initial point
    plt.scatter(L_values.iloc[0], R_values.iloc[0], color='blue', marker='o', label='Initial Point')
    plt.text(L_values.iloc[0], R_values.iloc[0], 'Initial', fontsize=9, verticalalignment='bottom')

    plt.xlabel('L')
    plt.ylabel('R')
    plt.title('Plot of Fibonacci search method for Each Iteration')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()  # Adjust layout to prevent overlap of text
    plt.show()
