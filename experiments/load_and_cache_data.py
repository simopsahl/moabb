import moabb

def load_and_cache_data(datasets: list[moabb.datasets.base.BaseDataset], path: str):
    from moabb import set_log_level
    set_log_level("info")
    from tqdm import tqdm
    for dataset in tqdm(datasets, desc="Loading datasets"):
        dataset.get_data(cache_config=dict(use=True, path=path, save_raw=True))

# This script is used to load and cache the data for the experiments.

if __name__ == "__main__":
    OUTPUT_PATH = "/mnt/results/sopsahl/moabb/data/raw"
    datasets = [moabb.datasets.Zhou2016(), moabb.datasets.alex_mi.AlexMI()]
    load_and_cache_data(datasets, OUTPUT_PATH)