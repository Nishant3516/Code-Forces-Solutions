def advancers(scores, n, k):
    threshold_score = scores[k - 1]
    count = sum(1 for score in scores if score >= threshold_score and score > 0)
    
    return count
        

N, k = list(map(int,input().split()))
scores=list(map(int,input().split()))
print(advancers(scores,N,k))
