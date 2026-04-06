import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data():
    file_path = os.path.join("data", "saas_data.xlsx")
    df = pd.read_excel(file_path)
    return df

def calculate_conversion(df, column):
    result = df.groupby(column)['Opportunity Status'].value_counts().unstack(fill_value=0)
    result['Conversion %'] = (result['Won'] / (result['Won'] + result['Loss'])) * 100
    return result.sort_values('Conversion %', ascending=False)

def run_analysis():
    print("Loading dataset...")
    df = load_data()
    df.rename(columns={"Technology\nPrimary": "Technology"}, inplace=True)

    print(f"Total Records: {len(df)}")

    overall = (len(df[df['Opportunity Status'] == 'Won']) / len(df)) * 100
    print(f"Overall Conversion Rate: {round(overall,2)}%")

    tech = calculate_conversion(df, "Technology")
    channel = calculate_conversion(df, "B2B Sales Medium")

    print("\nConversion by Technology:\n", tech)
    print("\nConversion by Sales Channel:\n", channel)

    os.makedirs("output", exist_ok=True)

    tech['Conversion %'].plot(kind='bar', title="Conversion by Technology")
    plt.savefig("output/tech.png")
    plt.clf()

    channel['Conversion %'].plot(kind='bar', title="Conversion by Channel")
    plt.savefig("output/channel.png")
    plt.clf()

    print("\nCharts saved in output folder")