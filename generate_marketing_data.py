import pandas as pd
import numpy as np

print("⏳ customized data generation in progress...")
np.random.seed(42)
n_users = 30000


channels = np.random.choice(
    ['TikTok Ads', 'Google Search', 'Meta Ads', 'Organic SEO', 'Email Referral'], 
    n_users, 
    p=[0.35, 0.20, 0.25, 0.15, 0.05]
)
devices = np.random.choice(['iOS', 'Android', 'Web PC'], n_users, p=[0.45, 0.40, 0.15])


signup_prob = {'TikTok Ads': 0.3, 'Google Search': 0.6, 'Meta Ads': 0.4, 'Organic SEO': 0.7, 'Email Referral': 0.85}
signups = [1 if np.random.rand() < signup_prob[c] else 0 for c in channels]


purchase_prob = {'TikTok Ads': 0.08, 'Google Search': 0.25, 'Meta Ads': 0.12, 'Organic SEO': 0.35, 'Email Referral': 0.50}
purchases = [1 if (s == 1 and np.random.rand() < purchase_prob[c]) else 0 for s, c in zip(signups, channels)]


cac = [np.random.uniform(8, 15) if c in ['TikTok Ads', 'Meta Ads'] 
       else np.random.uniform(15, 30) if c == 'Google Search' 
       else 0 for c in channels]


ltv = [np.random.uniform(40, 200) if p == 1 else 0 for p in purchases]


df = pd.DataFrame({
    'User_ID': range(100000, 100000 + n_users),
    'Channel': channels,
    'Device': devices,
    'Is_Signed_Up': signups,
    'Is_Purchased': purchases,
    'Customer_Acquisition_Cost': cac,
    'Lifetime_Value': ltv
})

df.to_csv('marketing_growth_data.csv', index=False)
print("✅ Perfect! Customized dataset `marketing_growth_data.csv` has been generated with 30,000 rows of real user flow data.")