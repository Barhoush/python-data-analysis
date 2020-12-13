import pandas as pd
import glob


path = r'data' # use your path
all_files = glob.glob(path + "/*.csv")
li = []
maxIncomeMonth = {'month': all_files[0], 'income': 0}
maxStateOrders = {'state': '', 'orders': 0}
bestSalesTime   =   {'time': '', 'sales': 0}
bestProductSales   =   {'product': '', 'sales': 0}
bestStateOrders = {'state': '', 'sales': 0}

states  =   []
for index, filename in enumerate(all_files):
    df = pd.read_csv(filename, skiprows=0)
    df = df.rename(columns={'Order ID': 'id', 'Product': 'name', 'Quantity Ordered': 'quantity', 'Price Each': 'price',
                            'Order Date': 'date', 'Purchase Address': 'address'})
    df = df.dropna(how='any')
    df = df[pd.to_numeric(df['id'], errors='coerce').notnull()]
    df = df[pd.to_numeric(df['price'], errors='coerce').notnull()]
    df['state']  =   df['address'].str.split(', ').str[1]
    df['time']  =   df['date'].str.split(' ').str[1]
    bestTime = df['time'].value_counts()
    bestProduct =   df['name'].value_counts()
    bestState =   df['state'].value_counts()

    if(bestTime.max()   >   bestSalesTime['sales']):
        bestSalesTime['time'] = bestTime.idxmax()
        bestSalesTime['sales'] = bestTime.max()

    if(bestProduct.max()   >   bestProductSales['sales']):
        bestProductSales['product'] = bestProduct.idxmax()
        bestProductSales['sales'] = bestProduct.max()

    if(bestState.max()   >   bestStateOrders['sales']):
        bestStateOrders['state'] = bestState.idxmax()
        bestStateOrders['sales'] = bestState.max()

    shape   =   df.shape
    # print(df[df.price == df.price.max()])
    if(shape[0] >   maxIncomeMonth['income']):
        maxIncomeMonth['month']  =   filename
        maxIncomeMonth['income']  =   shape[0]

    # df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

# print(frame)
print("Q1) Month with most sales: ", maxIncomeMonth['month'])
print("Q2) State with most sales: ", bestStateOrders)
print("Q3) Best time to display advertisements to increase sales: ", bestSalesTime)
print("Q4) Best product had the highest sales count: ", bestProductSales)
