#!/usr/bin/env python
# coding: utf-8

# ## Exploratory Data Analysis on World Happiness Project 2022

# ## Installing Python Libraries for EDA

# In[1]:


#importing the necessary libraries for exploratory data analysis
get_ipython().system('pip install plotly')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')
print('libraries imported')


# ## Importing our data

# In[2]:


#importing our csv data
data= pd.read_csv('C:/Users/user/Downloads/2022.csv')


# In[3]:


#checking the first five rows of our data
data.head()


# In[4]:


#checking the columns in our data
data.columns


# In[5]:


#extracting the colums we will be using from our dataframe for analysis
data_columns= ['Country', 'Happiness score', 'Explained by: GDP per capita','Explained by: Social support', 
               'Explained by: Healthy life expectancy', 'Explained by: Freedom to make life choices', 'Explained by: Generosity',
               'Explained by: Perceptions of corruption']
data_df= data[data_columns].copy()
data_df.head()


# In[6]:


#rename our columns
data_df.rename({'Country': 'country_name', 'Happiness score': 'happiness_score', 
                'Explained by: GDP per capita': 'GDP_per_capita', 'Explained by: Social support': 'social_support', 
                'Explained by: Healthy life expectancy': 'healthy_life_expectancy', 
                'Explained by: Freedom to make life choices': 'freedom_to_make_life_choices', 
                'Explained by: Generosity': 'generosity', 'Explained by: Perceptions of corruption': 'perceptions_by_corruption'},
               axis= 'columns', inplace= True)


# In[7]:


data_df.head()


# ## Data Cleaning

# In[8]:


#checking for null values
data_df.isnull().sum()


# In[9]:


#we have only a row where all its values are missing so we decide to drop it
data_df.dropna(inplace=True)


# In[10]:


#confirming if we still have a Nan values in our dataframe
data_df.isna().any()


# In[11]:


#to see the number of rows and columns of our dataframe
data_df.shape


# In[12]:


#to see information about our dataframe
data_df.info()


# In[13]:


#converting object typed data to float
#however because of a comma in the data, we can't convert it yet
#we have to remove the comma first, otherwise python will raise an error when we try to convert to float
data_df.replace(",", ".", regex=True, inplace=True)
data_df[['happiness_score', 'GDP_per_capita', 'social_support', 'healthy_life_expectancy', 'freedom_to_make_life_choices',
         'generosity', 'perceptions_by_corruption']]= data_df[['happiness_score', 'GDP_per_capita', 'social_support', 
                                                               'healthy_life_expectancy', 'freedom_to_make_life_choices', 
                                                               'generosity', 'perceptions_by_corruption']].astype(float)


# In[16]:


#confitming to see if our column data types have been changed
data_df.dtypes


# In[17]:


data_df.head()


# ## Data Visualization

# In[18]:


#plotting a box plot with our gdp per capita column
plt.figure(figsize=(8,5))
sns.boxplot(x='GDP_per_capita', data=data_df)
plt.title('GDP Per Capita Box Plot', fontsize=15)

#we can see we have an outlier here


# In[19]:


#plotting a correlation map
corr= data_df.corr(method='spearman')
f, ax=plt.subplots(figsize=(10,5))
sns.heatmap(corr, mask= np.zeros_like(corr, dtype=bool)
           ,cmap='magma', square= True, ax=ax)


# In[20]:


#plotting a pair grid to observe the relationships in our dataset
p= sns.PairGrid(data_df)
p.map(sns.scatterplot, edgecolor='white')


# In[21]:


#top 10 happiest countries
top_10_happy= data_df.sort_values('happiness_score',ascending= False,ignore_index=True)[['country_name', 'happiness_score']].head(10)


# In[22]:


#bar chart of the 10 most happy country
plt.figure(figsize=(10,8))
sns.set_theme(style= 'darkgrid')
plt.title('Top 10 happiest Countries', fontsize= 15, color='red')
bar =sns.barplot(x= 'country_name', y= 'happiness_score', data= top_10_happy, palette='Set2', linewidth= 4.0, errwidth=5 )
plt.xlabel('Country Name', fontsize=12)
plt.ylabel('Happiness Score', fontsize=12)
plt.xticks(rotation =30)


# In[23]:


#least 10 happiest countries
least_10_happy= data_df.sort_values('happiness_score',ascending= False,ignore_index=True)[['country_name', 'happiness_score']].tail(10)


# In[24]:


#bar chart of the 10 least happiest country
plt.figure(figsize=(10,8))
sns.set_theme(style= 'darkgrid')
plt.title('Least 10 happiest Countries', fontsize= 15, color='red')
bar= sns.barplot(x= 'country_name', y= 'happiness_score', data= least_10_happy, palette='Paired', linewidth= 4.0, errwidth=5 )
plt.xlabel('Country Name', fontsize=12)
plt.ylabel('Happiness Score', fontsize= 12)
plt.xticks(rotation =30, ha='right')


# In[25]:


#plotting a reg plot between gdp per capia and happiness score
plt.figure(figsize=(10,8))
sns.set_theme(style= 'darkgrid')
sns.regplot(x= 'GDP_per_capita', y= 'happiness_score', data= data_df)
plt.title('Regression Plot Between GDP Per Capita and Happiness Score', fontsize= 15)
plt.xlabel('GDP Per Capita', fontsize= 12)
plt.ylabel('Happiness Score', fontsize=12)


# In[26]:


#plotting a reg plot between healthy life expectancy and happiness score
plt.figure(figsize=(10,8))
sns.set_theme(style= 'darkgrid')
sns.regplot(x= 'healthy_life_expectancy', y= 'happiness_score', data= data_df)
plt.title('Regression Plot Between Healthy Life Expectancy and Happiness Score', fontsize= 15)
plt.xlabel('Healthy Life Expectancy', fontsize= 12)
plt.ylabel('Happiness Score', fontsize=12)


# In[27]:


#plotting a reg plot between freedom to make life choices and happiness score
plt.figure(figsize=(10,8))
sns.set_theme(style='darkgrid')
sns.regplot(x='freedom_to_make_life_choices', y='happiness_score', data= data_df)
plt.xlabel('Freedom to make life choices', fontsize=12)
plt.ylabel('Happiness Score', fontsize= 12)
plt.title('Regression between Freedom to make life choices and Happiness Score', fontsize=15, color='black')


# In[28]:


#using plotly express to plot a bubble chart betwen hapiness score and perceptions by corruption
fig=px.scatter(x='perceptions_by_corruption',y='happiness_score', data_frame=data_df,size='GDP_per_capita', 
               hover_data=['country_name'], title=('Bubble Plot Between Happiness Score and Perceptions by Corruption'),
               color='country_name', labels={'happiness_score': 'Happiness Score', 'perceptions_by_corruption': 'Corruption Index'},
              template='plotly_dark')
fig.show()

#adding colors when you have multiple variables in a dataset is not ideal as anyone looking at it will constantly
#have to look at the labels to identify which variable he is looking at
#however because I'm using an interactive plot and have included the country names when you hover on each
#it shouldn't be confusing reading it

