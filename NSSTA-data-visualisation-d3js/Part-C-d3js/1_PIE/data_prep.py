import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    data=data[:10000]
    return data



def get_pie_data(data):
    wages_data = {}
    for item in data:
        salary=item["Wages or Salaries (Rs.)"]
        if salary<50000:
            wages_data['0-50k'] = wages_data.get('0-50k', 0) + 1
        elif salary<250000:
            wages_data['50k-250k'] = wages_data.get('50k-250k', 0) + 1
        elif salary<500000:
            wages_data['250k-500k'] = wages_data.get('250k-500k', 0) + 1
        elif salary<1000000:
            wages_data['500k-1M'] = wages_data.get('500k-1M', 0) + 1
        else:
            wages_data['1M+'] = wages_data.get('1M+', 0) + 1
    
    paid_days_data = {}
    for item in data:
        paid_days=item["Number of Man-days Paid For"]
        if paid_days<200:
            paid_days_data['0-200'] = paid_days_data.get('0-200', 0) + 1
        elif paid_days<400:
            paid_days_data['200-400'] = paid_days_data.get('200-400', 0) + 1
        elif paid_days<600:
            paid_days_data['400-600'] = paid_days_data.get('400-600', 0) + 1
        elif paid_days<1000:
            paid_days_data['600-1000'] = paid_days_data.get('600-1000', 0) + 1
        else:
            paid_days_data['1000+'] = paid_days_data.get('1000+', 0) + 1
    
    return wages_data, paid_days_data
        
    


if __name__ == "__main__":
    data = load_data('E-employment_labour_cost.json')
    wages_data, paid_days_data = get_pie_data(data)
    print("Wages Data:", wages_data)
    print("Paid Days Data:", paid_days_data)
    with open('wages_data.json', 'w') as file:
        json.dump(wages_data, file)
    
    with open('paid_days_data.json', 'w') as file:
        json.dump(paid_days_data, file)
        
    print("Data preparation completed. Wages and paid days data saved to JSON files.")