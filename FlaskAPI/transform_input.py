import numpy as np

COLUMNS = [
    'Rating',
    'num_comp',
    'hourly',
    'employer_provided',
    'same_state',
    'age',
    'python_yn',
    'spark',
    'excel',
    'desc_len',
    'Size_-1',
    'Size_1 to 50 employees',
    'Size_10000+ employees',
    'Size_1001 to 5000 employees',
    'Size_201 to 500 employees',
    'Size_5001 to 10000 employees',
    'Size_501 to 1000 employees',
    'Size_51 to 200 employees',
    'Size_Unknown',
    'Type of ownership_-1',
    'Type of ownership_College / University',
    'Type of ownership_Company - Private',
    'Type of ownership_Company - Public',
    'Type of ownership_Government',
    'Type of ownership_Hospital',
    'Type of ownership_Nonprofit Organization',
    'Type of ownership_Other Organization',
    'Type of ownership_School / School District',
    'Type of ownership_Subsidiary or Business Segment',
    'Type of ownership_Unknown',
    'Industry_-1',
    'Industry_Accounting',
    'Industry_Advertising & Marketing',
    'Industry_Aerospace & Defense',
    'Industry_Architectural & Engineering Services',
    'Industry_Auctions & Galleries',
    'Industry_Banks & Credit Unions',
    'Industry_Beauty & Personal Accessories Stores',
    'Industry_Biotech & Pharmaceuticals',
    'Industry_Brokerage Services',
    'Industry_Colleges & Universities',
    'Industry_Computer Hardware & Software',
    'Industry_Construction',
    'Industry_Consulting',
    'Industry_Consumer Product Rental',
    'Industry_Consumer Products Manufacturing',
    'Industry_Department, Clothing, & Shoe Stores',
    'Industry_Education Training Services',
    'Industry_Energy',
    'Industry_Enterprise Software & Network Solutions',
    'Industry_Farm Support Services',
    'Industry_Federal Agencies',
    'Industry_Financial Analytics & Research',
    'Industry_Financial Transaction Processing',
    'Industry_Food & Beverage Manufacturing',
    'Industry_Gambling',
    'Industry_Gas Stations',
    'Industry_Health Care Products Manufacturing',
    'Industry_Health Care Services & Hospitals',
    'Industry_Health, Beauty, & Fitness',
    'Industry_IT Services',
    'Industry_Industrial Manufacturing',
    'Industry_Insurance Agencies & Brokerages',
    'Industry_Insurance Carriers',
    'Industry_Internet',
    'Industry_Investment Banking & Asset Management',
    'Industry_K-12 Education',
    'Industry_Lending',
    'Industry_Logistics & Supply Chain',
    'Industry_Metals Brokers',
    'Industry_Mining',
    'Industry_Motion Picture Production & Distribution',
    'Industry_Other Retail Stores',
    'Industry_Real Estate',
    'Industry_Religious Organizations',
    'Industry_Research & Development',
    'Industry_Security Services',
    'Industry_Social Assistance',
    'Industry_Sporting Goods Stores',
    'Industry_Staffing & Outsourcing',
    'Industry_Stock Exchanges',
    'Industry_TV Broadcast & Cable Networks',
    'Industry_Telecommunications Manufacturing',
    'Industry_Telecommunications Services',
    'Industry_Transportation Equipment Manufacturing',
    'Industry_Transportation Management',
    'Industry_Travel Agencies',
    'Industry_Trucking',
    'Industry_Video Games',
    'Industry_Wholesale',
    'Sector_-1',
    'Sector_Accounting & Legal',
    'Sector_Aerospace & Defense',
    'Sector_Agriculture & Forestry',
    'Sector_Arts, Entertainment & Recreation',
    'Sector_Biotech & Pharmaceuticals',
    'Sector_Business Services',
    'Sector_Construction, Repair & Maintenance',
    'Sector_Consumer Services',
    'Sector_Education',
    'Sector_Finance',
    'Sector_Government',
    'Sector_Health Care',
    'Sector_Information Technology',
    'Sector_Insurance',
    'Sector_Manufacturing',
    'Sector_Media',
    'Sector_Mining & Metals',
    'Sector_Non-Profit',
    'Sector_Oil, Gas, Energy & Utilities',
    'Sector_Real Estate',
    'Sector_Retail',
    'Sector_Telecommunications',
    'Sector_Transportation & Logistics',
    'Sector_Travel & Tourism',
    'Revenue_$1 to $2 billion (USD)',
    'Revenue_$1 to $5 million (USD)',
    'Revenue_$10 to $25 million (USD)',
    'Revenue_$10+ billion (USD)',
    'Revenue_$100 to $500 million (USD)',
    'Revenue_$2 to $5 billion (USD)',
    'Revenue_$25 to $50 million (USD)',
    'Revenue_$5 to $10 billion (USD)',
    'Revenue_$5 to $10 million (USD)',
    'Revenue_$50 to $100 million (USD)',
    'Revenue_$500 million to $1 billion (USD)',
    'Revenue_-1',
    'Revenue_Less than $1 million (USD)',
    'Revenue_Unknown / Non-Applicable',
    'job_state_AL',
    'job_state_AZ',
    'job_state_CA',
    'job_state_CO',
    'job_state_CT',
    'job_state_DC',
    'job_state_DE',
    'job_state_FL',
    'job_state_GA',
    'job_state_IA',
    'job_state_ID',
    'job_state_IL',
    'job_state_IN',
    'job_state_KS',
    'job_state_KY',
    'job_state_LA',
    'job_state_MA',
    'job_state_MD',
    'job_state_MI',
    'job_state_MN',
    'job_state_MO',
    'job_state_NC',
    'job_state_NE',
    'job_state_NJ',
    'job_state_NM',
    'job_state_NY',
    'job_state_OH',
    'job_state_OR',
    'job_state_PA',
    'job_state_RI',
    'job_state_SC',
    'job_state_TN',
    'job_state_TX',
    'job_state_UT',
    'job_state_VA',
    'job_state_WA',
    'job_state_WI',
    'job_simp_analyst',
    'job_simp_data engineer',
    'job_simp_data scientist',
    'job_simp_director',
    'job_simp_manager',
    'job_simp_mle',
    'job_simp_na',
    'seniority_jr',
    'seniority_na',
    'seniority_senior',
]

