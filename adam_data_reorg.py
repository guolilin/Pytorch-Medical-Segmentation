import os

s_dir = '/root/lilin.gll/workspace/dataset/ADAM/'
d_train_s_dir = 'dataset/train_source/'
d_train_l_dir = 'dataset/train_label/'
d_test_s_dir = 'dataset/test_source/'
d_test_l_dir = 'dataset/test_label/'
d_train_loc_dir = 'dataset/train_loc/'

filenames = os.listdir(s_dir)
cand = [
'10056F',
'10071F',
'10076F',
'10063F',
'10055F',
'10057B',
'10069B',
'10043',
'10051F',
'10032'
]

idx = 1
idx_train = 10000
idx_test = 10000
for f in filenames:
    with open(s_dir + f + '/location.txt') as loc:
        has_ia = len(loc.readlines())
    if has_ia == 0:
        continue
     
    if f in cand:
        cmd = 'ln -s ' + s_dir + f + '/pre/TOF.nii.gz ' + d_test_s_dir + 'source_' + f + '.nii.gz'
        os.system(cmd)
        cmd = 'ln -s ' + s_dir + f + '/aneurysms.nii.gz ' + d_test_l_dir + 'label_' + f + '.nii.gz'
        os.system(cmd)
    else:
        cmd = 'ln -s ' + s_dir + f + '/pre/TOF.nii.gz ' + d_train_s_dir + 'source_' + f + '.nii.gz'
        os.system(cmd)
        cmd = 'ln -s ' + s_dir + f + '/aneurysms.nii.gz ' + d_train_l_dir + 'label_' + f + '.nii.gz'
        os.system(cmd)
        cmd = 'ln -s ' + s_dir + f + '/location.txt ' + d_train_loc_dir + 'loc_' + f + '.txt'
        os.system(cmd)
