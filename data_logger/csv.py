import pandas as pd
from pathlib import Path

def create_csv_file(csv_path = "./data/logs", filename = "log"):
    # Make csv file using pathname
    df = pd.DataFrame({'ID': [],
                   'Classname': [],
                   'x_min': [],
                   'y_min': [],
                   'x_max': [],
                   'y_max': []})
    filepath = Path(str(csv_path)+'/'+str(filename)+'.csv')  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    df.to_csv(filepath)  
    df.to_csv(index=False)


def read_csv_file(csv_path, filename): 
    # Read csv file 
    df = pd.read_csv(str(csv_path)+'/'+str(filename)+'.csv')
    df.drop('Unnamed: 0', axis=1, inplace=True)
    print(df.columns)
    return df

def save_csv_file(df, csv_path, filename):
    # Save dataframe to a file
    df.to_csv(str(csv_path)+'/'+str(filename)+'.csv')  
    df.to_csv(index=False)

def add_data(df, id, class_name, bounding_box):
    """
    Save information of an objects that are detected to dataframe
    """
    try:
        # Check whether the object is detected before. If not, add to the dataframe
        if id in df.loc[:,'ID'].values: 
            id_row = df.index[df['ID']==id].tolist()
            df.loc[id_row, ['ID', 'Classname', 'x_min', 'y_min', 'x_max', 'y_max']] = [id, class_name, (int(bounding_box[0]), int(bounding_box[1]), int(bounding_box[2]), int(bounding_box[3]))]
        else:
            df_new = pd.DataFrame([[id, class_name, int(bounding_box[0]), int(bounding_box[1]), int(bounding_box[2]), int(bounding_box[3])]], columns=('ID', 'Classname', 'x_min', 'y_min', 'x_max', 'y_max'))
            df = df.append(df_new, ignore_index=True)
    except:
        None

    return df


