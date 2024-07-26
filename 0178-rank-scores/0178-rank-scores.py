import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    if len(scores['score']) == 0:
        scores['rank'] = []
        return pd.DataFrame(scores[['score','rank']])
    scores = scores.sort_values(by='score',ascending=False)
    scores = scores.reset_index()
    curr = scores['score'].max()
    scores['rank'] = 0
    scores.loc[0,'rank'] = 1 
    for x in range(1,len(scores)):
        if scores.loc[x,'score'] == curr:
            scores.loc[x,'rank'] = scores.loc[x-1,'rank']
            curr = scores.loc[x,'score']
        elif scores.loc[x,'score'] < curr:
            scores.loc[x,'rank'] = scores.loc[x-1,'rank'] + 1
            curr = scores.loc[x,'score']
    
    return pd.DataFrame(scores[['score','rank']])