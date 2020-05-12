import dask.dataframe as dd
#remove the url data and description field
dfu = dd.read_csv('us.csv', dtype={'year': 'float64'}, 
                usecols=['region','price','year','manufacturer','model','condition','cylinders',
                        'fuel','odometer','title_status','transmission','vin','drive','size',
                        'type','paint_color','county','state','lat','long'])

#cut down dataset to managable level for R
dfu = dfu.head(500)
dfu.to_csv('us500.csv', index=False)


dfg = dd.read_csv('germ.csv',  encoding = "ISO-8859-1")
dfg = dfg.head(500)
dfg.to_csv('germ500.csv', index=False)