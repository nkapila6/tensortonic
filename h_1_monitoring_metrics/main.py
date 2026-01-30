# 30.01.2026, 2:36 PM
# Nikhil Kapila
# https://www.tensortonic.com/problems/monitoring-metrics-selection

def compute_clf(y_true, y_pred):
    tp = sum([y_t==1 and y_p==1 for (y_t,y_p) in zip(y_true, y_pred)])
    tn = sum([y_t==0 and y_p==0 for (y_t,y_p) in zip(y_true, y_pred)])
    fp = sum([y_t==0 and y_p==1 for (y_t,y_p) in zip(y_true, y_pred)])
    fn = sum([y_t==1 and y_p==0 for (y_t,y_p) in zip(y_true, y_pred)])
    n = len(y_true)
    
    acc = (tp+tn)/n
    prec = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1 = (2*prec*recall)/(prec+recall)

    return [("accuracy", acc), ("f1", f1), ("precision", prec), ("recall", recall)]

def compute_reg(y_true, y_pred):
    n = len(y_true)
    mae = 1/n * sum([abs(yt-yp) for (yt,yp) in zip(y_true, y_pred)])
    rmse =(1/n * sum([abs(yt-yp)**2 for (yt,yp) in zip(y_true, y_pred)]))**0.5

    return [("mae", round(mae,4)), ("rmse", round(rmse,4))]

def compute_ranking(y_true, y_pred):
    sorted_relevance = sorted(zip(y_pred, y_true), key=lambda x:x[0], reverse=True)
    sorted_relevance = [item[1] for item in sorted_relevance]
    top_3 = sorted_relevance[:3]

    relevant_top_3 = sum(top_3)
    prec = relevant_top_3/3.0

    total_relevant = sum(y_true)
    if total_relevant==0:
        recall = 0.0
    else:
        recall = relevant_top_3/total_relevant

    return sorted([("precision_at_3", float(prec)), ("recall_at_3", float(recall))])

def compute_monitoring_metrics(system_type, y_true, y_pred):
    """
    Compute the appropriate monitoring metrics for the given system type.
    """

    if system_type=="classification":
        return compute_clf(y_true, y_pred)

    if system_type=="regression":
        return compute_reg(y_true, y_pred)

    if system_type=="ranking":
        return compute_ranking(y_true, y_pred)

def main():
    input = "classification", [1, 0, 1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1, 1, 0]
    print(compute_monitoring_metrics(*input))

    input = "regression", [3.0, 5.0, 2.5, 7.0], [2.5, 5.5, 2.0, 8.0]
    print(compute_monitoring_metrics(*input))


if __name__ == "__main__":
    main()