def transform_input(form_data):
    features = {col: 0 for col in COLUMNS}
    
    features['Rating'] = float(form_data.get('rating', 0))
    features['num_comp'] = float(form_data.get('num_comp', 0))
    features['hourly'] = int(form_data.get('hourly', 0))
    features['employer_provided'] = int(form_data.get('employer_provided', 0))
    features['same_state'] = int(form_data.get('same_state', 0))
    features['age'] = float(form_data.get('age', 0))
    features['python_yn'] = int(form_data.get('python_yn', 0))
    features['spark'] = int(form_data.get('spark', 0))
    features['excel'] = int(form_data.get('excel', 0))
    features['desc_len'] = float(form_data.get('desc_len', 0))
    
    size = form_data.get('size', '')
    if f'Size_{size}' in features:
        features[f'Size_{size}'] = 1
        
    ownership = form_data.get('ownership', '')
    if f'Type of ownership_{ownership}' in features:
        features[f'Type of ownership_{ownership}'] = 1
        
    industry = form_data.get('industry', '')
    if f'Industry_{industry}' in features:
        features[f'Industry_{industry}'] = 1
        
    sector = form_data.get('sector', '')
    if f'Sector_{sector}' in features:
        features[f'Sector_{sector}'] = 1
        
    revenue = form_data.get('revenue', '')
    if f'Revenue_{revenue}' in features:
        features[f'Revenue_{revenue}'] = 1
        
    state = form_data.get('job_state', '')
    if f'job_state_{state}' in features:
        features[f'job_state_{state}'] = 1
        
    job_simp = form_data.get('job_simp', '')
    if f'job_simp_{job_simp}' in features:
        features[f'job_simp_{job_simp}'] = 1
        
    seniority = form_data.get('seniority', '')
    if f'seniority_{seniority}' in features:
        features[f'seniority_{seniority}'] = 1
    
    return [features[col] for col in COLUMNS]
