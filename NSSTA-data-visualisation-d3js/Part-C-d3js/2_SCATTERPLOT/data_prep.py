import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    data=data[:1000]
    return data



def get_scatterplot_data(data):
    man_days_data = []
    for item in data:
        if item["Man-days Worked - Total"] != 0:
            man_days_data.append(item["Man-days Worked - Total"])
    return man_days_data
        
    


if __name__ == "__main__":
    data = load_data('E-employment_labour_cost.json')
    man_days_data = get_scatterplot_data(data)
    print("Man Days Data:", man_days_data)
    with open('man_days_data.json', 'w') as file:
        json.dump(man_days_data, file)
    
        
    print("Data preparation completed. Wages and paid days data saved to JSON files.")