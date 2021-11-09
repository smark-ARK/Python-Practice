def weightOfOrder(w, g):
    weightOfWidgets = w*75
    weightOfGizmos = g*112
    totalWeight = weightOfWidgets+weightOfGizmos
    print('weightOfWidgets: ', weightOfWidgets, 'grams')
    print('weightOfGizmos:', weightOfGizmos, 'grams')
    return totalWeight


nOfWidgets = int(input('Enter the number of widgets in the order: '))
nOfGizmos = int(input('Enter the number of gizmos in the order: '))

print('The total weight of the order is: ',
      weightOfOrder(nOfWidgets, nOfGizmos), 'grams')
