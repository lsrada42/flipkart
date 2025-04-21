import pandas as pd
from langchain_core.documents import Document

#data converter - convert csv file to document format
def dataconverter():
    product_data = pd.read_csv("data/flipkart_product_review.csv")
    
    data = product_data[["product_title","review"]]
    
    product_list = [] 

    #iterate over the rows of the df
    for index, row in product_data.iterrows():
        object = {
            'product_name': row['product_title'], 
            'review': row['review']
        }

        ## append to product list
        product_list.append(object)
        
    #converting to document format
    docs = []

    for object in product_list: 
        metadata = {'product_name' : object['product_name']}
        page_content = object['review']

        doc = Document(page_content = page_content, metadata = metadata)

        docs.append(doc)
        
    return docs
        