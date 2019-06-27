import pandas as pd
#import matplotlib.pylot as plt
import seaborn as sns



#get column names

column_names = ['user_id','item_id','rating','timestamps']
#getting the ratings and timestamps
df = pd.read_csv('data.csv')

#reading the movie dataset 
movie_titles = pd.read_csv('movies.csv')

#print(df.head())
data = pd.merge(df, movie_titles, on='item_id')
#calculating the mean rating of all the movie
mean = data.groupby('title')['rating'].mean().sort_values(ascending=False).head()

#print(mean)

#calculate count rating for all the movie
count = data.groupby('title')['rating'].count().sort_values(ascending=False).head()

#creating dataframe with 'rating' count values

ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())

#sorting values according to the 'num of rating columns'

moviemat = data.pivot_table(index='user_id',columns='title',values='rating')
prom = ratings.sort_values('num of ratings',ascending=False).head(10)


#analysing correlation with similar movies 

starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']

#getting similar movie recommendation with correlations 

similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

#operation for starwars like movies 
corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace = True)
#print(corr_starwars.head())

#similar movies 

sim = corr_starwars.sort_values('Correlation',ascending=False).head(10)
corr_starwars = corr_starwars.join(ratings['num of ratings'])

#print(corr_starwars.head())

recom = corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head() 
#print(recom)


#operation for some comedy movies like liar liar

corr_liarliar = pd.DataFrame(similar_to_liarliar,columns=['Correlation'])
corr_liarliar.dropna(inplace= True)

sim = corr_liarliar.sort_values('Correlation',ascending=False).head(10)
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])

recom_ll = corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation',ascending = False).head()
print(recom_ll)
