class hparams:

    train_or_test = 'train'
    output_dir = 'logs/adam_runet'
    aug = None
    latest_checkpoint_file = 'checkpoint_latest.pt'
    total_epochs = 10000000
    epochs_per_checkpoint = 1
    batch_size = 16
    ckpt = None
    init_lr = 0.005
    scheduer_step_size = 20
    scheduer_gamma = 0.95
    debug = False
    mode = '3d' # '2d or '3d'
    in_class = 1
    out_class = 1

    crop_or_pad_size = 64,64,64 # if 2D: 256,256,1
    patch_size = 64,64,64 # 128,128,64 if 2D: 128,128,1

    # for test
    patch_overlap = 48,48,48 # if 2D: 4,4,0

    fold_arch = '*.nii.gz'

    save_arch = '.nii.gz'

    source_train_dir = 'dataset/train_source'
    label_train_dir = 'dataset/train_label'
    loc_train_dir = 'dataset/train_loc'

    source_test_dir = 'dataset/test_source'
    label_test_dir = 'dataset/test_label'

    output_dir_test = 'results/adam_runet/test'
