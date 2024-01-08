import os

s_dir = '/root/lilin.gll/workspace/dataset/zcmu/'
d_train_s_dir = 'dataset/train_source/'
d_train_l_dir = 'dataset/train_label/'
d_test_s_dir = 'dataset/zcmu_test_source/'
d_test_l_dir = 'dataset/zcmu_test_label/'
d_train_loc_dir = 'dataset/train_loc/'

filenames = os.listdir(s_dir + 'niiori')
cand = [
'11',
'12',
'21',
'2',
'4',
'9',
'17',
'24',
'20',
'15'
]

for f in filenames:
    num = f.split('_')[0]
    if num in cand:
        cmd = 'ln -s ' + s_dir + 'niiori/' + f + ' ' + d_test_s_dir + 'source_' + num + '.nii'
        os.system(cmd)
        cmd = 'ln -s ' + s_dir + 'anno/' + num + '_merge.nii.gz ' + d_test_l_dir + 'label_' + num + '.nii.gz'
        os.system(cmd)
    else:
        cmd = 'ln -s ' + s_dir + 'niiori/' + f + ' ' + d_train_s_dir + 'source_' + num + '.nii'
        os.system(cmd)
        cmd = 'ln -s ' + s_dir + 'anno/' + num + '_merge.nii.gz ' + d_train_l_dir + 'label_' + num + '.nii.gz'
        os.system(cmd)
        cmd = 'ln -s ' + s_dir + 'locs/' + num + '_loc.txt ' + d_train_loc_dir + 'loc_' + num + '.txt'
        os.system(cmd)
