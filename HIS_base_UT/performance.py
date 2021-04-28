from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def confusion_matrix(data):
    acc = accuracy_score(data['Label'], data['predict'])
    #precision = precision_score(data['Label'], data['predict'], average='weighted')
    #recall = recall_score(data['Label'], data['predict'], average='weighted')
    #f1 = f1_score(data['Label'], data['predict'], average='weighted')

    print("Accuracy : {:.4f}".format(acc))
    #print("Precision : {:.4f}".format(precision))
    #print("Recall : {:.4f}".format(recall))
    #print("F1-score : {:.4f}".format(f1))