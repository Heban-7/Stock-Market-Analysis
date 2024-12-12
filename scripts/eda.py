# Load Data
def load_data(filepath):
    df = pd.read_cv(filepath)
    return df

def info(data):
    df = data.info()
    return df

