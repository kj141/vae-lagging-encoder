
params={
    'enc_type': 'lstm',
    'dec_type': 'lstm',
    'nz': 32,
    'ni': 300,
    'enc_nh': 256,
    'dec_nh': 256,
    'dec_dropout_in': 0.5,
    'dec_dropout_out': 0.5,
    'batch_size': 32,
    'epochs': 100,
    'test_nepoch': 5,
    'train_data': '/home/kujain/LanguageVAE/data/ptb.train.txt',
    'val_data': '/home/kujain/LanguageVAE/data/ptb.valid.txt',
    'test_data': '/home/kujain/LanguageVAE/data/ptb.test.txt'
}
