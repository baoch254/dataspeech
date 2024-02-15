from datasets import load_dataset
from multiprocess import set_start_method
from dataspeech import rate_apply, pitch_apply, snr_apply
import torch
import argparse
from accelerate.logging import get_logger

logger = get_logger(__name__)

if __name__ == "__main__":
    set_start_method("spawn")
    parser = argparse.ArgumentParser()
    
    
    parser.add_argument("dataset_name", type=str, help="Repo id.")
    parser.add_argument("--configuration", default=None, type=str, help="Dataset configuration to use.")
    parser.add_argument("--dump_folder_path", default=None, type=str, help="If specified, save the dasaset on disk.")
    parser.add_argument("--repo_id", default=None, type=str, help="If specified, push the model to the hub.")
    parser.add_argument("--audio_column_name", default="audio", type=str, help="Audio column name.")
    parser.add_argument("--text_column_name", default="text", type=str, help="Text column name.")
    parser.add_argument("--rename_column", action="store_true", help="If activated, rename audio and text column names to 'audio' and 'text'. Useful if you wan't to merge datasets afterwards.")
    parser.add_argument("--cpu_num_workers", default=1, type=int, help="Number of CPU workers for transformations that don't use GPUs or if no GPU are available.")
    parser.add_argument("--cpu_writer_batch_size", default=1000, type=int, help="writer_batch_size for transformations that don't use GPUs. See: https://huggingface.co/docs/datasets/v2.17.0/en/package_reference/main_classes#datasets.Dataset.map.writer_batch_size")
    parser.add_argument("--batch_size", default=16, type=int, help="Batch size when relevant") # TODO: better description

    args = parser.parse_args()
    
    if args.configuration:
        dataset = load_dataset(args.dataset_name, args.configuration)
    else:
        dataset = load_dataset(args.dataset_name)
        
    audio_column_name = "audio" if args.rename_column else args.audio_column_name
    text_column_name = "text" if args.rename_column else args.text_column_name
    if args.rename_column:
        dataset = dataset.rename_columns({args.audio_column_name: "audio", args.text_column_name: "text"})


    logger.info("Compute speaking rate")
    rate_dataset = dataset.map(
        rate_apply,
        with_rank=False,
        num_proc=args.cpu_num_workers,
        writer_batch_size= args.cpu_writer_batch_size,
        remove_columns=[audio_column_name]
    )

    logger.info("Compute snr and reverb")
    snr_dataset = dataset.map(
        snr_apply,
        batched=True,
        batch_size=args.batch_size,
        with_rank=True if torch.cuda.device_count()>0 else False,
        num_proc=torch.cuda.device_count() if torch.cuda.device_count()>0 else args.cpu_num_workers,
        remove_columns=[audio_column_name]
    )
    
    logger.info("Compute pitch")
    pitch_dataset = dataset.map(
        pitch_apply,
        batched=True,
        batch_size=args.batch_size,
        with_rank=True if torch.cuda.device_count()>0 else False,
        num_proc=torch.cuda.device_count() if torch.cuda.device_count()>0 else args.cpu_num_workers,
        remove_columns=[audio_column_name]
    )
        
    for split in dataset.keys():
        dataset[split] = pitch_dataset[split].add_column("snr", snr_dataset[split]["snr"]).add_column("c50", snr_dataset[split]["c50"])
        dataset[split] = dataset[split].add_column("speaking_rate", rate_dataset[split]["speaking_rate"]).add_column("phonemes", rate_dataset[split]["phonemes"])
    
    if args.dump_folder_path:
        logger.info("Saving to disk...")
        dataset.save_to_disk(args.dump_folder_path)
    if args.repo_id:
        logger.info("Pushing to the hub...")
        if args.configuration:
            dataset.push_to_hub(args.repo_id, args.configuration)
        else:
            dataset.push_to_hub(args.repo_id)
    